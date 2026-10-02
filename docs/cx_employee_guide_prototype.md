# CX Employee Guide — Prototype Implementation

**Status:** Experiment / prototype  
**Project:** CX SharePoint Refresh  
**Purpose:** Provide the working group with a practical, bounded method for building and testing a conversational CX Employee Guide using a small set of authoritative CX content.

## 1. What we are testing

The CX Employee Guide is a conversational navigation layer that helps an employee describe what they are trying to achieve and then guides them to the appropriate CX capability, authoritative source and next step.

It is not a new source of organisational knowledge.

The experiment tests this proposition:

> **Can an employee describe what they are trying to achieve, without knowing CX's structure or terminology, and be guided to the correct authoritative CX resource and next step?**

The experiment should use existing organisational AI capability where practical. It does not establish a requirement for a standalone CX agent, custom development or a new knowledge store.

## 2. Target experience

The basic interaction is:

```text
Employee need
    ↓
CX Employee Guide
    ↓
Understand intent
    ↓
Identify relevant CX capability
    ↓
Retrieve approved CX content
    ↓
Identify authoritative source
    ↓
Explain relevance
    ↓
Provide source + clear next step
```

The underlying content remains authoritative. The Guide retrieves, interprets and routes.

## 3. Worked example — residential parking permits

### Employee question

> I'm starting a project about residential parking permits. I need to understand what customers are struggling with. Can CX help?

### Expected interpretation

| Field | Expected result |
| --- | --- |
| Employee need | Understand customer problems before designing a project |
| Intent | Customer insight |
| CX capability | Customer Insight |
| Authoritative resource | Customer Insights |
| Why it is relevant | Provides existing customer and service evidence |
| Next step | Review available insight; request CX support if existing evidence is insufficient |

### Expected Guide response

> It sounds like you need customer insight before you start designing the project.
>
> CX has customer and service insights that may help you understand common customer needs, pain points and contact drivers.
>
> **Start here → Customer Insights**
>
> If the existing evidence doesn't answer your question, the resource should explain how to request additional CX support.

The prototype must replace the example resource name with the actual approved source and link used in the test.

### Follow-up question

> Actually, I want to map the whole experience customers go through when applying for the permit.

### Expected interpretation

The employee's intent has changed from understanding customers to understanding an end-to-end experience.

| Field | Expected result |
| --- | --- |
| Previous intent | Customer insight |
| New intent | Journey mapping |
| CX capability | Journey Mapping / CX Design |
| Authoritative resource | Journey Mapping Toolkit |
| Relationship to previous result | Customer Insights may provide evidence for the journey map |
| Next step | Open the toolkit and begin the journey-mapping pathway |

### Expected Guide response

> In that case, journey mapping is the more relevant starting point.
>
> **Open → Journey Mapping Toolkit**
>
> Use Customer Insights as evidence when developing the journey.

This follow-up is important because it tests whether the Guide can respond to employee intent rather than simply matching keywords.

## 4. What the working group needs to prepare

Do not catalogue the whole CX intranet.

Start with approximately **five representative employee needs** and **10–20 authoritative content items**.

For every test item, capture:

| Required field | Purpose |
| --- | --- |
| Employee need | What the employee is trying to achieve |
| Employee language | How employees are likely to describe the need |
| CX capability | Relevant CX service or capability |
| Authoritative source | Approved page, resource, tool or service |
| Source link | Direct link to the authoritative source |
| Why/when to use | Short description that helps retrieval |
| Next step | What the employee should do after reaching the source |
| Owner | Who is responsible for the content/service |
| Audience | Who the resource is intended for |
| Status | Current / approved / draft / unknown |
| Related resources | Other useful authoritative sources, where relevant |

Only current, approved and appropriately accessible content should be used as grounding material for the prototype.

## 5. Seed prototype dataset

Use this structure to begin the experiment. Replace working labels with verified project content before testing.

| Employee intent | CX capability | Authoritative resource | When to use it | Expected next step |
| --- | --- | --- | --- | --- |
| Understand customers | Customer Insight | Customer Insights | Need evidence about customers or communities | Review available insight |
| Understand an experience | Journey Mapping | Journey Mapping Toolkit | Need an end-to-end view of a customer experience | Start journey mapping |
| Improve an experience | CX Design | CX improvement guidance | Existing experience has identified friction | Follow the design/improvement pathway |
| Find CX help | CX services | CX offer / service directory | Employee does not know which CX capability is relevant | Identify relevant CX service |
| Get specialist help | Relevant CX capability | Support/contact pathway | Existing resources do not answer the need | Request or contact CX support |

This dataset is the minimum structured context behind the Guide. It is not intended to become another permanent content repository.

## 6. Configure the prototype

Use the smallest existing organisational capability that can:

1. accept natural-language questions;
2. retrieve from the approved test content;
3. maintain conversational context for follow-up questions;
4. return links to source material; and
5. respect existing access permissions.

Do not introduce a new platform solely for this experiment unless existing organisational capability cannot test the hypothesis.

### Prototype behaviour instructions

Use the following as a starting instruction set and adapt it to the selected enterprise tool:

```text
You are the CX Employee Guide.

Your purpose is to help City of Melbourne employees find the appropriate
CX capability, authoritative information and next step.

Use only the approved CX sources provided for this experiment.

When answering:

1. Understand what the employee is trying to achieve.
2. Identify the relevant CX capability where the sources support it.
3. Find the most appropriate authoritative source.
4. Briefly explain why the source is relevant.
5. Link to the authoritative source.
6. Explain the next step where it is known.
7. Preserve relevant conversational context when the employee asks a follow-up.
8. Do not invent organisational processes, policies, ownership or guidance.
9. Do not present unverified information as authoritative.

If the available information does not support a reliable answer:

- say that authoritative guidance could not be found;
- provide the closest relevant approved source if useful; and
- classify the failure for the experiment.
```

## 7. Failure classification

A failed answer is useful evidence.

Classify unsuccessful or unreliable interactions as:

- missing content;
- duplicate or competing sources;
- unclear authoritative source;
- unclear ownership;
- terminology mismatch;
- outdated content;
- inaccessible content;
- poor content structure;
- ambiguous employee need;
- retrieval failure despite suitable content; or
- human judgement / specialist support required.

Do not solve these problems inside the AI prompt if the underlying information environment is the cause.

Feed them back into the SharePoint Refresh content, information architecture and governance backlog.

## 8. Test procedure

For each selected employee scenario:

1. Record the employee question before testing.
2. Record the expected capability, source and next step.
3. Run the task through the proposed navigation/search experience.
4. Run the same task through the CX Employee Guide.
5. Test at least one natural follow-up question.
6. Record whether the Guide reached the expected authoritative source.
7. Record whether the employee understood the next step.
8. Capture incorrect, unsupported or incomplete responses.
9. Classify failures.
10. Identify whether the fix belongs to content, information architecture, governance, retrieval/configuration or the conversational experience.

Where practical, use representative employees rather than only project-team members.

## 9. Evidence to capture

The experiment should capture:

- task success;
- authoritative-source accuracy;
- time or steps to reach the source;
- relevance of the result;
- next-step comprehension;
- unsupported or incorrect answers;
- useful abstentions where the Guide correctly refuses to invent an answer;
- follow-up conversation performance;
- content and governance gaps discovered; and
- qualitative employee feedback.

Establish the baseline during testing rather than inventing success thresholds before evidence exists.

## 10. Guardrails

For the prototype:

- approved organisational sources remain authoritative;
- the Guide must link back to those sources;
- source permissions must not be bypassed;
- do not ingest sensitive or uncontrolled information without approval;
- do not allow the Guide to invent missing organisational policy or process;
- do not make the prototype a duplicate knowledge repository;
- do not give it transactional or autonomous action capability;
- keep employee testing and captured interaction data proportionate to the experiment;
- make uncertainty visible; and
- prefer a clear "I cannot find authoritative guidance" response over a plausible unsupported answer.

## 11. Minimum experiment build

The experiment is ready to run when the working group has:

- selected approximately five employee scenarios;
- identified approximately 10–20 authoritative resources;
- completed the minimum metadata for those resources;
- configured the Guide against that controlled content;
- loaded the prototype behaviour instructions;
- prepared expected answers for the test scenarios;
- confirmed source access and permissions; and
- prepared a simple test log for results and failures.

Anything beyond this should require evidence that it is necessary for the experiment.

## 12. Decision after testing

Use the evidence to decide whether:

- navigation/search already meets the need;
- content or governance needs improvement before conversational assistance;
- existing organisational AI capability is sufficient;
- the CX Employee Guide warrants a broader prototype;
- integration with the future CX information experience should be explored; or
- the concept should stop because it does not provide enough additional value.

A successful experiment does not automatically mean CX should create a permanent standalone agent.

The preferred outcome is the smallest maintainable capability that helps employees reach trusted CX information and services with less effort.

## 13. Working-group starting point

For the first working session, do only this:

1. Select one real employee need from the SharePoint Refresh research.
2. Write the question in the employee's language.
3. Identify the correct CX capability.
4. Identify the authoritative resource.
5. Agree the expected next step.
6. Confirm who owns the source and whether it is current.
7. Add two or three related resources.
8. Run the question and a follow-up through the prototype.

The residential parking permit example in this document can be used as the pattern.

Once that single path works, repeat it for the remaining scenarios.
