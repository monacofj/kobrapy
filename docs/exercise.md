Programming Exercise
====================

The goal of this exercise is to gain hands-on experience with the tools,
practices, and workflows of open-source software development.

KobraPy provides a starter codebase with known bugs, feature requests, and
suggested improvements. These offer opportunities to practice version control,
issue tracking, collaborative development, and release management.

Getting Started
---------------

**Create your own project.** The exercise is not about contributing to KobraPy
itself, but about developing a new project based on it.

Your instructor may provide specific setup instructions. Otherwise, create a
new repository and copy the KobraPy codebase into it. Do not fork KobraPy on
GitHub for this exercise: forks are appropriate when contributing back to the
original project.

**Choose a name.** Every programmer knows the responsibility involved in
naming a project. Choose wisely.

Attribution and Licensing
-------------------------

Your project is a derivative work of KobraPy and must respect its copyright
and licensing terms.

For this exercise, adopt the following conventions:

- Preserve original copyright notices in reused files, adding attribution
  for new contributions.
- Attribute new files to your development team, using a collective copyright
  notice.
- Use SPDX identifiers [1] for copyright and license information.
- Choose a license consistent with KobraPy's licensing terms. When in doubt,
  use the same license as KobraPy.

Documentation
-------------

Your documentation should describe **your own project**, not KobraPy. Review
and update the relevant files:

- `README.md`
- `AUTHORS`
- `docs/manual.md`
- `docs/CONTRIBUTING.md`

Make sure your contribution guidelines reflect the practices and workflows
adopted by your team.

Development Workflow
--------------------

Review the required bugs and suggested features in
[`docs/issues.md`](issues.md). Address the required bugs and select additional
improvements, or propose your own.

For each planned change:

1. Create an issue in your repository.
2. Develop the change in a dedicated branch.
3. Submit a pull request.
4. Review and discuss changes before merging.

Follow your project's contribution guidelines throughout the process.

Release Planning
----------------

Organize your work using GitHub milestones:

- **1.0.0-alpha:** Initial release for feedback.
- **1.0.0-beta:** Feature freeze and stabilization.
- **1.0.0:** Stable release.

Beyond the Exercise
-------------------

The purpose is not merely to produce a working game, but to experience how
open-source projects are organized and sustained.

Reflect critically on the practices you adopt, their advantages and
limitations, and how they can support long-term maintainability, newcomer
onboarding, and contributor retention.

*Press any key to start.*

References
----------

[1] SPDX — Software Package Data Exchange. https://spdx.dev
