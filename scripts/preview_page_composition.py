"""Read-only Confluence page composition preview. Never contacts Atlassian."""
import argparse
import json
import re
from pathlib import Path

HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
PROHIBITED = re.compile(r"(?i)github|collaboration mirror|collaboration workspace")


def select_section(source, heading):
    lines = source.splitlines()
    matches = [(i, len(m.group(1))) for i, line in enumerate(lines)
               if (m := HEADING.match(line)) and m.group(2).strip() == heading]
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one section {heading!r}, found {len(matches)}")
    start, depth = matches[0]
    end = next((i for i in range(start + 1, len(lines))
                if (m := HEADING.match(lines[i])) and len(m.group(1)) <= depth), len(lines))
    return "\n".join(lines[start:end]).strip()


def compose(config, root):
    if config.get("schema_version") != 1:
        raise ValueError("Expected schema_version: 1")
    pages = config.get("pages")
    if not isinstance(pages, list) or not pages:
        raise ValueError("Nonempty pages array required")
    output = []
    used_ids = set()
    for page in pages:
        pid, title = page["id"], page["title"]
        if pid in used_ids:
            raise ValueError(f"Duplicate page id: {pid}")
        used_ids.add(pid)
        taxonomy = page.get("taxonomy")
        if taxonomy:
            level = taxonomy.get("level")
            stages = taxonomy.get("stages", [])
            if level not in ("4Ds", "4ds") or not stages or any(
                s not in ("Discover", "Define", "Develop", "Deliver") for s in stages
            ):
                raise ValueError(f"Invalid 4Ds/4ds taxonomy on {pid}")
            if level == "4ds" and not taxonomy.get("parent"):
                raise ValueError(f"Inner loop {pid} requires parent")
        rendered = [f"# {title}"]
        references = []
        for section in page.get("sections", []):
            rel = Path(section["file"])
            target = (root / rel).resolve()
            if target != root.resolve() and root.resolve() not in target.parents:
                raise ValueError(f"Unsafe path: {rel}")
            if not target.is_file() or target.suffix != ".md":
                raise ValueError(f"Missing Markdown source: {rel}")
            body = select_section(target.read_text(encoding="utf-8"), section["heading"])
            if PROHIBITED.search(body):
                raise ValueError(f"Publishing boundary failed: {rel} / {section['heading']}")
            rendered.append(body)
            references.append(f"{rel}#{section['heading']}")
        if not references:
            raise ValueError(f"Page {pid} has no selected sections")
        output.append({"id": pid, "title": title, "taxonomy": taxonomy,
                       "work": page.get("work"),
                       "information_types": page.get("information_types", []),
                       "governance": page.get("governance"),
                       "sources": references, "markdown": "\n\n".join(rendered) + "\n"})
    return output


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="publishing.json")
    ap.add_argument("--root", default=".")
    ap.add_argument("--output", default="build/confluence-preview")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    config = json.loads((root / args.config).read_text(encoding="utf-8"))
    pages = compose(config, root)
    out = (root / args.output).resolve()
    if out != root and root not in out.parents:
        raise ValueError("Preview output must stay inside repository")
    out.mkdir(parents=True, exist_ok=True)
    for page in pages:
        (out / (page["id"] + ".md")).write_text(page["markdown"], encoding="utf-8")
    (out / "manifest.json").write_text(json.dumps([
        {k: v for k, v in page.items() if k != "markdown"} for page in pages
    ], indent=2), encoding="utf-8")
    print(f"READ-ONLY: composed {len(pages)} pages into {out}; no Atlassian requests or writes")


if __name__ == "__main__":
    main()
