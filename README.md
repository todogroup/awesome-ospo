# Awesome OSS Management [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

This list identifies packages and projects that have been built by TODO Group
members or found helpful for managing open source projects and offices.

## Contents
* [Code Reviews](#code-reviews)
* [Continuous Integration / Continuous Delivery](#continuous-integration--continuous-delivery)
* [Contributor License Agreements / Developer Certificate of Origins](#contributor-license-agreements--developer-certificate-of-originis)
* [GitHub Metrics and Dashboards](#github-metrics-and-dashboards)
* [GitHub Management](#github-management)
* [Project Quality](#project-quality)
* [Supply Chain Trust](#supply-chain-trust)
* [Licensing](#licensing)
* [Localization and Internationalization](#localization-and-internationalization)
* [Websites and Documentation](#websites-and-documentation)
* [Security](#security)
* [In-Kind Donations](#in-kind-donations)
* [Content License](#content-license)

## Code Reviews

- [mention-bot](https://github.com/facebookarchive/mention-bot) - The mention bot will automatically mention potential reviewers on pull requests. It helps getting faster turnaround on pull requests by involving the right people early on.
- [PullApprove](https://www.pullapprove.com) - Allows for fancier rules on how pull requests are approved.
- [sentinel](https://github.com/habitat-sh/sentinel) - PR Test, review, and merge workflow bot
- [pull-review](https://github.com/imsky/pull-review) - assign pull request reviewers intelligently, inspired by mention-bot
- [pull-request-size](https://github.com/noqcks/pull-request-size) - Automatically adds GitHub labels based on the size of a Pull Request.
- [Pullie](https://github.com/godaddy/pullie) - GitHub App that helps with PRs: requests reviews, links Jira tickets, nags for missing required file changes (e.g. changelog entries)

## Continuous Integration / Continuous Delivery 

- [GitHub Actions](https://github.com/features/actions) - Automate your workflow from idea to production.
- [Jenkins](https://www.jenkins.io/) - open source automation server that provides hundreds of plugins to support building, deploying and automating any project.
- [Jenkins X](https://jenkins-x.io/) - open source CI/CD solution for modern cloud applications on Kubernetes.
- [Ortelius](https://ortelius.io/) - providing a central catalog of services with their deployment specs, application teams can easily consume and deploy services across cluster.
- [Screwdriver](https://screwdriver.cd/) -  Screwdriver is an open source build platform designed for Continuous Delivery.
- [Spinnaker](https://spinnaker.io/) - multi-cloud continuous delivery platform for releasing software changes with high velocity and confidence
- [Tekton](https://tekton.dev/) - set of shared, open source components for building CI/CD systems
- [Travis CI](https://travis-ci.org/) - A hosted continuous integration service used to build and test software projects hosted at GitHub and Bitbucket

## Contributor License Agreements / Developer Certificate of Origins

- [CLA Assistant](https://github.com/cla-assistant/cla-assistant) - Streamline your workflow and let CLA assistant handle the legal side of contributions to a repository for you. CLA assistant enables contributors to sign CLAs from within a pull request.
- [DCOB](https://github.com/chef/dcob) - A bot for enforcing developer certificate of origin sign-offs for each commit in a PR
- [CLA Portal](https://github.com/vmware/claportal) - Enables a workflow for contributors to sign a CLA for pull requests to your GitHub repositories. Also supports DCO sign-offs in the commits.
- [OSS Contribution Tracker](https://github.com/amzn/oss-contribution-tracker) - Track contributions made to external projects and manage CLAs
- [Dr CLA](https://github.com/salesforce/dr-cla) - GitHub bot for dealing with Contributor License Agreements
- [DCO Bot](https://github.com/probot/dco) - GitHub App that enforces the Developer Certificate of Origin (DCO) on Pull Requests

## GitHub Metrics and Dashboards

- [oss-dashboard](https://github.com/amzn/oss-dashboard) - A dashboard for viewing many GitHub organizations, and/or users, at once.
- [osstracker](https://github.com/Netflix/osstracker) - OSS Tracker is an application that collects information about a Github organization and aggregates the data across all projects within that organization into a single user interface to be used by various roles within the owning organization.
- [ghcrawler](https://github.com/microsoft/ghcrawler) - GHCrawler is a GitHub API crawler that crawls a GitHub-hosted project and automatically tracks, retrieves, and stores its contents. GHCrawler is primarily intended for people trying to track sets of organizations and data repositories.
- [devstats](https://github.com/cncf/devstats) - A toolset to visualize GitHub archives using Grafana dashboards used by the Cloud Native Computing Foundation and Kubernetes
- [MeasureOSS](https://github.com/MeasureOSS/Measure) - A contributor relationship management system
- [GrimoireLab](https://chaoss.github.io/grimoirelab/) - Software development analytics platform supporting more than 30 different data sources, part of CHAOSS Software project from The Linux Foundation
- [Starfish](https://github.com/indeedeng/starfish) - A tool to identify GitHub contributions within a specified window of time. 
- [Project Portal](https://github.com/SAP/project-portal-for-innersource) - Lists all InnerSource (or Open Source) projects of a company in an interactive and easy to use way. Can be used as a template for implementing the "InnerSource portal" pattern by the InnerSource Commons community. 

## GitHub Management

- [opensource-portal](https://github.com/Microsoft/opensource-portal) - Microsoft's Open Source Portal for GitHub is a tool to help large organizations with GitHub management operations, onboarding and more. It is implemented in Node.js.
- [hubcommander](https://github.com/Netflix/hubcommander) - A Slack bot for GitHub organization management
- [GitHub Settings](https://github.com/probot/settings) - uses .github/config.yml as the source of truth, and any changes to that file in the default branch will update GitHub
- [Zappr](https://github.com/zalando/zappr) - An agent that enforces guidelines for your GitHub repositories (from code reviews to necessary files)
- [FBShipIt](https://github.com/facebook/fbshipit) - A library written in Hack for copying commits from one repository to another.'
- [Copybara](https://github.com/google/copybara) - A tool for transforming and moving code between repositories.
- [github org scripts](https://github.com/mozilla/github-org-scripts) - Some helper scripts to manage github orgs via API.
- [github-org-mgmt scripts](https://github.com/bertvv/github-org-mgmt) - A few scripts for managing a Github organization
- [Automated Github Organization Invites](https://github.com/thundergolfer/automated-github-organization-invites) - Host a webpage allow people to click and receive and invite to your Github Organization
- [Pepper](https://github.com/genuinetools/pepper) - A tool for performing actions on GitHub repos or a single repo. 
- [Grit](https://github.com/grailbio/grit) - Grit is a tool to mirror monorepo subtrees to Github
- [Sheriff](https://github.com/electron/sheriff) - Controls and monitors organization permissions across GitHub, Slack and GSuite
- [Mariner Issue Collector](https://github.com/indeedeng/Mariner-Issue-Collector) - Identify open issues across all of your dependencies
- [Steampipe GitHub Plugin](https://hub.steampipe.io/plugins/turbot/github) - Query GitHub Repositories, Organizations, and other resources with SQL.
- [Steampipe GitHub Sherlock](https://hub.steampipe.io/mods/turbot/github_sherlock) - Interrogate your GitHub resource configurations to identify improvements based on best practices.
- [(Corporate) Git Proxy](https://github.com/finos/git-proxy) - Scan outgoing attempts to push to public repository and raise compliance/info-sec friendly checks before allowing the push to complete.

## Governance

- [Minimal Viable Governance](https://github.com/github/MVG) - Currently in beta - is a repository-based approach for putting lightweight governance into free and open source projects that are run in version control systems. It provides an overall two-tier organizational governance structure for a set of free and open source projects.

## Project Quality

- [CII Best Practices Badging](https://bestpractices.coreinfrastructure.org/) - The Core Infrastructure Initiative (CII) Best Practices badge is a way for Free/Libre and Open Source Software (FLOSS) projects to show that they follow best practices. Projects can voluntarily self-certify, at no cost, by using this web application to explain how they follow each best practice.
- [Fosstars](https://github.com/SAP/fosstars-rating-core) - A framework for defining and calculating ratings for open source projects
- [RepoLinter](https://github.com/todogroup/repolinter) - Lint open source repositories for common issues.
  - [RepoLinter Dashboard](https://github.com/todogroup/repolinter-dashboard) - A Dashboard for RepoLinter
- [Linguist](https://github.com/github/linguist) - Identify the programming languages used in a project.
- [repo-scaffolding](https://github.com/twitter/repo-scaffolding) - Scaffolding tools for creating and maintaining projects based on Twitter Open Source standards and best practices.
- [Repo Health Check](https://github.com/dogweather/repo-health-check) - Analyze a project: How are the maintainers doing?

## Supply Chain Trust

- [OpenChain Conformance](https://certification.openchainproject.org) - The OpenChain Specification is a way for companies using Free/Libre and Open Source Software (FLOSS) to show that they meet the key requirements for quality compliance programs. Companies can voluntarily self-certify, at no cost, by using this web application.

## Licensing

- [SPDX](https://spdx.org) - Set of standards for communicating the components, licenses and copyright associated with a software package.
- [LicenseFinder](https://github.com/pivotal-legacy/LicenseFinder) - Find licenses for your project's dependencies
- [ScanCode toolkit](https://github.com/nexB/scancode-toolkit) - Scan code for licenses, copyright and dependencies
- [FOSSology](https://www.fossology.org) - Scan code for license, copyright and export control information
- [Licensee](https://github.com/benbalter/licensee) - Identify a project's license file
- [License Identifier (LiD)](https://github.com/codeauroraforum/lid) - Identify and extract license text from source code
- [askalono](https://github.com/amzn/askalono) - a library and command-line tool to help detect license texts. It's designed to be fast, accurate, and to support a wide variety of license texts.
- [License Classifier](https://github.com/google/licenseclassifier) - A library and set of tools that can analyze text to determine what type of license it contains
- [OSS Attribution Builder](https://github.com/amzn/oss-attribution-builder) - The OSS Attribution Builder is a website that helps teams create attribution documents (notices, "open source screens", credits, etc) commonly found in software products.
- [OSS Review Toolkit](https://github.com/heremaps/oss-review-toolkit) - enables highly automated and customizable Open Source compliance checks od the source code and dependencies of a project by scanning it, downloading its sources, reporting any errors and violations against user-defined rules, and by creating third-party attribution documentation.
- [fossa-cli](https://github.com/fossas/fossa-cli) - Fast, portable and reliable dependency analysis for any codebase
- [Licensed](https://github.com/github/licensed) - A Ruby gem to cache and verify the licenses of dependencies
- [LicensePlist](https://github.com/mono0926/LicensePlist) - A command-line tool that automatically generates a Plist of all your dependencies, including files added manually(specified by YAML config file) or using Carthage or CocoaPods.
- [dpkg-licenses](https://github.com/daald/dpkg-licenses) - A command line tool which lists the licenses of all installed packages in a Debian-based system (like Ubuntu).
- [FOSSID](https://fossid.com) - A comprehensive commercial scanner for licenses and vulnerabilities.  Knowledgebase covers 78M+ repositories and 600B+ snippets. Includes detailed snippet scanning to detect the license on fragments and copied/pasted code, even if the open source license is not explicitly or correctly declared.
- [DependencyTrack](https://github.com/DependencyTrack/dependency-track) - Dependency-Track is an intelligent Component Analysis platform that allows organizations to identify and reduce risk in the software supply chain
- [ScanOSS](https://www.scanoss.com/) - Scan your codebase for snippets and plagerism from large knowledge base of open source projects.  Designed to integrate with CI/CD and modern IDEs, to "start left" to do continuous validation instead of one report at the end.  Product itself is fully open source.  
- [TLDRLegal](https://tldrlegal.com/) - TLDRLegal summarizes the most common open source licenses in plain English. Provides a quick reference for what a user can, cannot, and must do according to the license terms. 

## Localization and Internationalization

- [zanata](https://github.com/zanata/zanata-platform) - Zanata is a web-based system for translators to translate documentation and software online using a web browser.
- [Weblate](https://weblate.org/) - Weblate is a free web-based translation management system.
- [Respresso](https://respresso.io/localization-converter) - Multiplatform localization converter for iOS (.strings + Objective-C getters), Android (strings.xml) and Web (.json).

## Websites and Documentation

- [Docusaurus](https://docusaurus.io) - Docusaurus is a React-based static site generator, specifically developed to more easily help create and maintain open source websites.
- [GatsbyJS](https://www.gatsbyjs.org/) - Gatsby is a site generator that allows you to build fast websites and apps with React.
- [VuePress](https://vuepress.vuejs.org/) - VuePress is a minimalistic Vue-based static site generator, optimized for writing technical documentation.

## Security

- [Eclipse Steady](https://github.com/eclipse/steady) - Eclipse Steady, formerly known as "Vulnerability Assessement Tool" (Vulas), helps to discover, assess and mitigate known vulnerabilities in Java and Python projects.
- [Lift](https://www.sonatype.com/products/sonatype-lift) — Sonatype Lift is a free forever, cloud-native and collaborative code analysis platform built for developers. It analyzes each developer pull request to find and fix security, performance, reliability, and style issues, then reports them as comments in code review — where they are 70x more likely to get fixed.

## In-Kind Donations
The following organizations have formal or informal programs for offering in-kind donations to free and open source projects or foundations. 
- [AWS](https://aws.amazon.com/opensource/) - AWS started a program in 2019 to provide promotional credits to open source projects. Details are in [this blog post](https://aws.amazon.com/blogs/opensource/aws-promotional-credits-open-source-projects/) and you can [Apply Here](https://pages.awscloud.com/AWS-Credits-for-Open-Source-Projects) (Last Updated: April 14, 2021)
- [Indeed](https://opensource.indeed.com) - If you work in a charitable organization that serves the free and open source software communities, and you are trying to hire for your organization, Indeed's Open Source Program Office may be able to provide promotional credits for to advertise your job posting on Indeed.com. Email opensource@indeed.com for details. (Last updated: April 14, 2021)
- [Azure Credits](https://cloudblogs.microsoft.com/opensource/2021/09/28/announcing-azure-credits-for-open-source-projects/) - This program grants Azure credits to open source projects for a year. Developers will be able to use these credits for testing, storage, or other development.

# Content License

[![License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by-sa.svg)](https://creativecommons.org/licenses/by-sa/4.0/) © Contributors 2016-2021
