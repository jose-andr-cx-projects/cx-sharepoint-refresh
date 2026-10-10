import base64
import html
import json
import os
import re
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote, urlencode, urlparse
from urllib.request import Request, urlopen

import markdown

SITE = os.environ['ATLASSIAN_SITE'].rstrip('/')
EMAIL = os.environ['ATLASSIAN_EMAIL']
TOKEN = os.environ['ATLASSIAN_API_TOKEN']
SPACE_KEY = os.environ['CONFLUENCE_SPACE_KEY'].strip()
MODE = os.environ['PUBLISH_MODE']

if urlparse(SITE).scheme != 'https':
    raise RuntimeError('ATLASSIAN_SITE must begin with https://')
if SPACE_KEY != 'cex':
    raise RuntimeError('Expected lowercase Confluence space key cex')
if MODE not in ('validate', 'publish'):
    raise RuntimeError('Invalid PUBLISH_MODE')


def api(method, path, payload=None):
    if not path.startswith('/wiki/'):
        raise RuntimeError('Only Confluence API paths are allowed')
    data = json.dumps(payload).encode('utf-8') if payload is not None else None
    secret = base64.b64encode(f'{EMAIL}:{TOKEN}'.encode()).decode()
    req = Request(
        SITE + path,
        data=data,
        method=method,
        headers={
            'Authorization': 'Basic ' + secret,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
    )
    try:
        with urlopen(req, timeout=40) as response:
            body = response.read()
            return json.loads(body) if body else {}
    except HTTPError as exc:
        raise RuntimeError(
            f'Confluence {method} failed (HTTP {exc.code}) at {path.split("?")[0]}'
        ) from None


def all_results(path):
    results = []
    while path:
        response = api('GET', path)
        results.extend(response.get('results', []))
        next_path = response.get('_links', {}).get('next')
        if next_path and next_path.startswith('https://'):
            parsed = urlparse(next_path)
            if parsed.netloc != urlparse(SITE).netloc:
                raise RuntimeError('Unexpected pagination domain')
            next_path = parsed.path + ('?' + parsed.query if parsed.query else '')
        path = next_path
    return results


# Exact-key lookup avoids accepting a misleading first listing result.
direct = api('GET', '/wiki/rest/api/space/' + quote(SPACE_KEY, safe=''))
print('Direct space key:', direct.get('key'))
print('Direct space ID:', direct.get('id'))
# Bitbucket read-only validation found all four pages in the observed space.
EXPECTED_SPACE_ID = '68452354'
if not direct.get('id'):
    raise RuntimeError('Confluence space ID is missing')
space_id = str(direct['id'])
if space_id != EXPECTED_SPACE_ID:
    raise RuntimeError('Unexpected Confluence space ID; stopping')

targets = {
    'SP-Refresh - Project Management': [
        'project_overview.md', 'scope_and_delivery_plan.md',
        'ways_of_working.md', 'decision_log.md', 'risk_and_dependency_log.md',
    ],
    'SP-Refresh - Discovery and Content Audit': ['discovery_and_content_audit.md'],
    'SP-Refresh - Experience and Content Design': ['experience_and_content_design.md'],
    'SP-Refresh - Scoping Playback': ['scoping_playback.md'],
}


def find_unique(title):
    items = all_results('/wiki/api/v2/pages?' + urlencode({
        'space-id': space_id,
        'title': title,
        'status': 'current',
        'limit': 100,
    }))
    matches = [item for item in items if item.get('title') == title]
    if len(matches) != 1:
        raise RuntimeError(
            f'Expected one existing page named {title!r}; found {len(matches)}. No changes made.'
        )
    return matches[0]


def render(filenames):
    sections = []
    for filename in filenames:
        path = Path('docs') / filename
        if not path.is_file():
            raise RuntimeError(f'Missing source document {path}')
        source = path.read_text(encoding='utf-8')
        # Official-only publishing boundary: reject collaboration-only references.
        # Run in BOTH validation and publication, before any Confluence writes.
        prohibited = re.search(
            r'(?i)github|collaboration mirror|collaboration workspace|'
            r'github[ ]*[→-][ ]*bitbucket',
            source,
        )
        if prohibited:
            raise RuntimeError(
                f'Official publishing content check failed in {path}: '
                f'found {prohibited.group(0)!r}. '
                'Remove unofficial workflow references before publishing.'
            )
        # Avoid broken repository-relative Markdown links in Confluence.
        source = re.sub(r'\[([^\]]+)\]\((?:\.\./)?docs/[^)]+\.md\)', r'\1', source)
        source = re.sub(r'\[([^\]]+)\]\([a-zA-Z0-9_./-]+\.md\)', r'\1', source)
        sections.append(markdown.markdown(source, extensions=['tables'], output_format='xhtml'))
    return '\n<hr/>\n'.join(sections)


# Resolve all targets and source documents before any writes.
resolved = [(title, find_unique(title), render(names)) for title, names in targets.items()]
for title, page, body in resolved:
    print(f'OK: {title} (page ID {page["id"]}; HTML {len(body)} chars)')

if MODE == 'validate':
    print('READ-ONLY VALIDATION PASSED — no pages created or updated.')
else:
    # Validation succeeded; publishing still requires explicit approval.
    if os.environ.get('CONFLUENCE_TARGETS_APPROVED') != 'true':
        raise RuntimeError('Publishing blocked: explicit approval required')
    # Publishing replaces the full body of each existing Confluence page.
    for title, page, body in resolved:
        current = api('GET', f'/wiki/api/v2/pages/{page["id"]}?body-format=storage')
        if str(current.get('spaceId')) != space_id or current.get('title') != title:
            raise RuntimeError(f'Page identity changed for {title}; stopping')
        version = current['version']['number']
        commit = html.escape(os.environ.get('BITBUCKET_COMMIT', 'unknown'))
        footer = (
            '<hr/><p>Generated from CX SharePoint Refresh Markdown; '
            f'Bitbucket commit: {commit}. '
            'Review status remains as marked in source documents.</p>'
        )
        payload = {
            'id': str(page['id']),
            'spaceId': space_id,
            'status': 'current',
            'title': title,
            'body': {'representation': 'storage', 'value': body + footer},
            'version': {
                'number': version + 1,
                'message': 'Sync from controlled project Markdown',
            },
        }
        api('PUT', f'/wiki/api/v2/pages/{page["id"]}', payload)
        print(f'UPDATED: {title} (page ID {page["id"]})')
    print('Four existing pages updated; no Jira operations performed.')
