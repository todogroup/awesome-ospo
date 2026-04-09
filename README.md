# Awesome OSS Management [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

This list identifies packages and projects that have been built by TODO Group
members or found helpful for managing open source projects and offices.

## Code Reviews

Tools for managing and automating code review processes.
- [PullApprove](https://www.pullapprove.com) - Allows for fancier rules on how pull requests are approved.
- [sentinel](https://github.com/habitat-sh/sentinel) - PR test, review, and merge workflow bot.
- [pull-review](https://github.com/imsky/pull-review) - Assign pull request reviewers intelligently, inspired by mention-bot.
- [pull-request-size](https://github.com/noqcks/pull-request-size) - Automatically adds GitHub labels based on the size of a Pull Request.
- [Pullie](https://github.com/godaddy/pullie) - GitHub App that helps with PRs: requests reviews, links Jira tickets, nags for missing required file changes (e.g. changelog entries).
- [Danger](https://danger.systems/) - Runs during your CI process, and gives teams the chance to automate common code review chores.
- [Reviewable](https://reviewable.io/) - GitHub code reviews done right. Features like side-by-side diffs, real-time collaboration, and batch actions.
- [CodeClimate](https://codeclimate.com/) - Get automated code review for test coverage, maintainability and more so that you can save time and merge with confidence.

## Continuous Integration / Continuous Delivery

CI/CD platforms and tools.

- [GitHub Actions](https://github.com/features/actions) - Automate your workflow from idea to production.
- [Jenkins](https://www.jenkins.io/) - Open source automation server that provides hundreds of plugins to support building, deploying and automating any project.
- [Jenkins X](https://jenkins-x.io/) - Open source CI/CD solution for modern cloud applications on Kubernetes.
- [Ortelius](https://ortelius.io/) - Provides a central catalog of services with their deployment specs, application teams can easily consume and deploy services across cluster.
- [Screwdriver](https://screwdriver.cd/) - Open source build platform designed for Continuous Delivery.
- [Spinnaker](https://spinnaker.io/) - Multi-cloud continuous delivery platform for releasing software changes with high velocity and confidence.
- [Tekton](https://tekton.dev/) - Powerful and flexible open source framework for creating CI/CD systems, allowing developers to build, test, and deploy across cloud providers and on-premise systems.
- [Travis CI](https://www.travis-ci.com/) - A hosted continuous integration service used to build and test software projects hosted at GitHub and Bitbucket.
- [CircleCI](https://circleci.com/) - Cloud-native CI/CD platform that helps developers build, test, and deploy software faster and more reliably.
- [GitLab CI/CD](https://docs.gitlab.com/ee/ci/) - GitLab's built-in continuous integration, delivery, and deployment capabilities.
- [Buildkite](https://buildkite.com/) - Run fast, secure, and scalable continuous integration pipelines on your own infrastructure.

## Contributor License Agreements / Developer Certificate of Origins

CLA and DCO management tools.

- [CLA Assistant](https://github.com/cla-assistant/cla-assistant) - Streamline your workflow and let CLA assistant handle the legal side of contributions to a repository for you. CLA assistant enables contributors to sign CLAs from within a pull request.
- [Dr CLA](https://github.com/salesforce/dr-cla) - GitHub bot for dealing with Contributor License Agreements.
- [DCO Bot](https://github.com/apps/dco) - GitHub App that enforces the Developer Certificate of Origin (DCO) on Pull Requests.
- [EasyCLA](https://github.com/linuxfoundation/easycla) - A Contributor License Agreement (CLA) service used in the Linux Foundation's LFX platform which lets project contributors read, sign, and submit contributor license agreements easily.

## GitHub Metrics and Dashboards

Tools for tracking and visualizing GitHub activity.

- [osstracker](https://github.com/Netflix/osstracker) - An application that collects information about a GitHub organization and aggregates the data across all projects within that organization into a single user interface to be used by various roles within the owning organization.
- [devstats](https://github.com/cncf/devstats) - A toolset to visualize GitHub archives using Grafana dashboards used by the Cloud Native Computing Foundation and Kubernetes.
- [MeasureOSS](https://github.com/MeasureOSS/Measure) - A contributor relationship management system.
- [GrimoireLab](https://chaoss.github.io/grimoirelab/) - Software development analytics platform supporting more than 30 different data sources, part of CHAOSS Software project from The Linux Foundation.
- [Project Portal](https://github.com/SAP/project-portal-for-innersource) - Lists all InnerSource (or Open Source) projects of a company in an interactive and easy to use way. Can be used as a template for implementing the "InnerSource portal" pattern by the InnerSource Commons community.
- [Issue/PR/Discussion Metrics](https://github.com/github/issue-metrics) - A GitHub Action that searches for pull requests/issues/discussions in a repository or organization and measures several available metrics like time to close and time to first response. It calculates the metrics and writes the metrics to a Markdown file. The issues/pull requests/discussions can be filtered by using a search query.
- [Augur](https://github.com/chaoss/augur) - A software suite for collecting and measuring structured data about OSS communities.
- [OSSF Metrics Dashboard](https://insights.oss-scorecard.dev/) - OpenSSF Scorecard's dashboard for tracking and visualizing security metrics for open source projects.
- [OSS Compass](https://github.com/oss-compass/compass-web) - An open source community health analytics platform that provides insights into open source project and ecosystem health.
- [Cauldron](https://cauldron.io/) - Get insights of your software development. Track team performance and software evolution with an easy to use web interface.

## GitHub Management

Tools for managing GitHub organizations and repositories.

- [opensource-management-portal](https://github.com/microsoft/opensource-management-portal) - Microsoft's Open Source Portal for GitHub is a tool to help large organizations with GitHub management operations, onboarding and more. It is implemented in Node.js.
- [hubcommander](https://github.com/Netflix/hubcommander) - A Slack bot for GitHub organization management.
- [GitHub Settings](https://github.com/apps/settings) - Uses .github/config.yml as the source of truth, and any changes to that file in the default branch will update GitHub.
- [Copybara](https://github.com/google/copybara) - A tool for transforming and moving code between repositories.
- [github-org-mgmt](https://github.com/bertvv/github-org-mgmt) - A few scripts for managing a GitHub organization.
- [github-org-scripts](https://github.com/mozilla/github-org-scripts) - Some helper scripts to manage GitHub organizations via API.
- [Automated GitHub Organization Invites](https://github.com/thundergolfer/automated-github-organization-invites) - Host a webpage to allow people to click and receive an invite to your GitHub Organization.
- [Pepper](https://github.com/genuinetools/pepper) - A tool for performing actions on GitHub repos or a single repo.
- [Grit](https://github.com/grailbio/grit) - A tool to mirror monorepo subtrees to GitHub.
- [Sheriff](https://github.com/electron/sheriff) - Controls and monitors organization permissions across GitHub, Slack and GSuite.
- [Mariner Issue Collector](https://github.com/indeedeng/Mariner-Issue-Collector) - Identify open issues across all of your dependencies.
- [Steampipe GitHub Plugin](https://hub.steampipe.io/plugins/turbot/github) - Query GitHub Repositories, Organizations, and other resources with SQL.
- [Powerpipe GitHub Sherlock Mod](https://hub.powerpipe.io/mods/turbot/steampipe-mod-github-sherlock) - Interrogate your GitHub resource configurations to identify improvements based on best practices.
- [(Corporate) Git Proxy](https://github.com/finos/git-proxy) - Scan outgoing attempts to push to public repository and raise compliance/info-sec friendly checks before allowing the push to complete.
- [Stale Repos Action](https://github.com/github/stale-repos) - Get a regular report of inactive repositories in your organization so that you can choose to archive or revive.
- [Forker](https://github.com/marketplace/actions/github-forker) - A GitHub Action that can automate the creation of fork repositories.
- [GitHub Manager](https://github.com/backstage/backstage/tree/master/plugins/github-actions) - Backstage plugin for GitHub management and monitoring.
- [Octokit](https://github.com/octokit) - Official clients and tools for the GitHub API.
- [GitHub CLI](https://cli.github.com/) - Official command line tool for GitHub.

## Governance

Tools for project governance and community management.

- [Minimal Viable Governance](https://github.com/github/MVG) - Currently in beta - is a repository-based approach for putting lightweight governance into free and open source projects that are run in version control systems. It provides an overall two-tier organizational governance structure for a set of free and open source projects.

## Policy and Compliance

- [FOSSA](https://fossa.com/) - Automated license compliance, vulnerability management, and code quality tracking for modern teams.
- [WhiteSource (now Mend)](https://www.mend.io/) - Automated open source security and license compliance management.
- [Snyk](https://snyk.io/) - Find and fix vulnerabilities in open source dependencies and container images.
- [Black Duck](https://www.synopsys.com/software-integrity/security-testing/software-composition-analysis.html) - Comprehensive software composition analysis for security and license compliance.
- [Veracode SCA](https://www.veracode.com/products/software-composition-analysis) - Software composition analysis for identifying open source risk.
- [OSPO Policy Templates](https://github.com/todogroup/policies) - Collection of OSPO policy templates for organizations.

## Community Management

- [Discourse](https://www.discourse.org/) - A platform for community discussion that's modern, open source, and ready to use.
- [Orbit](https://orbit.love/) - Community experience platform that helps organizations build and grow their communities.
- [Common Room](https://www.commonroom.io/) - Community intelligence platform for tracking and engaging community members.
- [Discord](https://discord.com/) - Voice, video, and text communication service used by many open source communities.
- [Slack](https://slack.com/) - Business communication platform widely used by open source projects.
- [Matrix](https://matrix.org/) - Open standard for decentralised communication, used for bridging different chat platforms.

## Dependency Management

- [Renovate](https://renovatebot.com/) - Automated dependency updates for multi-platform and multi-language projects.
- [Dependabot](https://github.com/dependabot) - GitHub's automated dependency update tool.
- [WhiteSource Renovate](https://github.com/whitesource/renovate) - Multi-platform and multi-language dependency update automation.
- [Greenkeeper](https://greenkeeper.io/) - Automated dependency management for npm packages (now part of Snyk).
- [David](https://david-dm.org/) - Dependency monitoring service for Node.js projects.
- [Libraries.io](https://libraries.io/) - The open source discovery service for tracking project dependencies.
- [OSS Index](https://ossindex.sonatype.org/) - Free service for identifying vulnerabilities in open source components.

## Project Quality

Tools for assessing and improving project quality.

- [OpenSSF Best Practices Badge](https://www.bestpractices.dev/) - The Open Source Security Foundation (OpenSSF) Best Practices badge is a way for Free/Libre and Open Source Software (FLOSS) projects to show that they follow best practices. Projects can voluntarily self-certify, at no cost, by using this web application to explain how they follow each best practice. The OpenSSF Best Practices Badge is inspired by the many badges available to projects on GitHub. Consumers of the badge can quickly assess which FLOSS projects are following best practices and as a result are more likely to produce higher-quality secure software.
- [Fosstars](https://github.com/SAP/fosstars-rating-core) - A framework for defining and calculating ratings for open source projects.
- [RepoLinter](https://github.com/todogroup/repolinter) - Lint open source repositories for common issues.
- [Linguist](https://github.com/github-linguist/linguist) - Identify the programming languages used in a project.
- [repo-scaffolding](https://github.com/twitter/repo-scaffolding) - Scaffolding tools for creating and maintaining projects based on Twitter Open Source standards and best practices.
- [Repo Health Check](https://github.com/dogweather/repo-health-check) - Analyze a project: How are the maintainers doing?
- [OpenSSF Scorecard](https://github.com/ossf/scorecard) - Security health metrics for Open Source projects.
- [CHAOSS Metrics](https://chaoss.community/metrics/) - Community-defined metrics for measuring open source project health.
- [All Contributors](https://github.com/all-contributors/all-contributors) - Recognize all contributors to your open source projects, not just code.

## Supply Chain Trust

Tools/frameworks for managing software supply chain security.

- [OpenChain Conformance](https://openchainproject.org) - The OpenChain Specification is a way for companies using Free/Libre and Open Source Software (FLOSS) to show that they meet the key requirements for quality compliance programs. Companies can voluntarily self-certify, at no cost, by using this web application.

## Licensing

Tools for managing and tracking open source licenses.

- [SPDX](https://spdx.dev/) - Set of standards for communicating the components, licenses and copyright associated with a software package.
- [LicenseFinder](https://github.com/pivotal/LicenseFinder) - Find licenses for your project's dependencies.
- [ScanCode toolkit](https://github.com/aboutcode-org/scancode-toolkit) - Scan code for licenses, copyright and dependencies.
- [FOSSology](https://www.fossology.org) - Scan code for license, copyright and export control information.
- [Licensee](https://github.com/licensee/licensee) - Identify a project's license file.
- [askalono](https://github.com/jpeddicord/askalono) - A library and command-line tool to help detect license texts. It's designed to be fast, accurate, and to support a wide variety of license texts.
- [License Classifier](https://github.com/google/licenseclassifier) - A library and set of tools that can analyze text to determine what type of license it contains.
- [OSS Review Toolkit](https://github.com/oss-review-toolkit/ort) - Enables highly automated and customizable open source compliance checks od the source code and dependencies of a project by scanning it, downloading its sources, reporting any errors and violations against user-defined rules, and by creating third-party attribution documentation.
- [fossa-cli](https://github.com/fossas/fossa-cli) - Fast, portable and reliable dependency analysis for any codebase.
- [Licensed](https://github.com/licensee/licensed) - A Ruby gem to cache and verify the licenses of dependencies.
- [LicensePlist](https://github.com/mono0926/LicensePlist) - A command-line tool that automatically generates a Plist of all your dependencies, including files added manually (specified by YAML config file) or using Carthage or CocoaPods.
- [dpkg-licenses](https://github.com/daald/dpkg-licenses) - A command line tool which lists the licenses of all installed packages in a Debian-based system (like Ubuntu).
- [FOSSID](https://fossid.com) - A comprehensive commercial scanner for licenses and vulnerabilities.  Knowledgebase covers 78M+ repositories and 600B+ snippets. Includes detailed snippet scanning to detect the license on fragments and copied/pasted code, even if the open source license is not explicitly or correctly declared.
- [DependencyTrack](https://github.com/DependencyTrack/dependency-track) - An intelligent component analysis platform that allows organizations to identify and reduce risk in the software supply chain.
- [ScanOSS](https://www.scanoss.com/) - Scan your codebase for snippets and plagerism from large knowledge base of open source projects.  Designed to integrate with CI/CD and modern IDEs, to "start left" to do continuous validation instead of one report at the end.  Product itself is fully open source.
- [TLDRLegal](https://www.tldrlegal.com/) - Summarizes the most common open source licenses in plain English. Provides a quick reference for what a user can, cannot, and must do according to the license terms.
- [Choose A License](https://choosealicense.com/) - Recommends an open source license based on the collaboration style and intended use of a project. The site's appendix provides a helpful birds-eye view of terms across the most common licenses.
- [ClearlyDefined](https://clearlydefined.io/) - An open source project and a free service that provides a cached copy of licensing metadata for software components through a simple [API](https://api.clearlydefined.io/api-docs/). Organizations are be able to contribute back any missing or wrongly identified licensing metadata, helping to create a global database that is accurate for the benefit of all, improving compliance and security across the whole software supply chain.

## Localization and Internationalization

Tools for managing translations and i18n.

- [zanata](https://github.com/zanata/zanata-platform) - Web-based system for translators to translate documentation and software online using a web browser.
- [Weblate](https://weblate.org/) - Web-based translation management system.
- [Respresso](https://respresso.io/localization-converter/) - Multiplatform localization converter for iOS (.strings + Objective-C getters), Android (strings.xml) and Web (.json).

## Websites and Documentation

Tools for creating and managing project websites and documentation.

- [Docusaurus](https://docusaurus.io) - React-based static site generator, specifically developed to more easily help create and maintain open source websites.
- [GatsbyJS](https://www.gatsbyjs.com/) - Site generator that allows you to build fast websites and apps with React.
- [VuePress](https://vuepress.vuejs.org/) - Vue-based static site generator, optimized for writing technical documentation.
- [GitBook](https://www.gitbook.com/) - A modern documentation platform where teams can document everything from products, to APIs and internal knowledge bases.
- [MkDocs](https://www.mkdocs.org/) - A fast, simple and downright gorgeous static site generator that's geared towards building project documentation.
- [Hugo](https://gohugo.io/) - The world's fastest framework for building websites, popular for documentation sites.
- [Jekyll](https://jekyllrb.com/) - A simple, blog-aware, static site generator perfect for personal, project, or organization sites.
- [Sphinx](https://www.sphinx-doc.org/) - A tool that makes it easy to create intelligent and beautiful documentation for Python projects.
- [Gitiles](https://gerrit.googlesource.com/gitiles/) - A simple repository browser for Git repositories, written in Java.

## Security

Security scanning and vulnerability management tools.

- [Eclipse Steady](https://github.com/eclipse/steady) - Helps to discover, assess and mitigate known vulnerabilities in Java and Python projects. Formerly known as "Vulnerability Assessement Tool" (Vulas).
- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/) - OWASP dependency-check is a Software Composition Analysis (SCA) tool that attempts to detect publicly disclosed vulnerabilities contained within a project's dependencies.
- [Bandit](https://github.com/PyCQA/bandit) - A tool designed to find common security issues in Python code.
- [Semgrep](https://semgrep.dev/) - A fast, open-source, static analysis tool for finding bugs, security issues, and anti-patterns in code.
- [CodeQL](https://securitylab.github.com/tools/codeql/) - GitHub's semantic code analysis engine for finding security vulnerabilities.
- [Trivy](https://github.com/aquasecurity/trivy) - A comprehensive security scanner for vulnerabilities in container images, file systems, and Git repositories.
- [Gitleaks](https://github.com/zricethezav/gitleaks) - A tool for detecting and preventing secrets in Git repos.

## In-Kind Donations

Resources for in-kind donations and support programs.

The following organizations have formal or informal programs for offering in-kind donations to free and open source projects or foundations.

- [AWS](https://aws.amazon.com/opensource/) - A program started in 2019 to provide promotional credits to open source projects. Details are in [this blog post](https://aws.amazon.com/blogs/opensource/aws-promotional-credits-open-source-projects/) (Last Updated: April 14, 2021)
- [Azure Credits](https://opensource.microsoft.com/azure-credits/) - This program grants Azure credits to open source projects, which developers can use for testing, storage, or other development.
- [Google Cloud Credits](https://cloud.google.com/developers/startups) - Google for Startups Cloud Program provides cloud credits and other benefits for qualifying startups and open source projects.
- [GitHub Sponsors](https://github.com/sponsors) - A way to support the open source maintainers and projects you depend on.
- [Open Collective](https://opencollective.com/) - A legal and financial toolbox for grassroots groups to collect and spend money transparently.
- [JetBrains Open Source Licenses](https://www.jetbrains.com/community/opensource/) - Free licenses for all JetBrains developer tools for qualifying open source projects.

## OSPO Resources

- [TODO Group](https://todogroup.org/) - The TODO Group is an open group of companies who want to collaborate on practices, tools, and other ways to run successful and effective Open Source Program Offices.
- [OSPO 101](https://github.com/todogroup/ospo101) - A course on open source program offices for developers who want to make the most out of open source in their organization.
- [OSPO Mind Map](https://github.com/todogroup/ospology/tree/main/ospo-mindmap) - A mind map of the Open Source Program Office (OSPO) responsibilities, organized by the OSPO responsibilities.
- [OSPO Survey](https://www.linuxfoundation.org/research/) - Annual survey by The Linux Foundation on the state of open source program offices.
- [InnerSource Commons](https://innersourcecommons.org/) - A growing community of practitioners with the goal of creating and sharing knowledge about InnerSource.

## Content License

[![License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by-sa.svg)](https://creativecommons.org/licenses/by-sa/4.0/) © Contributors 2016-2021
