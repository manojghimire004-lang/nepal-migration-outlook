# Nepal Migration Outlook

A survey-informed web prototype exploring whether someone's circumstances lean toward leaving Nepal within three years. Visitors answer six questions and receive an outlook with explanations. Answers are processed in the browser and are not saved.

## Project story

I used Jotform to work with a youth opportunity, migration and return-intent survey from Nepal. I translated findings from 72 responses into a structured CSV, added a reproducible Python cleaning and validation step, and built an interactive HTML/CSS/JavaScript questionnaire. This repository packages the work for review, version control and publication through GitHub.

The project was developed with AI assistance. The initial findings export was produced from Jotform's AI analysis summaries, and the Python cleaning step was added afterward. The Python script cleans the aggregate findings file; it does not clean or reconstruct individual survey submissions. The source code and checks make the workflow inspectable rather than relying only on generated output.

## What I built

- A findings dataset with counts, denominators, percentages, themes and limitations.
- A Python script that strips surrounding whitespace, checks numeric types and ranges, removes exact duplicate rows, preserves missing values and reconciles percentages against counts.
- A responsive questionnaire with input validation, reset behavior and explanations.
- A transparent scoring prototype and documented assumptions.
- A GitHub-ready project with a reproducible workflow and deployment instructions.

## Run it

Requires Python 3 for the cleaning step. No third-party Python packages are needed.

```sh
python clean_findings.py
python -m http.server 8000
```

Open http://localhost:8000. You can also open `index.html` directly.

## Findings

| Metric | Combined summary |
| --- | --- |
| Responses | 72 |
| Planned to leave within three years | 46 of 72 (63.9%) |
| Students | 60 of 72 (83.3%) |
| Family abroad | 47 of 72 (65.3%) |

Source: [Youth Opportunity, Migration, and Return Intent Survey (Nepal)](https://form.jotform.com/261077009071047). Findings were retrieved on September 30, 2026. Some counts were reconstructed from rounded percentages in two groups of 36. The source file includes row-level provenance and caveats. No raw personal responses are included.

## Method and limits

The questionnaire asks about job satisfaction, education satisfaction, career growth, priorities, family abroad and migration preparations. A chosen rule-based score ranges from 0 to 21: 0–6 leans toward staying, 7–13 is uncertain and 14–21 leans toward leaving. The interface documents every contribution.

This is **not a trained machine learning model**. Weights and thresholds are design choices, not measured associations. Aggregate summaries cannot establish individual predictors or predictive accuracy. The 63.9% survey statistic is not a visitor's personal probability. Preparations reflect self-reported readiness and are not independent evidence of future migration.

The sample is small and concentrated among students and Bagmati/Koshi respondents. Conditional questions contain skipped answers, and some group-level statistics lack clear denominators. Approximate combined means assume equal valid response counts. No national representativeness, causal relationship, employment qualification or model accuracy is claimed.

## Skills this portfolio demonstrates

| Skill | Evidence a reviewer can inspect |
| --- | --- |
| Survey analysis | Translating a research question into findings with sample limits |
| Python fundamentals | CSV parsing, functions, argument parsing, exceptions and validation |
| Data quality | Missing-value handling, duplicate removal, range checks and reconciliation |
| Statistical reasoning | Separating sample rates from personal predictions; avoiding unsupported claims |
| Frontend development | Semantic forms, JavaScript state, responsive CSS and accessible labels |
| Quality assurance | Input checks and representative scoring cases |
| Technical communication | Methodology, provenance, reproducible commands and limitations |
| Version control | A reviewable repository suitable for commits and change history |

These are project examples, not a certification of independent mastery. I should be able to explain the code, modify it without relying entirely on AI, and reproduce the results during an interview.

## Skills to strengthen for analyst or developer applications

Requirements vary by employer and role. For analyst positions, useful next demonstrations are SQL joins and aggregations, Excel or a BI dashboard, descriptive statistics and a short business recommendation supported by evidence. O*NET lists SQL and Python among technologies for [Business Intelligence Analysts](https://www.onetonline.org/link/summary/15-2051.01). For developer positions, extend this project with modular JavaScript, meaningful automated tests, accessibility checks and a documented deployment workflow.

For a future machine learning version, obtain consented respondent-level data with an explicit target, establish a baseline, avoid target leakage, separate training and evaluation data, and report precision, recall, calibration and uncertainty. A larger sample and external validation would be necessary before claiming dependable personal predictions. Python appears among the employer-demanded technologies for [Data Scientists](https://www.onetonline.org/link/hot_tech/15-2051.00).

## Resume wording

> Developed a survey-informed migration outlook prototype using Jotform findings from 72 responses, Python CSV cleaning and validation, and an interactive HTML/CSS/JavaScript interface; documented sample bias and scoring assumptions in a reproducible GitHub portfolio project.

Use “published with GitHub Pages” only after a working GitHub Pages deployment is verified. Do not describe this version as a trained AI predictor or claim accuracy metrics.

## GitHub Pages

After uploading the repository, go to Settings → Pages, choose “Deploy from a branch,” select the default branch and `/(root)`, then save. The app's assets use relative URLs. GitHub Pages publishes the website; GitHub repository hosting alone does not make the application live. A Pages site may be publicly accessible even when repository access is restricted, depending on account settings.

## Files

```text
index.html                 Interactive app
app.js                     Questionnaire and scoring
survey_findings_source.csv Original aggregate summary
survey_findings_clean.csv  Validated aggregate summary
clean_findings.py       Reproducible cleaning step
check_scoring.mjs         Representative scoring checks
```
