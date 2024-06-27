# Contributing Guidelines

Contributions are always welcome!

**Before spending lots of time on something, ask for feedback on your idea first!**

Please search issues and pull requests before adding something new to avoid duplicating
efforts and conversations.


To make a code contribution to srt2docx
--------------------------------------

* Fork the srt2docx Github repository and make your changes.  Use a well named topic branch for the changes, preferably with uppercase and dashes, use your initials at the beginning of the branch name e.g. `SD-SRT2DOCX-FIXES`.  Fork off the `master` branch.  Avoid forking from repository work branches as they may get rebased.

* Test your changes as thoroughly as possible, by running the test suite and viewing the coverage reports.

* Please follow the code style for the language you are working in and try to match the general structure of the code.  Check that your diff looks as clean and minimal as possible.

* Create a pull request in Github.  For now, the "base branch" should be
  "master", i.e. the pull requests are merged directly to the master branch.
  In the description:

  - Summarize the change and the motivation for the change.

  To report bugs or request features
----------------------------------

Use GitHub issues to report bugs or request features:

* Please include a compilation or execution log to help diagnosis.


## Installing

Fork and clone the repo, then build and run tests to ensure all is okay before you start anything.


## Testing

Please ensure all tests are passing before submitting a pull request (unless you're creating a failing test to increase test coverage or show a problem).

