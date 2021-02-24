# Contributing to nari

**First:** if you're unsure or afraid of *anything*, please ask in our Discord server's #nari channel.

Please attach a GitHub Issue to all feature PRs when possible to provide context and discussion for other developers
that are reviewing the PR. While we're generally fine with reviewing code, we cannot guess why a feature is useful
every time. Similarly, bug fix PRs should be based on a bug report issue so we have context on what the specific
problem is.


## Table of Contents

- [I have a Question](#i-have-a-question)
- [I have a Feature Idea](#i-have-a-feature-idea)
- [New Issue](#new-issue)
- [New Pull Request](#new-pull-request)
- [Licensing](#licensing)


## I just have a Question

Please ask in our Discord or the Discussions tab in GitHub. The #nari channel can be used for discussion, support, etc
however we can't teach you how to program either in general or Python specifically. If someone volunteers to help you,
that's up to them. We can answer user questions here however keep in mind that issues around FFXIV data structures
might be better asked in other community servers with more knowledge on the topic.


## I have a Feature Idea

Awesome, thanks for thinking of us! If it's something you're unsure of, please ask in our Discord. If it turns out
pretty solid and you want some user feedback, the Discussions tab on the repo is a great place to get feedback from
other users before we create a project or issue. We think community discussion is important and the Discussions page
is a lot easier to read than a Discord conversation that can get buried in a busy chat log.


## New Issue

We welcome all bug reports and feature development issues. A user problem doesn't always mean a bug though, so please
get some help troubleshooting in our Discord before reporting a bug. For features, we recommend discussing in the
Discussion tab on the repo first, so that feature ideas are in a place the community can easily read, and development
or implementation details are in the issue. This helps contributors avoid reading feature opinions and focus on the
technical details of the implementation.

Please follow the Issue Template that comes up when you submit an issue, as it helps us a lot knowing all the required
details are neatly summarised from the start.

### General Issue Guidelines

- Please use the search and see if there's a duplicate issue before posting. If something has been closed, it's
probably for a reason.

- For feature requests, **include a use case**. This makes it infinitely easier for us to understand what you're trying
 to achieve with the feature.

- For bug reports, **include steps to reproduce the bug**. We can't discuss or address a bug we can't trigger.


## New Pull Request

Thank you for contributing! We're happy to read almost any pull request but it helps us a lot if it's attached to an
issue to provide context. The PR description should summarise the change but the issue context helps us a lot to see
the use case and implementation details at a high level.

### Cosmetic Changes

While we love features and bug fixes, cosmetic changes provide little value and are a time sync to review. They're
generally used for padding contributions instead of improving code. As such, we will not accept cosmetic PRs. It's fine
to fix these issues inside other PRs that touch the same code however.

The following are considered cosmetic changes:

- Comments and Documentation
- Grammar
- Typos
- Code Formatting (potentially excluding whitespace, due to Python's inherent use of it)
- README updates


## Licensing

nari uses the MIT licence. The copyright is attributed to "xivlogs" as an org rather than maintaining every individual
contributor, however if you feel the need to get explicit copyright, please discuss with one of the maintainers in
Discord.
