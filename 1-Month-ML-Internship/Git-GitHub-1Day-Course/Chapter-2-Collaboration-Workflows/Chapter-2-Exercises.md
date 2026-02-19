# Chapter 2: Collaboration Workflows - Comprehensive Exercises

**Difficulty:** Intermediate-Advanced | **Estimated Time:** 2 hours | **Prerequisites:** Chapters 0-1 completed

---

## Overview

This exercise file consolidates and expands on all exercises from Chapter 2 modules. Complete these exercises to master pull requests, code reviews, and team collaboration workflows.

---

## Exercise 1: Create Your First Pull Request

**Objective:** Understand the complete pull request workflow

**Instructions:**

1. **Prepare Repository on GitHub**
   - Go to your `github-practice` repository
   - Ensure main branch is up to date
   - Create a new branch locally:
   ```bash
   git checkout -b feature/add-features
   ```

2. **Make Changes on Feature Branch**
   ```bash
   echo "## New Features" > features.md
   echo "" >> features.md
   echo "### Feature 1: User Authentication" >> features.md
   echo "- Login functionality" >> features.md
   echo "- Password reset" >> features.md
   echo "" >> features.md
   echo "### Feature 2: User Profiles" >> features.md
   echo "- Profile creation" >> features.md
   echo "- Profile editing" >> features.md
   ```

3. **Commit Your Changes**
   ```bash
   git add features.md
   git commit -m "feat: Add features documentation
   
   - Document user authentication feature
   - Document user profiles feature
   - Include implementation details"
   ```

4. **Push Feature Branch to GitHub**
   ```bash
   git push -u origin feature/add-features
   ```

5. **Create Pull Request on GitHub**
   - Go to your repository
   - Notice the "Compare & pull request" button
   - Click it or go to "Pull requests" tab and click "New pull request"
   - Select:
     - Base branch: `main`
     - Compare branch: `feature/add-features`
   - Fill in PR title: "feat: Add features documentation"
   - Add description:
     ```
     ## Description
     This PR adds documentation for upcoming features.
     
     ## Related Issues
     Relates to planning phase
     
     ## Changes
     - Added features.md file
     - Documented authentication feature
     - Documented user profile feature
     
     ## Type of Change
     - [x] Documentation
     - [ ] Bug fix
     - [ ] New feature
     ```
   - Click "Create pull request"

6. **Review Your Own PR**
   - Look at "Files changed" tab
   - Review diff of changes
   - Look at "Comments" tab

7. **Merge the Pull Request**
   - Scroll down to merge section
   - Click "Merge pull request"
   - Click "Confirm merge"
   - Click "Delete branch" to clean up

8. **Pull Changes Locally**
   ```bash
   git checkout main
   git pull origin main
   ls
   # Should show features.md
   ```

**Verification Checklist:**
- [ ] Feature branch created locally
- [ ] Changes committed with descriptive message
- [ ] Branch pushed to GitHub
- [ ] Pull request created with proper title and description
- [ ] PR files changed tab shows correct diffs
- [ ] PR merged successfully
- [ ] Merged changes visible in main locally

**Key Concepts:**
- Pull requests are the primary collaboration mechanism
- PRs include discussion and review capabilities
- Merging can be done via GitHub interface
- Clean up branches after merging

---

## Exercise 2: Request Code Review

**Objective:** Practice the code review request process

**Instructions:**

1. **Create Feature Branch for Review**
   ```bash
   git checkout -b feature/improve-readme
   ```

2. **Create Changes Worth Reviewing**
   ```bash
   cat > REVIEW_GUIDELINES.md << EOF
   # Code Review Guidelines
   
   ## Reviewer Responsibilities
   - Understand the purpose of changes
   - Check code quality and style
   - Look for potential bugs
   - Verify tests are adequate
   - Suggest improvements
   
   ## Review Checklist
   - [ ] Code follows style guide
   - [ ] No credentials in code
   - [ ] Tests pass locally
   - [ ] Functions are documented
   - [ ] Performance impact considered
   
   ## Approval Levels
   - Approval: Ready to merge
   - Request changes: Needs fixes
   - Comment: General discussion
   EOF
   ```

3. **Create Multiple Commits**
   ```bash
   git add REVIEW_GUIDELINES.md
   git commit -m "docs: Add code review guidelines"
   
   echo "## Performance Tips" >> README.md
   echo "- Use caching for repeated operations" >> README.md
   git add README.md
   git commit -m "docs: Add performance tips to README"
   ```

4. **Push to GitHub**
   ```bash
   git push -u origin feature/improve-readme
   ```

5. **Create Pull Request**
   - Go to "Pull requests" → "New pull request"
   - Select branches appropriately
   - Add detailed description:
     ```
     ## Description
     This PR improves documentation and adds code review guidelines.
     
     ## Motivation
     We need clear guidelines for team code review process.
     
     ## Changes
     - Added REVIEW_GUIDELINES.md with detailed process
     - Enhanced README with performance tips
     
     ## Testing
     - Verified all links work
     - Checked formatting consistency
     ```

6. **Request Reviewers** (if collaborators available)
   - Click "Reviewers" on the right side
   - Select reviewers (you can select yourself for this exercise)
   - Comment: "@username please review for clarity and completeness"

7. **Check PR Status**
   ```bash
   # In terminal, view from main branch
   git log --oneline main
   # Feature branch not yet merged
   ```

**Verification Checklist:**
- [ ] Feature branch with multiple commits created
- [ ] PR created with comprehensive description
- [ ] Reviewer requested (self or otherwise)
- [ ] PR shows all changes in "Files changed" tab
- [ ] Can comment on individual files/lines

**Key Concepts:**
- PRs should have clear, detailed descriptions
- Asking for review is a collaboration mechanism
- Multiple commits before merge show development process
- PR comments enable discussion before merge

---

## Exercise 3: Handle Code Review Feedback

**Objective:** Respond to review comments and update PR

**Instructions:**

1. **Simulate Review Feedback**
   - On your PR, click on a line in "Files changed"
   - Click the comment icon
   - Add a comment suggesting improvement:
     ```
     Is this performance consideration applicable to all use cases?
     Perhaps we should add more details.
     ```

2. **Respond to Feedback in Code**
   ```bash
   git checkout feature/improve-readme
   ```

3. **Update README with More Detail**
   ```bash
   cat >> README.md << EOF
   
   ### Performance Tips Detail
   - Database query caching: Reduces repeated queries by 70%
   - Client-side caching: Improves response time for users
   - CDN usage: Best for static assets and content
   EOF
   ```

4. **Commit the Changes**
   ```bash
   git add README.md
   git commit -m "docs: Add detailed performance tips as per review feedback"
   ```

5. **Push Updated Branch**
   ```bash
   git push origin feature/improve-readme
   ```

6. **Reply to Code Review Comment**
   - Go back to PR
   - Find the comment you made
   - Click "Reply"
   - Write: "Updated README with more details about performance tips and when to apply them."
   - Click "Comment"

7. **View Updated PR**
   - PR now shows the new commit
   - "Files changed" shows incremental changes
   - Conversation shows comment thread

**Verification Checklist:**
- [ ] Left code review comment on your own PR
- [ ] Made changes based on feedback
- [ ] Created new commit with changes
- [ ] Pushed updated branch
- [ ] Replied to review comment
- [ ] PR shows complete conversation history

**Key Concepts:**
- PR workflows include feedback and iteration
- New commits on feature branch automatically update PR
- Conversation history is preserved
- This mimics real team review process

---

## Exercise 4: Perform Code Review on Others' PRs

**Objective:** Learn how to review code professionally

**Instructions:**

1. **Find a PR to Review**
   - For this exercise, create a second repository
   - Have it with an open PR, or review your own again
   - OR find an open-source project with PRs:
     - https://github.com/good-first-issue
     - https://github.com/firstcontributions

2. **Review the PR**
   - Click "Files changed" tab
   - Examine all changes carefully

3. **Leave Line-by-Line Comments**
   - Click on lines that need comments
   - Suggest improvements:
     ```
     This could be more efficient with a set instead of a list.
     ```
     ```
     Good error handling here! Consider also validating input types.
     ```

4. **Leave a General Review Comment**
   - Scroll to bottom
   - Click "Review changes"
   - Select "Comment" (just reviewing)
   - Write overall feedback:
     ```
     Good implementation overall. A few suggestions:
     
     1. Consider performance implications
     2. Update tests to cover edge cases
     3. Documentation could be more detailed
     ```
   - Click "Submit review"

5. **Approve a PR**
   - Create another PR (or use different one)
   - Click "Review changes"
   - Select "Approve"
   - Add message: "Looks great! This improves the codebase."
   - Click "Submit review"

6. **Request Changes on PR**
   - Create another PR
   - Click "Review changes"
   - Select "Request changes"
   - Add message: "Please address the performance concerns in the helper function"
   - Click "Submit review"

**Verification Checklist:**
- [ ] Left comments on specific lines
- [ ] Provided constructive feedback
- [ ] Left general review comment
- [ ] Used "Approve" option
- [ ] Used "Request changes" option
- [ ] All review types visible in PR conversation

**Key Concepts:**
- Line comments should be specific and constructive
- General comments summarize review scope
- Approvals indicate quality confidence
- Request changes can block merging
- Professional reviews help maintain code quality

---

## Exercise 5: GitHub Flow Workflow

**Objective:** Practice the complete GitHub Flow workflow

**Instructions:**

1. **Create Issue** (optional but recommended)
   - Go to "Issues" tab
   - Click "New issue"
   - Title: "GitHub Flow Demo - Implement feature"
   - Description:
     ```
     ## Description
     This issue tracks implementation of a demo feature.
     
     ## Steps
     1. Create feature branch
     2. Make changes
     3. Create PR
     4. Review and discuss
     5. Merge when ready
     ```

2. **Create Feature Branch**
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/github-flow-demo
   ```

3. **Make Focused Changes**
   ```bash
   cat > github-flow.md << EOF
   # GitHub Flow Process
   
   1. Create a branch for feature/fix
   2. Make commits for each logical change
   3. Push branch to GitHub
   4. Create pull request to main
   5. Discuss and review changes
   6. Merge when approved
   7. Delete branch after merge
   EOF
   ```

4. **Commit Logically**
   ```bash
   git add github-flow.md
   git commit -m "docs: Add GitHub flow documentation"
   ```

5. **Multiple Commit Example**
   ```bash
   echo "## Benefits" >> github-flow.md
   echo "- Simple and clear process" >> github-flow.md
   git add github-flow.md
   git commit -m "docs: Add benefits section to GitHub flow"
   ```

6. **Push Feature Branch**
   ```bash
   git push -u origin feature/github-flow-demo
   ```

7. **Create Pull Request**
   - Reference issue if created: "Closes #<issue-number>"
   - Provide clear description
   - Ensure main is target branch

8. **Code Review Process**
   - Request reviews from team members
   - Leave feedback on your own PR
   - Iterate with comments and new commits

9. **Merge to Main**
   - Once approved, merge via GitHub UI
   - Delete branch (option in merge dialog)

10. **Cleanup Locally**
    ```bash
    git checkout main
    git pull origin main
    git branch -d feature/github-flow-demo
    ```

11. **Verify Complete Flow**
    ```bash
    git log --oneline --graph --all | head -10
    ```

**Verification Checklist:**
- [ ] Started from main branch
- [ ] Created focused feature branch
- [ ] Made related changes in logical commits
- [ ] Pushed branch to GitHub
- [ ] Created PR with issue reference
- [ ] Went through review process
- [ ] Merged via GitHub UI
- [ ] Deleted feature branch
- [ ] Verified clean local state

**Key Concepts:**
- GitHub Flow is simple: create branch → PR → review → merge
- Branches should be focused on single features
- PRs are discussion and review points
- Clean up after merging
- Main branch should always be deployable

---

## Exercise 6: Rebase vs Merge Workflow

**Objective:** Understand different merge strategies

**Instructions:**

1. **Rebase Merge Strategy**
   ```bash
   # Create feature branch
   git checkout -b feature/rebase-demo
   echo "Feature content" > rebase-feature.md
   git add rebase-feature.md
   git commit -m "feat: Add rebase demo feature"
   git push -u origin feature/rebase-demo
   ```

2. **Create PR with Rebase Option**
   - Create PR on GitHub
   - In merge section, click dropdown showing merge strategy
   - Select "Rebase and merge"
   - Click "Rebase and merge"
   - Feature commits are replayed on main

3. **View Linear History**
   ```bash
   git pull origin main
   git log --oneline | head -5
   # History appears linear - no merge commit
   ```

4. **Squash Merge Strategy**
   ```bash
   git checkout -b feature/squash-demo
   echo "First part" > squash-demo.md
   git add squash-demo.md
   git commit -m "WIP: Start squash demo feature"
   
   echo "Second part" >> squash-demo.md
   git add squash-demo.md
   git commit -m "WIP: Continue squash demo feature"
   
   echo "Final part" >> squash-demo.md
   git add squash-demo.md
   git commit -m "WIP: Complete squash demo feature"
   
   git push -u origin feature/squash-demo
   ```

5. **Create PR and Squash Merge**
   - Create PR on GitHub
   - Click merge dropdown
   - Select "Squash and merge"
   - Write single commit message: "feat: Add squash merge demo feature"
   - Merge

6. **View Squashed Result**
   ```bash
   git pull origin main
   git log --oneline | head -3
   # Multiple WIP commits become one clean commit
   ```

7. **Regular Merge (with merge commit)**
   ```bash
   git checkout -b feature/regular-merge-demo
   echo "Regular merge content" > regular-merge.md
   git add regular-merge.md
   git commit -m "feat: Add regular merge demo"
   git push -u origin feature/regular-merge-demo
   ```

8. **Create PR and Regular Merge**
   - Create PR
   - Select "Create a merge commit" option
   - Merge

9. **View Merge Commit**
   ```bash
   git pull origin main
   git log --oneline --graph | head -5
   # Merge commit appears with branch information
   ```

**Verification Checklist:**
- [ ] Rebased PR merged (linear history)
- [ ] Squashed PR merged (multiple commits → one)
- [ ] Regular merged PR (merge commit created)
- [ ] Can see all three strategies in git log
- [ ] Understand when to use each strategy

**Key Concepts:**
- **Rebase merge**: Linear history, clean timeline
- **Squash merge**: Multiple commits into one
- **Merge commit**: Preserves branch history
- Choose strategy based on team preferences
- Each strategy has different use cases

---

## Exercise 7: Handle Merge Conflicts in Collaboration

**Objective:** Resolve real team collaboration conflicts

**Instructions:**

1. **Set Up Conflict Scenario**
   ```bash
   # Main branch changes
   git checkout main
   git pull origin main
   echo "Production config: db.prod.com" > config.md
   git add config.md
   git commit -m "config: Set production database"
   git push origin main
   ```

2. **Create Feature Branch (from older main)**
   ```bash
   git checkout -b feature/dev-config
   echo "Development config: db.dev.local" > config.md
   git add config.md
   git commit -m "config: Set development database"
   git push -u origin feature/dev-config
   ```

3. **Create PR**
   - Create PR on GitHub
   - Will show conflict warning
   - Shows "Can't merge automatically"

4. **Resolve Conflict Locally**
   ```bash
   git fetch origin
   git merge origin/main
   # Will show merge conflict
   ```

5. **View Conflict Markers**
   ```bash
   cat config.md
   # Shows:
   # <<<<<<< HEAD
   # Development config: db.dev.local
   # =======
   # Production config: db.prod.com
   # >>>>>>>
   ```

6. **Decide on Resolution**
   ```bash
   # Resolution: Support both environments
   cat > config.md << EOF
   # Configuration File
   
   ## Development
   DB_HOST=db.dev.local
   
   ## Production
   DB_HOST=db.prod.com
   EOF
   ```

7. **Complete Merge**
   ```bash
   git add config.md
   git commit -m "fix: Resolve config conflict with dual environment setup"
   git push origin feature/dev-config
   ```

8. **Merge PR on GitHub**
   - GitHub now shows "Can merge" (conflict resolved)
   - Merge the PR

**Verification Checklist:**
- [ ] Created conflict scenario
- [ ] PR showed conflict warning
- [ ] Resolved conflict markers manually
- [ ] Test that resolution works for both cases
- [ ] Committed resolution
- [ ] PR merged successfully

**Key Concepts:**
- Conflicts are natural in team development
- Conflict markers show both versions
- Manual resolution is sometimes necessary
- Test resolution before final merge
- Clear communication helps prevent conflicts

---

## Exercise 8: Use GitHub Labels and Milestones

**Objective:** Organize work using GitHub organization features

**Instructions:**

1. **Create Custom Labels**
   - Go to repository "Settings"
   - Click "Labels" in left sidebar
   - Click "New label"
   - Create labels:
     - **Name:** `bug` | **Color:** Red (#d73a4a)
     - **Name:** `enhancement` | **Color:** Blue (#0366d6)
     - **Name:** `documentation` | **Color:** Green (#0075ca)
     - **Name:** `needs-review` | **Color:** Yellow (#ffd700)
     - **Name:** `wontfix` | **Color:** Gray (#cccccc)

2. **Create Milestone**
   - Go to "Issues" tab
   - Click "Milestones"
   - Click "New milestone"
   - Title: "Version 1.0"
   - Description: "First stable release"
   - Due date: Select future date

3. **Create Issues with Labels**
   - Create Issue 1:
     - Title: "Add user authentication"
     - Label: `enhancement`
     - Milestone: `Version 1.0`
   - Create Issue 2:
     - Title: "Fix login button styling"
     - Label: `bug`
     - Milestone: `Version 1.0`
   - Create Issue 3:
     - Title: "Update API documentation"
     - Label: `documentation`
     - Milestone: `Version 1.0`

4. **Link PR to Issues**
   - Create PR with title: "Implement authentication"
   - In description reference issue: "Closes #1"
   - GitHub auto-links and closes issue when merged

5. **Use Labels in PR**
   - Add labels to PR: `needs-review`, `enhancement`
   - GitHub shows label badges

6. **Track Milestone Progress**
   - Click "Milestones"
   - Version 1.0 shows progress
   - As PRs merge and issues close, progress updates

**Verification Checklist:**
- [ ] Created multiple custom labels
- [ ] Created milestone with due date
- [ ] Issues labeled appropriately
- [ ] PRs labeled for status
- [ ] Issues linked to PRs
- [ ] Milestone progress tracked

**Key Concepts:**
- Labels help categorize and filter work
- Milestones group related work
- Issue references auto-close issues
- Labels visible in PR reviews
- Organizational tools improve coordination

---

## Exercise 9: Enforce Branch Protection Rules

**Objective:** Set up workflow enforcement through branch protection

**Instructions:**

1. **Access Branch Settings**
   - Go to repository Settings
   - Click "Branches" in left sidebar
   - Under "Branch protection rules"
   - Click "Add rule"

2. **Set Up Basic Protection**
   - Branch name pattern: `main`
   - Check: "Require a pull request before merging"
   - Check: "Require approvals" (set to 1)
   - Check: "Restrict who can push to matching branches"
   - Click "Create"

3. **Test Protection Rule**
   ```bash
   # Try to push directly to main (should fail)
   git checkout main
   echo "test" > test.md
   git add test.md
   git commit -m "test: Try direct push to main"
   git push origin main
   # Should be rejected!
   ```

4. **Enforce Requirements via PR**
   ```bash
   git reset --soft HEAD~1
   git reset HEAD test.md
   git checkout test.md
   
   # Create proper PR workflow
   git checkout -b feature/test-branch-protection
   echo "test" > test.md
   git add test.md
   git commit -m "feat: Test branch protection"
   git push -u origin feature/test-branch-protection
   ```

5. **Create PR - This Should Work**
   - Create PR from feature branch
   - Add branch protection comment: "This enforces PR requirements"
   - Get approval (from yourself if solo)
   - Merge successfully

6. **View Branch Protection in PR**
   - On PR, see status checks:
     - "Requires pull request reviews"
     - "Requires approvals"
   - These must pass before merge button enables

**Verification Checklist:**
- [ ] Branch protection rule created for main
- [ ] Direct push to main is rejected
- [ ] PR workflow required instead
- [ ] Approval required before merging
- [ ] Protection enforced in PR interface

**Key Concepts:**
- Branch protection prevents accidental damage
- Requires PR for main branch changes
- Can require approvals and status checks
- Enforces workflow standards
- Prevents direct pushes to production branches

---

## Exercise 10: Continuous Collaboration Workflow

**Objective:** Practice complete team-like collaboration scenario

**Instructions:**

1. **Create Issue for Feature**
   - Title: "Add user feedback system"
   - Description: "Implement email feedback collection"
   - Label: `enhancement`

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/user-feedback
   ```

3. **Multiple Commits Over Time**
   ```bash
   echo "# Feedback System" > feedback.md
   git add feedback.md
   git commit -m "docs: Start feedback system documentation"
   
   # After some work...
   echo "## Email Collection" >> feedback.md
   git add feedback.md
   git commit -m "feat: Add email collection documentation"
   
   # More work...
   echo "## Database Schema" >> feedback.md
   git add feedback.md
   git commit -m "docs: Document feedback database schema"
   ```

4. **Push Feature Branch**
   ```bash
   git push -u origin feature/user-feedback
   ```

5. **Create Draft PR**
   - Create PR
   - Check "Draft" option
   - Description: "In progress - working on documentation"
   - Notify team: "Ready for early review"

6. **Add More Commits**
   ```bash
   # Implement actual code
   echo "function collectFeedback(email) { }" > feedback.js
   git add feedback.js
   git commit -m "feat: Implement feedback collection function"
   git push origin feature/user-feedback
   ```

7. **Mark PR Ready for Review**
   - Click "Ready for review" button on PR
   - Changes from draft to regular PR

8. **Request Review**
   - Request reviewers
   - Add comment: "@reviewer please check implementation"

9. **Address Feedback**
   ```bash
   # Receive feedback requesting validation
   echo "function collectFeedback(email) {" > feedback.js
   echo "  if (!email.includes('@')) return false;" >> feedback.js
   echo "  return true;" >> feedback.js
   echo "}" >> feedback.js
   git add feedback.js
   git commit -m "fix: Add email validation to feedback collection"
   git push origin feature/user-feedback
   ```

10. **Final Merge**
    - Once approved, merge to main
    - Delete feature branch
    - Close related issue

11. **Update Main Locally**
    ```bash
    git checkout main
    git pull origin main
    git branch -d feature/user-feedback
    ```

**Verification Checklist:**
- [ ] Created issue for tracking
- [ ] Feature branch with multiple commits
- [ ] Draft PR created for early feedback
- [ ] Converted draft to regular PR
- [ ] Addressed review feedback with new commits
- [ ] Final merge to main
- [ ] Local cleanup completed

**Key Concepts:**
- Real workflows involve iteration
- PRs start as drafts for feedback
- Multiple commits show development story
- Feedback leads to code improvements
- Complete process: issue → branch → draft → review → merge

---

## Chapter 2 Challenge Project

**Objective:** Lead a complete collaboration workflow

**Project:** Collaborative Feature Implementation

**Requirements:**

1. Create GitHub issue with detailed requirements
2. Create feature branch with meaningful name
3. Make at least 5 commits with clear messages
4. Create PR with comprehensive description
5. Request code review (from self or others)
6. Address review feedback with new commits
7. Use labels and milestones
8. Set up branch protection for main
9. Merge with proper PR workflow
10. Delete branch and close issue

**Success Criteria:**
- [ ] Issue tracking feature request
- [ ] Feature branch contains all changes
- [ ] Clear commit history
- [ ] PR includes discussion and improvements
- [ ] Proper branch protection enforced
- [ ] Clean merge with PR workflow
- [ ] Project repository well-organized

---

## Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| PR shows conflicts | Pull main and resolve locally before pushing |
| Can't merge PR | Ensure all protection requirements are met |
| Review comments lost | Check all tabs and conversation history |
| Branch not deleted on merge | Check if squash/rebase was used |
| Draft PR won't let me request review | Convert to regular PR first |
| Can't push to main | Branch protection active - use PR workflow |

---

## Next Steps

You've completed Chapter 2 exercises! You now understand:
- ✅ Creating and managing pull requests
- ✅ Code review process and best practices
- ✅ GitHub Flow collaborative workflow
- ✅ Handling merge conflicts in teams
- ✅ Organizing work with labels and milestones
- ✅ Enforcing quality with branch protection

**Proceed to Chapter 3: Advanced Topics** to learn about rebasing, stashing, and GitHub automation.

---

**[← Back to Chapter 2 Overview](./README.md)** | **[Next: Chapter 3 →](../Chapter-3-Advanced-Topics/README.md)**
