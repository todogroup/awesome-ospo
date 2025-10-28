
# Caution. Not an Instructions file. This is a README meant for humans

## Introduction to dependency risk instruction files

Dependency risk instruction files are designed to provide detailed guidance for Copilot, when in agent mode, on where to get information and how to assess the risks of using a third-party package or library in software development, as well as how to format that information into a standardized dependency risk report in the chat window that is easily scannable and understandable by developers such that they make better informed decisions about dependency consumption. 

_See the [example dependency risk report for welly](#example-dependency-risk-report) at the bottom of this file._

The goal is to support the following visions:

- “Copilot should help me make healthier choices of dependencies.”
- "It should be obvious if Copilot suggests a fake package to use."

These instructions are meant to be called when:

1. Copilot is explicitly asked about the riskiness, health, quality, or security posture of a package or library.
2. Copilot suggests a new package or library.

The instructions are split into four files to allow for flexibility in ownership and customization
of different parts of the instructions over time, for instance between a centralized
Open Source Programs Office and individual development teams. This is explained in more detail below in the
section titled ["Why not a single instructions file"](#why-not-a-single-instructions-file)
What risks are currently flagged to users is detailed in the section
["Types of dependency risks"](#types-of-dependency-risks) These instruction files are meant as an
example of what can be done. You can edit or extend to match your own needs or internal company policies.

### How to use generally

Copy and paste all four of the instruction files in this directory into your repository's `.github/instructions/` directory.
Ask Copilot Chat agent mode a question like "What can you tell me about the security and community health of the python package welly?"
These instructions were created while using the GPT-4o model.
Performance has been observed to be more variable with other models.

If you have a new MCP tool or additional source of information for one of the
dependency risk categories, you can explore trying to add instructions for how to access that data
to either the company or repository level instructions files.

### How to test run in this repository

Although instructions should normally go in the `.github/instructions` directory if using them regularly, you can test run these instructions in a code spaces of this repository by asking Copilot in agent mode to _"use instructions found in the `instructions/dependency-risks` directory to answer the following question: tell me about the community health and security of npm package lunr "_.

### Disclaimer

These instructions are not exhaustive and do not replace any required compliance processes that you may be required to
follow based on writing code for a company or organization. They definitely do not surface all risks, nor is there
any guarantee that the information is up-to-date or accurate. Much of the data is sourced from either public metadata
repositories, package managers, or GitHub source repository pages, so information in some cases could be manipulated
by the package authors or maintainers.
Open ended questions posed to Copilot create more uncertainty in reliability of responses, so it is advisable to limit questions to known information in the metadata sources, which should be considered untrusted.

The dependency risk report prototype is meant to provide a quick reference that sometimes flags for
developers risks identifiable with publicly available metadata. It tries to do this at the point when
using a package is being first considered in their IDE (Integrated Development Environment), as this
is when switching costs are lowest. Users are encouraged to leverage the report as a starting point only
and to visit the suggested links to find more information.

## Why not a single instructions file?

The dependency risk instructions are split into four files to allow for different parts of the instructions
to be owned and maintained by different parties, then combined. While all the files are local files
now, one or more files could be externally defined. While Copilot will normally will not accept
externally defined instructions, it will if the instruction files include instructions to ask
the user for permission first and then the user explicitly allows it, as is seen in the
`dependencyRisk.instructions.md` file.

The benefit of this approach is it is possible to then have one or more of the instructions files
for how to generate the dependency risk report sit outside the repository, either in a MCP
tool or external repository. This allows for the company-level instructions to be somewhere
controlled by a centralized team, such as an open source programs office (OSPO) or a centralized
engineering team. These centrally controlled instruction files can be evolved over time and
point to newly created internal MCPs without needing to make pull requests to every repository
that wants to be able to generate a dependency risk report, minimizing problems with instruction
file staleness over time. At the same time, you can have repository-level preferences for styling,
or even stricter thresholds for some metrics, controlled in repository-specific instruction files
that get combined with the externally defined instructions to form a single end user experience.

In summary, this approach of layering instruction files into one joint instruction file allows for
the end-user experience from instruction files to be a combination of centralized team standards
and tooling with the repository-specific needs without frequent repeated pull requests across large
numbers of repositories.

The four files that layer on top of one another are described in more details below.

### Central instructions file that only points to the others

The `dependency-risk.instructions.md` file mostly just defines when the instructions files are used and points to
the other three dependency risk report instruction files. If any of the other instruction files
are externally defined or in MCPs, there is a line in this instruction files that asks the user
for permission to fetch them.

### Base level instructions file

The basics of where to find package and source repository metadata, how to process it,
and how to structure the dependency risk report is found in the
`dependency-risk-base-level.instructions.md` file. The other dependency risk report
instruction files' instructions layer on top of these base instructions and in some
cases may overrule them or in other cases merely extend.

### Repository specific instructions file

The `dependency-risk-repository-level.instructions.md` file is where repository-specific instructions can be placed that reflect an individual repository's preferences. Developers might decide a repository should have stricter or looser threshold for a particular risk based on what that repository is used for and how long it is designed to persist. For example, they might want to shift the threshold for how long ago is the last version update of a package to be 90 days instead of 2 years on the most critical projects that require fast pull
request response times. Alternatively, they might change that threshold to be less strict for
small NPM packages that are more likely to be feature-complete, or they might want different styling
to emphasize certain risks.

### Company specific instructions file

As a company might provide dependency-related tooling in an MCP or API format, instructions about
these can be in the `dependency-risk-company-level.instructions.md` file.
This file could alternatively have no additional instructions.

## Helping developers make better dependency consumption choices

We know developers too often choose dependencies based on familiarity or convenience rather than health,
security, and quality. Developers have also reported using packages that Copilot suggests without
additional checking if they exist or are risky.

To minimize these risks and encourage more well informed choices, the dependency risk report will
generate in the Copilot chat window when in agent mode when the user requests or Copilot suggests
a new package to use. As the dependency report can generate fully in 0.5-2 minutes and is in their
IDE (Integrated Development Environment), it is hoped the information will be more likely to
be considered than if they had to remember to do the research, leave their IDE, and spend 10-30 minutes
manually researching the same information across package managers, source repositories, and others locations.

## Types of dependency risks

It can be helpful to think of dependency risks in terms of two classes of risks, continuous and binary.
Binary risks are either present or not, with clear yes/no answers, which makes them fit well into compliance frameworks
and compliance tooling that can be deployed across an entire organization with the same thresholds and rules.
Continuous risks in contrast are risks that tend to exist on a continuous spectrum of risks and different projects
can reasonably have different thresholds for what is acceptable risk.

### Differences Between Binary and Continuous Risks

| Risk Class  | Definition                                                                 | Impact Felt At What Scale | Impact Types                        | Risks Best Addressed By What Type of Framework?         | Often Modified By What Instructions File                |
|-------------|----------------------------------------------------------------------------|------------------------------------------------|-------------------------------------|---------------------------------------------------------|--------------------------------------------------------|
| Binary      | Risks that are either present or not, with clear yes/no answers.            | Company-scale | $, reputation, trust                | compliance frameworks | Company-specific instructions file (`dependencyRisk.companyLevel.instructions.md`) |
| Continuous  | Risk presence is a continuous spectrum. Always some risk.          | Individual team   | unplanned for developer time        | risk-reduction frameworks | Repository-specific instructions file (`dependencyRisk.repositoryLevel.instructions.md`) |

### Types of dependency risk considered by the dependency risk report

| Risk Class    | Risk                      | Definition                                                                 | Factors Considered in Report                                                                                 |
|---------------|---------------------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Binary        | Vulnerability             | Whether known security vulnerabilities are associated with the dependency based on a CVE.        | Report uses public vulnerability databases reflected in ecosyste.ms. and sometimes vulnerability information on source repository in GitHub. Use other tools for full assessment!                        |
| Binary        | License                   | License of the package.            | Currently, only the first identified licenses is surfaced to the user.  Does not cover multiple licenses, modified licenses, whether copyleft license, tell you what licenses require extra steps, etc. Use other tooling for actual license compliance!              |
| Binary        | Malicious                 | Whether the package contains known or suspected malicious code.               | Currently, this does nothing but tell you to use your own tooling and check for company instructions file for listed tooling. It is a placeholder.       |
| Continuous    | Possibly abandoned _(sustainability)_        | Assesses if the dependency appears to be no longer maintained.              | Considers time since last release, lack of recent activity, if source repository is archived, etc.               |
| Continuous    | Not enough eyeballs _(sustainability)_     | Evaluates if there are too few contributors or reviewers to catch issues.   | Considers number of downloads, number of dependent repositories.                   |
| Continuous    | Contribution could stop suddenly _(sustainability)_ | Considers the risk that development may halt unexpectedly.           | Considers reliance on a single maintainer, if number of contributors is small, if only single version published, too few commits recently, etc.  |
| Continuous    | Poor security posture     | Assesses the overall security posture of the project.  | Considers low OpenSSF Scorecard score, if uses a dangerous GitHub Action workflow pattern, etc. Note that not all packages will have pre-existing scans by OpenSSF Scorecard |

**Use other tooling to assess the risk of license complications, malicious code, and security vulnerabilities as the dependency risk report generated is not exhaustive!**
However, it may still be useful to you if it flags a risk earlier than your
other tooling that flags one of these risks at pull request time or at build time.

#### What parts of continuous risk can be assessed well with publicly available metadata alone as these instructions try to do?

Continuous risks can be thought of as including three partially overlapping categories:
sustainability risks, quality risks, and security posture risks.
Sustainability risks can include "Possibly abandoned", "Not enough eyeballs to spot bugs", and
"Contribution could stop suddenly". While sustainability risks are often possible to identify with
package and source repository metadata publicly available in 2025 as they are largely activity-based
and community-based measurements, quality risks and security posture risks often require either
manual evaluation of the source code or additional scans of the source code itself to assess well.
When OpenSSF scorecard data exists, it is surfaced in the dependency risk report for security
posture information.

## Example dependency risk report

The following is an example of a dependency risk report generated by an earlier version of these
instruction files.

### Dependency risk report chat record for python package welly

-------------------------------

**User:**
Tell me about the community health and security of python package welly

**Copilot:**
Here is a detailed dependency risk report for the Python package welly (latest version: 0.5.2, PyPI):

--

**Indicators of risk: POSSIBLY ABANDONED**

- ✅ The package itself is deprecated: No
- ✅ The source repository is archived: No  
  <https://github.com/agilescientific/welly>
- ❌ The latest version of package was published more than 2 years ago: Yes (2022-02-28)

**Indicators of risk: NOT ENOUGH EYEBALLS TO SPOT PROBLEMS**

- ⚠️ Number of dependent repositories is <500: Yes (29)
- ⚠️ Number of package downloads <10,000: Yes (1,273 last month)

**Indicators of risk: CONTRIBUTION COULD STOP SUDDENLY**

- ✅ Package created at date is < 90 days before today: No (created 2015-11-09)
- ✅ Development distribution score (DDS) is < 0.15: No (0.53)
- ✅ Number of contributors is < 4: No (18 contributors)
- ✅ Number of package maintainers is <2: No (2 maintainers)
- ✅ Only a single version of the package has ever been published: No (25 versions published)
- ✅ There have been <3 commits in the past 365 days: No (many commits, including July 2025)
- ✅ All the commits in past 365 days are from 1 person: No (multiple contributors)
- Pull request page:  
  <https://github.com/agilescientific/welly/pulls>  
  Follow this link to see if pull requests get responses.

**Indicators of risk: POOR SECURITY POSTURE**

- ❔ The repository has a poor security posture based on an overall OpenSSF scorecard score of less than 5: Not found (scorecard API returned invalid URL)
- ❔ The repository has no indications of code review based on scorecard.dev "code-Review" score of less than 5: Not found
- ❔ The repository has a dangerous GitHub Actions workflow pattern based on scorecard.dev "Dangerous-Workflow" score of less than 5: Not found

**Indicators of risk: SECURITY VULNERABILITIES**

- ✅ There are any known vulnerabilities for any version of the package: No (no advisories found)
- Latest version of package: 0.5.2

**Indicators of risk: MALICIOUS CODE**

- ❔ nothing in this report checks for malicious code and you should use other tooling for that risk.

**Indicators of risk: LICENSE COMPLICATIONS**

- License detected: Apache-2.0 (detected only; may not catch multiple licenses or compliance requirements)

-------------------------------

**Summary of triggered risks**

- ❌ Latest version is more than 2 years old (2022-02-28)
- ⚠️ Number of dependent repositories is low (29)
- ⚠️ Number of downloads is low (1,273 last month)

**Key links**

- Ecosyste.ms:  
  <https://packages.ecosyste.ms/api/v1/registries/pypi.org/packages/welly>
- Source repository on GitHub:  
  <https://github.com/agilescientific/welly>
- Contributors graph:  
  <https://github.com/agilescientific/welly/graphs/contributors>
- Pull request page:  
  <https://github.com/agilescientific/welly/pulls>
- Commits over time:  
  <https://github.com/agilescientific/welly/commits>
- OpenSSF scorecard (API):  
  <https://api.scorecard.dev/projects/github.com/agilescientific/welly>
\
Please confirm this information via the provided webpage links and understand users can provide fake information, especially via README or description so be careful with those sources.

This report is not exhaustive and is not a substitute for actual compliance processes you may be required to follow.

-------------------------------

**Package name:** welly
**Package type:** pypi  
**Latest version considered:** 0.5.2

**Instruction file versions used:**

- dependencyRisk.baseLevel.instructions.md: 0.0.18
- dependencyRisk.companyLevel.instructions.md: 0.0.9
- dependencyRisk.repositoryLevel.instructions.md: 0.0.5
- dependencyRisk.instructions.md: 0.0.4

<!-- Version 0.1.01g -->
