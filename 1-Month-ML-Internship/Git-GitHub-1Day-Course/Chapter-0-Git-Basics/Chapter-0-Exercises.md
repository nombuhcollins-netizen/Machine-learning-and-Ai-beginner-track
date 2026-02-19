# Chapter 0: Git Basics - Comprehensive Exercises

**Difficulty:** Beginner | **Estimated Time:** 1.5 hours | **Prerequisites:** Git installed

---

## Overview

This exercise file consolidates and expands on all exercises from Chapter 0 modules. Complete these exercises to master local Git operations.

---

## Exercise 1: Complete Git Setup and Configuration

**Objective:** Ensure Git is properly installed and configured on your machine

**Instructions:**

1. **Verify Git Installation**
   ```bash
   git --version
   ```

2. **Set Up Global Configuration**
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

3. **Verify Configuration**
   ```bash
   git config --global user.name
   git config --global user.email
   git config --list
   ```

**Verification Checklist:**
- [ ] Git version is 2.0 or higher
- [ ] Global user.name is set correctly
- [ ] Global user.email is set correctly
- [ ] `git config --list` shows your configuration

---

## Exercise 2: Create and Initialize Your First Repository

**Objective:** Create a repository and understand the .git directory

**Instructions:**

1. **Create Project Directory**
   ```bash
   mkdir git-basics-practice
   cd git-basics-practice
   ```

2. **Initialize Repository**
   ```bash
   git init
   ```

3. **Explore the .git Directory**
   ```bash
   ls -la          # View all files including hidden ones
   ls .git         # View git directory contents
   ```

4. **Check Initial Status**
   ```bash
   git status
   ```

**Verification Checklist:**
- [ ] Directory was created successfully
- [ ] `git init` completed without errors
- [ ] `.git` directory exists
- [ ] `git status` shows "initial commit" message

**Key Concepts:**
- The `.git` directory contains all repository metadata
- A repository is a Git-tracked project

---

## Exercise 3: Staging and Committing Files

**Objective:** Master the staging area and create your first commits

**Instructions:**

1. **Create Initial Files**
   ```bash
   echo "# My Git Project" > README.md
   echo "console.log('Hello Git');" > app.js
   echo "body { margin: 0; }" > style.css
   ```

2. **Check Status**
   ```bash
   git status
   ```

3. **Stage Files Individually**
   ```bash
   git add README.md
   git status
   ```

4. **Create First Commit**
   ```bash
   git commit -m "docs: Add project README"
   ```

5. **Stage and Commit Remaining Files**
   ```bash
   git add app.js
   git commit -m "feat: Add JavaScript application file"
   
   git add style.css
   git commit -m "style: Add CSS stylesheet"
   ```

6. **View Commit History**
   ```bash
   git log
   git log --oneline
   ```

**Verification Checklist:**
- [ ] All three files were created
- [ ] Each file received an individual commit
- [ ] Commit messages follow the format: `type: description`
- [ ] `git log --oneline` shows all three commits

**Key Concepts:**
- Staging area (index) is where you prepare changes
- Commits capture snapshots of your work
- Semantic commit messages improve history

---

## Exercise 4: Modify and Track Changes

**Objective:** Understand how Git tracks file modifications

**Instructions:**

1. **Modify README.md**
   ```bash
   echo "" >> README.md
   echo "## Getting Started" >> README.md
   echo "This is my first Git project." >> README.md
   ```

2. **Check What Changed**
   ```bash
   git status
   git diff README.md
   ```

3. **Stage the Modification**
   ```bash
   git add README.md
   ```

4. **View Staged Changes**
   ```bash
   git diff --staged README.md
   ```

5. **Commit the Update**
   ```bash
   git commit -m "docs: Update README with getting started section"
   ```

6. **Create Another Modification**
   ```bash
   echo "const version = '1.0.0';" >> app.js
   ```

7. **Compare Commits**
   ```bash
   git log --oneline
   git show HEAD
   git show HEAD~1
   ```

**Verification Checklist:**
- [ ] Changes were visible with `git diff`
- [ ] Staged changes showed correctly with `git diff --staged`
- [ ] New commit was created
- [ ] Historical commits are viewable with `git show`

**Key Concepts:**
- `git diff` shows working directory changes
- `git diff --staged` shows staged changes
- `git show` displays commit details

---

## Exercise 5: Branching Fundamentals

**Objective:** Create and switch between branches

**Instructions:**

1. **List Current Branches**
   ```bash
   git branch
   ```

2. **Create a New Branch**
   ```bash
   git branch feature/add-authentication
   git branch          # Verify creation
   ```

3. **Switch to New Branch**
   ```bash
   git checkout feature/add-authentication
   # or use newer syntax:
   git switch feature/add-authentication
   ```

4. **Create Work on New Branch**
   ```bash
   echo "function authenticate(user, pass) {" > auth.js
   echo "  // Authentication logic" >> auth.js
   echo "}" >> auth.js
   ```

5. **Commit on Feature Branch**
   ```bash
   git add auth.js
   git commit -m "feat: Add authentication module"
   ```

6. **Check Branch History**
   ```bash
   git log --oneline
   git log --graph --all --decorate
   ```

7. **Return to Main Branch**
   ```bash
   git checkout main
   # Note: List of files should NOT include auth.js
   ls
   ```

8. **Switch Back to Feature Branch**
   ```bash
   git checkout feature/add-authentication
   ls      # auth.js should be visible again
   ```

**Verification Checklist:**
- [ ] Feature branch was created
- [ ] Switched to feature branch successfully
- [ ] Created and committed auth.js on feature branch
- [ ] Switched back to main - auth.js not visible
- [ ] Switched back to feature - auth.js visible

**Key Concepts:**
- `git branch` creates isolated development lines
- `git checkout` switches between branches
- Each branch maintains its own file state

---

## Exercise 6: Merging Branches

**Objective:** Merge feature branches back to main

**Instructions:**

1. **Ensure on Main Branch**
   ```bash
   git checkout main
   ```

2. **View Differences Before Merge**
   ```bash
   git log --oneline --graph --all
   git diff main feature/add-authentication
   ```

3. **Merge Feature Branch**
   ```bash
   git merge feature/add-authentication
   ```

4. **Verify Merge**
   ```bash
   ls      # Should now include auth.js
   git log --oneline
   ```

5. **Create Another Feature Branch**
   ```bash
   git branch feature/add-database
   git checkout feature/add-database
   
   echo "Database connection code" > database.js
   git add database.js
   git commit -m "feat: Add database connection module"
   ```

6. **Merge Second Feature**
   ```bash
   git checkout main
   git merge feature/add-database
   ```

7. **View Final History**
   ```bash
   git log --oneline --graph --all
   ```

**Verification Checklist:**
- [ ] Feature branches were merged into main successfully
- [ ] All files (auth.js, database.js) exist on main
- [ ] Git log shows merge commits
- [ ] No merge conflicts occurred

**Key Concepts:**
- `git merge` integrates branches
- Merge commits record integration points
- Fast-forward merges occur when no concurrent changes exist

---

## Exercise 7: Resolving Merge Conflicts

**Objective:** Understand and resolve merge conflicts

**Instructions:**

1. **Create Conflicting Branches**
   ```bash
   git checkout -b feature/update-config
   ```

2. **Modify config.js on feature branch**
   ```bash
   echo "// Configuration file" > config.js
   echo "const API_URL = 'https://api.dev.com';" >> config.js
   git add config.js
   git commit -m "feat: Add configuration file with dev endpoint"
   ```

3. **Switch to Main and Create Conflict**
   ```bash
   git checkout main
   echo "// Configuration file" > config.js
   echo "const API_URL = 'https://api.prod.com';" >> config.js
   git add config.js
   git commit -m "feat: Add configuration file with prod endpoint"
   ```

4. **Attempt Merge**
   ```bash
   git merge feature/update-config
   # This should show a conflict
   ```

5. **View Conflict**
   ```bash
   cat config.js
   git status
   ```

6. **Resolve Conflict Manually**
   ```bash
   # Edit config.js to keep desired version:
   echo "// Configuration file" > config.js
   echo "const API_URL = 'https://api.example.com';" >> config.js
   echo "// Supports both dev and prod configs" >> config.js
   ```

7. **Complete Merge**
   ```bash
   git add config.js
   git commit -m "fix: Resolve config endpoint conflict"
   ```

8. **Verify Resolution**
   ```bash
   git log --oneline --graph --all
   cat config.js
   ```

**Verification Checklist:**
- [ ] Conflict was created as expected
- [ ] Conflict markers (<<<, ===, >>>) were visible
- [ ] Manual resolution was completed
- [ ] Merge was finalized with commit
- [ ] Final config.js contains desired configuration

**Key Concepts:**
- Conflicts occur when same lines are modified differently
- Conflict markers show competing changes
- Manual resolution requires editing the file
- Merge must be completed after resolution

---

## Exercise 8: Undoing Changes Safely

**Objective:** Learn safe methods to undo mistakes

**Instructions:**

1. **Make a Mistake (Intentionally)**
   ```bash
   echo "WRONG CONTENT" > app.js
   git status
   ```

2. **Discard Changes Before Staging**
   ```bash
   git diff app.js     # See the mistake
   git restore app.js  # Undo the change
   cat app.js          # Should show original content
   ```

3. **Create Another Mistake**
   ```bash
   echo "ANOTHER MISTAKE" > style.css
   git add style.css
   git status
   ```

4. **Unstage Without Discarding**
   ```bash
   git restore --staged style.css
   git status          # File should be unstaged
   cat style.css       # File still contains mistake
   ```

5. **Discard Unstaged Changes**
   ```bash
   git restore style.css
   cat style.css       # Should be restored
   ```

6. **Revert a Commit (Safe Undo)**
   ```bash
   git log --oneline | head -5
   git revert HEAD~1 -m "Safely undo previous commit"
   git log --oneline | head -5    # Should show new revert commit
   ```

**Verification Checklist:**
- [ ] `git restore` discarded working directory changes
- [ ] `git restore --staged` unstaged files without losing changes
- [ ] Original file content was preserved when appropriately restored
- [ ] `git revert` created a new commit undoing changes

**Key Concepts:**
- `git restore` safely reverts changes
- `git revert` creates a new commit undoing previous changes
- Never use `git reset --hard` unless absolutely certain

---

## Exercise 9: Working with Commit History

**Objective:** Navigate and understand commit history

**Instructions:**

1. **View Full Log**
   ```bash
   git log
   ```

2. **View Condensed Log**
   ```bash
   git log --oneline
   ```

3. **View With Branch Graph**
   ```bash
   git log --graph --all --decorate
   ```

4. **Filter by Author**
   ```bash
   git log --author="Your Name"
   ```

5. **Filter by Date**
   ```bash
   git log --since="2 days ago"
   git log --until="1 day ago"
   ```

6. **Search by Message**
   ```bash
   git log --grep="feat:"
   ```

7. **View Specific Commit Details**
   ```bash
   git log --oneline | head -1    # Get latest commit hash
   git show <commit-hash>          # View full details
   ```

8. **View File-Specific History**
   ```bash
   git log --oneline app.js
   git log --oneline -- README.md
   ```

**Verification Checklist:**
- [ ] Log commands display history in various formats
- [ ] Can filter commits by author and date
- [ ] Can search commits by message
- [ ] Specific commit details are viewable
- [ ] File-specific history is accessible

**Key Concepts:**
- Log commands help understand project evolution
- Filters enable finding specific commits
- History inspection aids debugging and understanding

---

## Exercise 10: Stashing Work in Progress

**Objective:** Temporarily save incomplete work

**Instructions:**

1. **Create Work in Progress**
   ```bash
   git checkout -b feature/incomplete-work
   echo "Incomplete feature code" > newfeature.js
   git add newfeature.js
   echo "More incomplete work" >> app.js
   ```

2. **Check Status**
   ```bash
   git status
   ```

3. **Stash Changes**
   ```bash
   git stash
   git status          # Should show clean working directory
   ls                  # newfeature.js should not exist
   ```

4. **Stash List**
   ```bash
   git stash list
   ```

5. **Switch Branches Without Committing**
   ```bash
   git checkout main
   ls                  # newfeature.js not here (stashed)
   ```

6. **Return to Feature Branch**
   ```bash
   git checkout feature/incomplete-work
   ```

7. **Restore Stashed Work**
   ```bash
   git stash pop
   git status          # Changes restored
   ls                  # newfeature.js restored
   ```

**Verification Checklist:**
- [ ] Changes were stashed successfully
- [ ] Working directory was clean after stashing
- [ ] Can switch branches with stashed changes
- [ ] Stashed changes were restored correctly
- [ ] `git stash list` showed stashed items

**Key Concepts:**
- `git stash` temporarily saves incomplete work
- Stashing allows switching branches without committing
- `git stash pop` restores stashed changes

---

## Chapter 0 Challenge Project

**Objective:** Apply all learned skills in one project

**Project:** Create a Personal Portfolio Repository

**Requirements:**

1. Create a new repository called `portfolio`
2. Create multiple files:
   - `README.md` - Portfolio description
   - `projects.json` - List of projects
   - `bio.txt` - Personal biography
3. Create at least 3 commits with semantic messages
4. Create a `dev` branch and make 2 commits there
5. Merge the `dev` branch back to main
6. Create a `bugfix/typos` branch, make changes, and merge
7. View complete history with `git log --graph --all --decorate`

**Success Criteria:**
- [ ] Repository created with `git init`
- [ ] Multiple files with semantic commits
- [ ] Branch operations completed
- [ ] Merges successful with visible history
- [ ] All commits have clear descriptive messages

---

## Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| "fatal: not a git repository" | Run `git init` in your directory |
| "Please tell me who you are" | Set `git config user.name` and `user.email` |
| Merge conflict | Manually edit files, then `git add` and `git commit` |
| Removed file by mistake | Use `git restore filename` |
| Wrong commit message | Use `git commit --amend -m "New message"` |
| Need to switch branches with changes | Use `git stash` before switching |

---

## Next Steps

You've completed Chapter 0 exercises! You now understand:
- ✅ Git initialization and configuration
- ✅ Staging and committing
- ✅ Branching and merging
- ✅ Conflict resolution
- ✅ History inspection and manipulation

**Proceed to Chapter 1: GitHub Fundamentals** to learn about remote repositories and collaboration.

---

**[← Back to Chapter 0 Overview](./README.md)** | **[Next: Chapter 1 →](../Chapter-1-GitHub-Fundamentals/README.md)**
