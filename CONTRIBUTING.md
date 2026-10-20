# Contributing to CampusHub

## 1. Before Starting

- Check the relevant GitHub Issue.
- Understand the task and its acceptance criteria.
- Avoid duplicating work already assigned to another contributor.
- Ask the team if anything is unclear.

## 2. Branch Naming

Create a separate branch for each task.

Use these naming conventions:

- feature/short-description
- fix/short-description
- docs/short-description
- chore/short-description
- test/short-description

Examples:

- feature/assignment-tracker
- fix/login-validation
- docs/contribution-guide
- chore/setup-gitignore
- test/assignment-workflow

Use lowercase letters and hyphens in branch names.

## 3. Commit Messages

Write clear, meaningful commit messages.

Examples:

- feat: add assignment tracker
- fix: handle invalid login input
- docs: add contribution guide
- chore: update gitignore
- test: add assignment tests

Keep commits focused on related changes.

## 4. Pull Request Workflow

1. Update your local main branch.
2. Create a branch for your task.
3. Make the required changes.
4. Run the relevant checks.
5. Commit your changes.
6. Push your branch to GitHub.
7. Open a pull request targeting main.
8. Link the related GitHub Issue.
9. Request a review from a teammate.
10. Address review feedback.
11. Merge only after the required approvals and checks pass.

## 5. Issue Linking

Every pull request should reference its related GitHub Issue.

Example:

Closes #7

Use the actual issue number associated with your task.

## 6. Review Expectations

Reviewers should check:

- Whether the changes meet the issue requirements.
- Whether the changes introduce errors.
- Whether relevant tests and checks pass.
- Whether documentation is updated when necessary.
- Whether secrets or unnecessary generated files are included.

## 7. Security

- Never commit passwords, API keys, or secret credentials.
- Keep local environment files out of Git.
- Do not expose private credentials in code or pull requests.
- Report accidentally exposed secrets to the team immediately.

## 8. Before Merging

Confirm that:

- The pull request has been reviewed.
- Required automated checks pass.
- Conflicts have been resolved.
- The changes satisfy the issue's acceptance criteria.

Follow the repository's branch protection settings and team review requirements.
