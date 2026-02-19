# Chapter 2 - Module 0: Pull Requests Fundamentals

**Duration:** 40 minutes | **Difficulty:** Intermediate

---

## Learning Objectives

By the end of this module, you will be able to:

1. Understand what pull requests are
2. Create a pull request on GitHub
3. Write clear PR titles and descriptions
4. Link issues to pull requests
5. Understand the PR review process
6. Handle PR feedback

---

## What is a Pull Request?

A **pull request (PR)** is a proposal to merge code changes from one branch into another.

```
Before PR:
main:     A → B → C
             └─ feature-login: D → E

Create PR:
Asking: "Can I merge feature-login into main?"
Review: Team examines changes D and E

After Approval & Merge:
main:     A → B → C → F (merge commit)
             └─ D → E ↗
```

### Why Pull Requests?

✅ **Code Review** - Team evaluates changes before merging
✅ **Quality Gate** - Catch bugs early
✅ **Documentation** - PR description explains why
✅ **Discussion** - Team talks about the code
✅ **Accountability** - Clear who approved what
✅ **CI/CD Integration** - Automated testing

---

## Components of a Pull Request

### 1. Title

Clear, concise description of changes:

```
Good PR titles:
✅ Add user authentication
✅ Fix login button styling
✅ Update documentation for API

Bad PR titles:
❌ Fix stuff
❌ WIP
❌ asdfgh
```

### 2. Description

Explains what changed and why:

```markdown
## Description
Adds user authentication system using JWT tokens.

## Changes
- Created auth.py module
- Added login endpoint
- Implemented token validation
- Updated requirements.txt

## Why?
Addresses issue #42: Users need secure login

## Testing
- Unit tests added in test_auth.py
- Tested with 3 different login scenarios
- No breaking changes to existing APIs

## Screenshots (if applicable)
[Screenshot of login form]
```

### 3. Files Changed Tab

Shows all modified files and changes:

```
3 files changed, 150 additions(+), 20 deletions(-)

auth.py (new)           +120 additions
routes.py               +30 additions, -20 deletions
requirements.txt        +1 additions
```

### 4. Commits Tab

Shows individual commits in the PR:

```
- Add JWT token generation (commit a1b2c3d)
- Add login endpoint (commit e4f5g6h)
- Update requirements.txt (commit i7j8k9l)
```

### 5. Checks Tab

Shows automated tests and checks:

```
✅ All tests passed
✅ Code coverage maintained
❌ Linting failed (fix requested)
```

### 6. Conversation Tab

Comments, reviews, and discussion:

```
Reviewer: "Lines 45-50 could be simplified"
Author: "Good point, I'll refactor that"
```

---

## Creating a Pull Request

### Step 1: Ensure You Have a Feature Branch

On GitHub, a PR connects two branches:

```bash
# You should be on a branch (not main)
git switch feature-login
```

### Step 2: Push Your Branch

```bash
git push -u origin feature-login
```

### Step 3: Create PR on GitHub

1. Visit your repository on GitHub
2. You should see a yellow banner about your pushed branch
3. Click "Compare & pull request"
4. Or: Click "Pull requests" tab → "New pull request"

### Step 4: Select Branches

- **Base:** Where you want to merge (usually `main`)
- **Compare:** Your feature branch (`feature-login`)

### Step 5: Fill in Details

**Title:** [Clear description of changes]

**Description:** [Template below]

```markdown
## Description
[What does this PR do?]

## Changes
- [Change 1]
- [Change 2]
- [Change 3]

## Why?
Fixes #[issue number] or describes reason

## Testing
[How was this tested?]

## Checklist
- [ ] Code reviewed by myself
- [ ] Tests written/updated
- [ ] Documentation updated
- [ ] No breaking changes
```

### Step 6: Review & Create

Check "Files changed" tab to verify:
- Only intended files modified
- No accidental changes
- No secrets committed

Click "Create pull request"

---

## PR Statuses

### Draft PR

For work-in-progress, not ready to merge:

```bash
# Convert to draft when creating
# Or click "Convert to draft" while PR is open
```

Benefits:
- Signal: "Not ready for review yet"
- Explore ideas before finishing
- Get early feedback

### Ready for Review

Mark as ready:
```
Click "Ready for review" button
```

---

## Linking Issues to PRs

### Automatic Linking

In PR description, mention issues:

```markdown
Fixes #42
Closes #43
References #44
```

Keywords that auto-close:
- `close`, `closes`, `closed`
- `fix`, `fixes`, `fixed`
- `resolve`, `resolves`, `resolved`

When PR merges, linked issues automatically close!

### Manual Linking

On PR page:
1. Click "Development" on right sidebar
2. Click link icon
3. Search for issue
4. Select from list

---

## Review Process Workflow

```
1. Developer creates PR with description
   ↓
2. Automated checks run (tests, linting)
   ↓
3. Reviewers notified
   ↓
4. Reviewers examine code and leave comments
   ↓
5. Developer addresses feedback
   ↓
6. Conversation continues until consensus
   ↓
7. Reviewers approve
   ↓
8. PR merged (usually by developer or lead)
   ↓
9. Branch deleted
   ↓
10. Cycle repeats
```

---

## PR Best Practices

### Make PRs Small and Focused

❌ Bad: 500+ lines changing 10 different things
✅ Good: 50-200 lines, single feature

### Write Clear Descriptions

❌ Bad: "Update code"
✅ Good: "Add email validation to signup form - validates format and checks for existing emails"

### Include Tests

❌ Bad: "I tested it manually"
✅ Good: "Added 8 unit tests covering edge cases"

### Keep PRs Up to Date

```bash
# If main has new commits
git switch main
git pull

git switch feature-login
git merge main
# or
git rebase main

git push
```

### Reference Issues

```
Resolves #123
```

Helps track why changes were made.

---

## Exercises

### Exercise 1: Create Your First Pull Request

**Objective:** Create a PR with good descriptions

**Prerequisites:** 
- Feature branch pushed to GitHub
- GitHub repository set up

**Instructions:**

1. **Ensure you have unpushed changes**
   ```bash
   # On your feature branch
   git switch feature-new-feature
   
   # Make a change if needed
   echo "New content" >> feature.txt
   git add feature.txt
   git commit -m "Update feature content"
   git push
   ```

2. **Go to GitHub**
   - Visit your repository
   - Should see notification about your branch
   - Click "Compare & pull request"

3. **Fill in PR Details**
   
   **Title:**
   ```
   Add new feature to project
   ```
   
   **Description:**
   ```markdown
   ## Description
   This PR adds a new feature that improves the project.
   
   ## Changes
   - Added feature.txt with new content
   - Updated existing files (if any)
   
   ## Why?
   This feature addresses user requests for improved functionality.
   
   ## Testing
   - Tested locally with various inputs
   - Verified no breaking changes
   - All existing tests still pass
   
   ## Checklist
   - [x] Code reviewed
   - [x] Tests verified
   - [ ] Documentation updated (not applicable for this feature)
   ```

4. **Review Files Changed**
   - Should show your modified/new files
   - Verify nothing unintended is included

5. **Create Pull Request**
   - Click "Create pull request" button
   - Save the URL of your PR

**Verification Checklist:**
- [ ] PR created successfully
- [ ] Title is clear and descriptive
- [ ] Description explains the changes
- [ ] Files changed are correct
- [ ] PR is visible on repository

---

### Exercise 2: Link an Issue to a PR

**Objective:** Connect a PR to an issue

**Prerequisites:** Existing PR from Exercise 1

**Instructions:**

1. **Create an issue** (if you don't have one)
   - Go to Issues tab on GitHub
   - Click "New issue"
   - Title: "Implement new feature"
   - Description: "This is a test issue"
   - Click "Create issue"
   - Note the issue number (e.g., #5)

2. **Update PR description**
   - Go to your PR from Exercise 1
   - Click "Edit" button on description
   - Add line:
     ```
     Fixes #[your-issue-number]
     ```
   - Save

3. **Verify linking**
   - Refresh the page
   - Look for "Development" section on right
   - Should show linked issue
   - Click on issue number
   - Go back to issue
   - Issue should show linked PR

**Example:**
If issue is #5:
```markdown
Fixes #5
```

**Verification Checklist:**
- [ ] Issue created
- [ ] PR description includes "Fixes #X"
- [ ] Issue shows linked PR
- [ ] PR shows linked issue

---

### Exercise 3: Review Your Own PR (Self-Review)

**Objective:** Practice reviewing your own code

**Instructions:**

1. **Go to your PR**
   - Click your PR number

2. **Review each change**
   - Click "Files changed" tab
   - Examine each file modification
   - Ask yourself:
     - Is code quality good?
     - Are variable names clear?
     - Is documentation complete?
     - Are there any obvious bugs?

3. **Leave a comment on yourself**
   - Click "+" on a line number
   - Add a comment:
     ```
     Good: This change is clear and well-structured.
     Suggestion: Consider adding error handling here.
     ```
   - Click "Comment"

4. **Respond to your own comment**
   - Reply with a suggestion or acknowledgment
   - Example:
     ```
     Good catch! I've ensured error handling is implemented.
     ```

**Verification Checklist:**
- [ ] Self-review completed
- [ ] Left constructive comments
- [ ] Responded to comments
- [ ] Understand the code review process

---

## Command Reference

| Command | Purpose |
|---------|---------|
| `git push -u origin branch-name` | Push branch to create PR base |
| `git pull` | Get latest main before PR |
| `git merge main` | Update PR with latest main |

---

## PR Templates

Some teams use templates. Check repository for:
- `.github/pull_request_template.md`

---

## Key Takeaways

✅ PRs are proposals for code merges
✅ Clear descriptions are essential
✅ PR must include why changes were made
✅ Linking issues helps track progress
✅ PRs enable code review before merge
✅ Small, focused PRs are better

---

## Common Mistakes

| Mistake | Solution |
|---------|----------|
| Merging to main without review | Always create PR and wait for approval |
| Unclear PR title | Be specific: "Add email validation" not "Fix stuff" |
| Huge PR with 500+ lines | Split into multiple smaller PRs |
| Not updating PR after feedback | Address comments and push new commits |

---

## Next Steps

You've created your first PR! In **Module 1**, you'll learn how to review PRs from other developers.

---

**[← Back to Chapter 2 Overview](./README.md)** | **[Next: Module 1 →](./Module-1-Code-Reviews.md)**
