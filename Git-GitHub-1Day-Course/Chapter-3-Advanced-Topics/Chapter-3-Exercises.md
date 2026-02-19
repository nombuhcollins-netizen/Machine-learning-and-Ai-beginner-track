# Chapter 3: Advanced Topics - Comprehensive Exercises

**Difficulty:** Advanced | **Estimated Time:** 1.5 hours | **Prerequisites:** Chapters 0-2 completed

---

## Overview

This exercise file consolidates and expands on all exercises from Chapter 3 modules. Complete these exercises to master advanced Git techniques, versioning, and GitHub automation.

---

## Exercise 1: Interactive Rebase for History Cleanup

**Objective:** Use interactive rebase to reorganize and clean commit history

**Instructions:**

1. **Create Scenario with Multiple Commits**
   ```bash
   git checkout -b feature/rebase-demo
   
   # Create commits (some will be cleaned up)
   echo "Feature start" > feature.md
   git add feature.md
   git commit -m "WIP: Start feature development"
   
   echo "Add documentation" >> feature.md
   git add feature.md
   git commit -m "docs: Work in progress documentation"
   
   echo "Implement logic" > logic.js
   git add logic.js
   git commit -m "WIP: Implement feature logic"
   
   echo "More logic" >> logic.js
   git add logic.js
   git commit -m "WIP: Continue implementation"
   
   echo "Fix bug" >> logic.js
   git add logic.js
   git commit -m "fix: Correct logic error"
   
   git push -u origin feature/rebase-demo
   ```

2. **View Commit History**
   ```bash
   git log --oneline -5
   ```

3. **Start Interactive Rebase**
   ```bash
   # Rebase last 5 commits
   git rebase -i HEAD~5
   ```

4. **Edit Rebase Instructions**
   In the editor, you'll see:
   ```
   pick <hash1> WIP: Start feature development
   pick <hash2> docs: Work in progress documentation
   pick <hash3> WIP: Implement feature logic
   pick <hash4> WIP: Continue implementation
   pick <hash5> fix: Correct logic error
   ```

   Change to:
   ```
   pick <hash1> WIP: Start feature development
   squash <hash2> docs: Work in progress documentation
   squash <hash3> WIP: Implement feature logic
   squash <hash4> WIP: Continue implementation
   pick <hash5> fix: Correct logic error
   ```

5. **Write Combined Commit Message**
   When asked, write:
   ```
   feat: Implement feature with documentation
   
   - Started feature development
   - Added comprehensive documentation
   - Implemented core logic
   - Fixed logic error in implementation
   ```

6. **Complete Rebase**
   ```bash
   git log --oneline -3
   # Should show 2 commits instead of 5
   ```

7. **Force Push to GitHub**
   ```bash
   git push origin feature/rebase-demo --force
   ```

8. **View Updated PR on GitHub**
   - If you have a PR, it shows cleaned history
   - Commit count updated

**Verification Checklist:**
- [ ] Multiple commits created
- [ ] Interactive rebase launched
- [ ] Squash commands used correctly
- [ ] Combined commit message written
- [ ] History cleaned and reduced
- [ ] Force push successful
- [ ] GitHub PR updated with clean history

**Key Concepts:**
- Interactive rebase allows history editing
- `pick` = keep commit
- `squash` = combine with previous commit
- `reword` = change commit message
- Force push required after rebase (use carefully!)
- Main branch should never be rebased in team setting

---

## Exercise 2: Cherry-Pick Specific Commits

**Objective:** Apply specific commits to different branches

**Instructions:**

1. **Create Base Commits**
   ```bash
   git checkout main
   git checkout -b feature/cherry-pick-source
   
   # Create multiple commits
   echo "Bug fix 1" > bug1.md
   git add bug1.md
   git commit -m "fix: Critical security issue"
   
   echo "Bug fix 2" > bug2.md
   git add bug2.md
   git commit -m "fix: Performance improvement"
   
   echo "Feature 1" > feature1.md
   git add feature1.md
   git commit -m "feat: New user dashboard"
   
   echo "Bug fix 3" > bug3.md
   git add bug3.md
   git commit -m "fix: Memory leak in service"
   
   git log --oneline -4
   ```

2. **Note Commit Hashes**
   ```bash
   # Remember hashes of:
   # - "fix: Critical security issue"
   # - "fix: Performance improvement"
   # - "fix: Memory leak in service"
   ```

3. **Create Hotfix Branch**
   ```bash
   git checkout main
   git checkout -b hotfix/critical-fixes
   ```

4. **Cherry-Pick Critical Fixes Only**
   ```bash
   # Get hash of first fix
   git log feature/cherry-pick-source --oneline | grep "security"
   # Copy hash and cherry-pick
   git cherry-pick <hash>
   
   # Cherry-pick performance fix
   git log feature/cherry-pick-source --oneline | grep "Performance"
   git cherry-pick <hash>
   
   # Cherry-pick memory leak fix
   git log feature/cherry-pick-source --oneline | grep "Memory"
   git cherry-pick <hash>
   ```

5. **Verify Cherry-Picked Commits**
   ```bash
   git log --oneline -5
   # Should show 3 picked commits
   ```

6. **Resolve Cherry-Pick Conflicts (if any)**
   ```bash
   # If conflict occurs during cherry-pick:
   # Edit conflicted files
   git add <resolved-files>
   git cherry-pick --continue
   ```

7. **Push Hotfix Branch**
   ```bash
   git push -u origin hotfix/critical-fixes
   ```

8. **Create PR for Hotfix**
   - Create PR to main with critical fixes only
   - Merge to main
   - Publish hotfix version

**Verification Checklist:**
- [ ] Source branch with multiple commits created
- [ ] Hotfix branch created from main
- [ ] Specific commits cherry-picked
- [ ] Final branch contains only selected commits
- [ ] Feature commit NOT in hotfix
- [ ] Branch pushed to GitHub
- [ ] Cherry-picked history visible in PR

**Key Concepts:**
- Cherry-pick applies specific commits to another branch
- Useful for selective backporting
- Different from merge (doesn't include all commits)
- Can cause duplicate commits if not careful
- Helpful for hotfixes and selective patches

---

## Exercise 3: Reset and Reflog Recovery

**Objective:** Understand different reset types and recover lost commits

**Instructions:**

1. **Create Commits to Experiment With**
   ```bash
   git checkout -b feature/reset-demo
   
   echo "Content 1" > file1.md
   git add file1.md
   git commit -m "feat: Add file 1"
   
   echo "Content 2" > file2.md
   git add file2.md
   git commit -m "feat: Add file 2"
   
   echo "Content 3" > file3.md
   git add file3.md
   git commit -m "feat: Add file 3"
   
   git log --oneline
   ```

2. **Soft Reset (Keep Changes)**
   ```bash
   git reset --soft HEAD~1
   git status          # File3 is staged
   ls                  # file3.md still exists
   git log --oneline   # "Add file 3" commit gone
   ```

3. **Continue with Soft Reset**
   ```bash
   git commit -m "feat: Add file 3 with better message"
   git log --oneline
   ```

4. **Mixed Reset (Unstage Changes)**
   ```bash
   echo "Content 4" > file4.md
   git add file4.md
   git commit -m "feat: Add file 4"
   
   git reset --mixed HEAD~1
   git status          # file4.md is untracked
   cat file4.md        # File still exists locally
   ```

5. **Hard Reset (Discard Changes)**
   ```bash
   echo "Content 5" > file5.md
   git add file5.md
   git commit -m "WIP: Add file 5"
   
   git reset --hard HEAD~1
   ls                  # file5.md is GONE
   git log --oneline   # Commit removed
   ```

6. **Recover Lost Commit with Reflog**
   ```bash
   git reflog          # Shows all HEAD movements
   # Find commit like: <hash> HEAD@{5}: commit: WIP: Add file 5
   ```

7. **Recovery Process**
   ```bash
   git reset --hard <hash-from-reflog>
   ls                  # file5.md is restored!
   git log --oneline
   ```

8. **View Reflog Details**
   ```bash
   git log -g          # Shows reflog with commit info
   git show <hash>     # View recovered commit
   ```

**Verification Checklist:**
- [ ] Soft reset kept changes
- [ ] Mixed reset unstaged files
- [ ] Hard reset removed files
- [ ] Reflog showed commit history
- [ ] Lost commit recovered successfully
- [ ] Recovery restored file content

**Key Concepts:**
- `git reset --soft`: Undo commit, keep changes staged
- `git reset --mixed`: Undo commit, keep changes unstaged
- `git reset --hard`: Undo commit, discard changes
- Reflog is "undo" button for git
- Nothing is truly lost unless reflog expires (30 days default)

---

## Exercise 4: Stashing and Advanced Stash Management

**Objective:** Master temporary work storage with stash

**Instructions:**

1. **Create Work to Stash**
   ```bash
   git checkout -b feature/stash-demo
   
   # Make uncommitted changes
   echo "Work in progress" > wip.md
   echo "More WIP" > feature-draft.js
   ```

2. **Basic Stash**
   ```bash
   git status          # Shows untracked/uncommitted files
   git stash           # Stash all changes
   git status          # Clean working directory
   ```

3. **Stash List**
   ```bash
   git stash list
   # Shows: stash@{0}: WIP on feature/stash-demo
   ```

4. **Pop Stash**
   ```bash
   git stash pop       # Restore and remove from stash
   git status          # Changes back
   ```

5. **Multiple Stashes**
   ```bash
   echo "Stash 1" > work1.md
   git stash save "Working on feature 1"
   
   echo "Stash 2" > work2.md
   git stash save "Working on feature 2"
   
   echo "Stash 3" > work3.md
   git stash save "Working on feature 3"
   
   git stash list      # Shows all 3 stashes
   ```

6. **Apply Specific Stash**
   ```bash
   git stash apply stash@{1}  # Apply without removing
   git stash list              # Stash still exists
   ```

7. **Drop Stash**
   ```bash
   git stash drop stash@{0}  # Remove from stash
   git stash list            # One less stash
   ```

8. **Clear All Stashes**
   ```bash
   git stash clear     # Remove all stashes
   git stash list      # Empty
   ```

9. **Stash with Staged Changes**
   ```bash
   echo "Content" > staged.md
   git add staged.md   # Stage it
   
   git stash
   git stash show -p   # View stashed changes
   ```

10. **Create Branch from Stash**
    ```bash
    echo "Important work" > important.md
    git stash save "Important feature"
    
    git stash branch feature/from-stash
    # Creates new branch and applies stash
    git log --oneline
    ```

**Verification Checklist:**
- [ ] Created and stashed changes
- [ ] Listed multiple stashes
- [ ] Popped stash to restore changes
- [ ] Applied specific stash
- [ ] Dropped individual stashes
- [ ] Cleared all stashes
- [ ] Created branch from stash

**Key Concepts:**
- Stash temporarily saves work
- `git stash pop` = apply + drop
- `git stash apply` = restore without removing
- Multiple stashes can be managed
- Stashes can create new branches
- Useful for switching context without committing

---

## Exercise 5: Tags and Semantic Versioning

**Objective:** Create and manage version tags

**Instructions:**

1. **Create Lightweight Tags**
   ```bash
   git checkout main
   git tag v1.0.0
   git tag              # List tags
   ```

2. **Create Annotated Tags**
   ```bash
   git tag -a v1.1.0 -m "Version 1.1.0 - Bug fixes and improvements"
   git tag -l          # List all tags
   git show v1.1.0     # Show tag details
   ```

3. **Tag Specific Commit**
   ```bash
   # Get a commit hash
   git log --oneline | head -3
   
   # Tag it
   git tag -a v1.0.5 -m "Hotfix release" <commit-hash>
   git tag -l
   ```

4. **Semantic Versioning Practice**
   ```bash
   # MAJOR.MINOR.PATCH
   git tag v2.0.0 -m "Major version - Breaking changes"
   git tag v2.1.0 -m "Minor version - New features"
   git tag v2.1.1 -m "Patch version - Bug fixes"
   
   git tag -l --sort=version:refname  # Sort by version
   ```

5. **Push Tags to GitHub**
   ```bash
   git push origin v1.0.0              # Push single tag
   git push origin --tags              # Push all tags
   ```

6. **View Tags on GitHub**
   - Go to repository
   - Click "Releases" tab
   - Tags appear as releases

7. **Create Release from Tag**
   - Go to "Releases"
   - Click "Draft a new release"
   - Select tag: v1.0.0
   - Add release notes:
     ```
     ## Version 1.0.0 Release
     
     ### Features
     - Feature 1
     - Feature 2
     
     ### Bug Fixes
     - Fixed bug 1
     - Fixed bug 2
     
     ### Documentation
     - Added API documentation
     ```
   - Click "Publish release"

8. **Download Release Artifacts**
   - GitHub creates downloadable source archives
   - Visible on release page

**Verification Checklist:**
- [ ] Created lightweight and annotated tags
- [ ] Tagged specific commits
- [ ] Used semantic versioning (major.minor.patch)
- [ ] Pushed tags to GitHub
- [ ] Created release from tag
- [ ] Release notes visible on GitHub
- [ ] Tags sorted by version

**Key Concepts:**
- Tags mark specific points in history
- Lightweight tags are simple references
- Annotated tags include metadata and message
- Semantic versioning: MAJOR.MINOR.PATCH
- Releases are GitHub's way to distribute versions
- Tags should match version numbers

---

## Exercise 6: GitHub Actions and Automation

**Objective:** Create basic GitHub Actions workflow

**Instructions:**

1. **Create Actions Workflow Directory**
   ```bash
   mkdir -p .github/workflows
   cd .github/workflows
   ```

2. **Create Simple Workflow File**
   ```bash
   cat > hello-world.yml << 'EOF'
   name: Hello World Workflow
   
   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]
   
   jobs:
     hello:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Run a simple script
           run: |
             echo "Hello from GitHub Actions!"
             echo "Running on: ${{ runner.os }}"
             echo "Branch: ${{ github.ref }}"
   EOF
   ```

3. **Commit Workflow**
   ```bash
   cd ../..
   git add .github/
   git commit -m "ci: Add hello world GitHub Actions workflow"
   git push origin main
   ```

4. **View Workflow Execution**
   - Go to repository on GitHub
   - Click "Actions" tab
   - See workflow execution
   - Click on run to see details and logs

5. **Create Linting Workflow** (example)
   ```bash
   cat > .github/workflows/lint.yml << 'EOF'
   name: Code Quality Check
   
   on: [push, pull_request]
   
   jobs:
     lint:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Check file structure
           run: |
             echo "Checking repository structure..."
             ls -la
             echo "All files accounted for!"
   EOF
   ```

6. **Commit Linting Workflow**
   ```bash
   git add .github/workflows/lint.yml
   git commit -m "ci: Add code quality check workflow"
   git push origin main
   ```

7. **Create Workflow with Conditional Steps**
   ```bash
   cat > .github/workflows/conditional.yml << 'EOF'
   name: Conditional Workflow
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Check if main branch
           if: github.ref == 'refs/heads/main'
           run: echo "Running on main branch"
         
         - name: Check if pull request
           if: github.event_name == 'pull_request'
           run: echo "This is a pull request"
   EOF
   ```

8. **Commit Conditional Workflow**
   ```bash
   git add .github/workflows/conditional.yml
   git commit -m "ci: Add conditional workflow with branch checks"
   git push origin main
   ```

9. **Monitor Workflow Status**
   - Create a PR to trigger workflows
   - See status checks on PR
   - Workflows run on push and PR
   - Results appear in Actions tab

**Verification Checklist:**
- [ ] .github/workflows directory created
- [ ] hello-world.yml workflow created and committed
- [ ] Workflow executed successfully
- [ ] Lint workflow created
- [ ] Conditional workflow created
- [ ] All workflows visible in Actions tab
- [ ] Workflow logs show proper output

**Key Concepts:**
- GitHub Actions automate tasks
- Workflows trigger on events (push, PR, schedule)
- Jobs run on virtual machines
- Steps are individual commands/actions
- Can use community actions or write own
- Status checks appear on PRs

---

## Exercise 7: Bisect to Find Bugs

**Objective:** Use binary search to find bug-introducing commit

**Instructions:**

1. **Create Scenario with Bug**
   ```bash
   git checkout -b feature/bisect-demo
   
   # Good commit
   echo "function add(a, b) { return a + b; }" > calc.js
   git add calc.js
   git commit -m "feat: Add calculator functions"
   
   # Introduce bug
   echo "function multiply(a, b) { return a + b; }" >> calc.js
   git add calc.js
   git commit -m "feat: Add multiply function"
   
   # More commits before bug is noticed
   echo "function subtract(a, b) { return a - b; }" >> calc.js
   git add calc.js
   git commit -m "feat: Add subtract function"
   
   echo "function divide(a, b) { return a - b; }" >> calc.js
   git add calc.js
   git commit -m "feat: Add divide function"
   
   git log --oneline
   ```

2. **Notice There's a Bug**
   ```bash
   # Realize multiply and divide don't work correctly
   # Need to find which commit introduced the bug
   ```

3. **Start Bisect**
   ```bash
   git bisect start
   git bisect bad          # Current commit is bad (has bug)
   git bisect good HEAD~3  # Earlier commit was good
   ```

4. **Bisect Checks Out Commits**
   ```bash
   # Git checks out middle commit
   # Examine calc.js to see if multiply works
   cat calc.js
   
   # Multiply works but divide has the bug pattern
   ```

5. **Mark Commits**
   ```bash
   git bisect good         # This commit is good
   
   # Git checks out next midpoint
   # Multiply shows the bug (add instead of multiply)
   ```

6. **Find Problem Commit**
   ```bash
   git bisect bad
   
   # Git narrows down to problematic commit
   # Shows: commit <hash> is the first bad commit
   ```

7. **End Bisect**
   ```bash
   git bisect reset
   git checkout feature/bisect-demo
   ```

8. **Review Problem Commit**
   ```bash
   git show <hash-of-bad-commit>
   # Analysis reveals multiply function uses + instead of *
   ```

**Verification Checklist:**
- [ ] Commits with bug created
- [ ] Bisect start initiated
- [ ] Good and bad commits marked
- [ ] Bisect narrowed down bug location
- [ ] Problem commit identified
- [ ] Bisect reset completed
- [ ] Can view exact bug-introducing commit

**Key Concepts:**
- Binary search finds bugs quickly
- Mark commits as good/bad during bisect
- Automated search through history
- Useful for multi-commit changes
- Speeds up debugging compared to manual search
- Can bisect up to hundreds of commits

---

## Exercise 8: Worktrees for Parallel Work

**Objective:** Use worktrees to work on multiple branches simultaneously

**Instructions:**

1. **List Current Worktrees**
   ```bash
   git worktree list
   # Shows main worktree
   ```

2. **Create New Worktree**
   ```bash
   git worktree add ../feature-worktree feature/new-feature
   ```

3. **Switch to New Worktree Directory**
   ```bash
   cd ../feature-worktree
   git log --oneline
   git status
   ```

4. **Work in Worktree**
   ```bash
   echo "Feature code" > feature.js
   git add feature.js
   git commit -m "feat: Implement new feature"
   git push origin feature/new-feature
   ```

5. **Return to Main Worktree**
   ```bash
   cd ../seedai           # Back to main
   git worktree list      # Shows both worktrees
   ```

6. **Continue Work in Main**
   ```bash
   echo "Documentation" > docs.md
   git add docs.md
   git commit -m "docs: Add documentation"
   git push origin main
   ```

7. **View Worktree Status**
   ```bash
   git worktree list
   # Shows:
   # /path/to/main worktree (bare)
   # /path/to/feature-worktree feature-branch detached
   ```

8. **Remove Worktree**
   ```bash
   # First, cd out of worktree to main
   cd ../seedai
   git worktree remove ../feature-worktree
   ```

9. **Verify Removal**
   ```bash
   git worktree list
   # Only main worktree remains
   ```

**Verification Checklist:**
- [ ] Listed existing worktrees
- [ ] Created new worktree for feature branch
- [ ] Worked independently in both worktrees
- [ ] Made commits in separate worktrees
- [ ] Removed worktree successfully
- [ ] Main work unaffected by worktree usage

**Key Concepts:**
- Worktrees allow multiple branches checked out simultaneously
- Useful for parallel work without stashing
- Each worktree is independent
- Can work on bug while feature develops
- Improves productivity in complex projects
- Must remove worktrees when done

---

## Exercise 9: Hooks for Automation

**Objective:** Create Git hooks for automated tasks

**Instructions:**

1. **Navigate to Hooks Directory**
   ```bash
   cd .git/hooks
   ls -la
   # See example hooks
   ```

2. **Create Pre-Commit Hook**
   ```bash
   cat > pre-commit << 'EOF'
   #!/bin/bash
   echo "Running pre-commit checks..."
   
   # Check for .env files
   if git diff --cached --name-only | grep -E '\.env'; then
     echo "ERROR: Don't commit .env files!"
     exit 1
   fi
   
   # Check for console.log
   if git diff --cached | grep -E 'console\.log'; then
     echo "WARNING: Remove console.log statements before committing!"
     echo "Continue? (y/n)"
     read -r response
     if [ "$response" != "y" ]; then
       exit 1
     fi
   fi
   
   echo "Pre-commit checks passed!"
   EOF
   ```

3. **Make Hook Executable**
   ```bash
   chmod +x pre-commit
   ```

4. **Create Commit Message Hook**
   ```bash
   cat > commit-msg << 'EOF'
   #!/bin/bash
   commit_msg=$(cat "$1")
   
   # Check if message starts with type
   if ! echo "$commit_msg" | grep -E '^(feat|fix|docs|style|refactor|test|chore):'; then
     echo "ERROR: Commit message must start with: feat, fix, docs, style, refactor, test, or chore"
     exit 1
   fi
   
   echo "Commit message format valid!"
   EOF
   ```

5. **Make Commit Message Hook Executable**
   ```bash
   chmod +x commit-msg
   ```

6. **Test Hooks**
   ```bash
   cd ../..
   
   # Try invalid commit message
   echo "test" > hooktest.txt
   git add hooktest.txt
   git commit -m "invalid message"  # Should fail
   
   # Try valid format
   git commit -m "feat: Test hook functionality"  # Should succeed
   ```

7. **Create Post-Commit Hook**
   ```bash
   cd .git/hooks
   cat > post-commit << 'EOF'
   #!/bin/bash
   echo "Commit successful!"
   echo "Last commit info:"
   git log -1 --pretty=%B
   EOF
   chmod +x post-commit
   ```

8. **View Hook Execution**
   ```bash
   cd ../..
   echo "test2" > test2.txt
   git add test2.txt
   git commit -m "fix: Test post-commit hook"
   # See post-commit output
   ```

**Verification Checklist:**
- [ ] Pre-commit hook created and executable
- [ ] Pre-commit hook validates .env files
- [ ] Commit message hook checks format
- [ ] Invalid commits rejected by hooks
- [ ] Valid commits pass all hooks
- [ ] Post-commit hook displays information
- [ ] All hooks working as expected

**Key Concepts:**
- Hooks are scripts that run at Git events
- Prevent bad commits automatically
- Enforce team standards
- Pre-commit: runs before commit
- Commit-msg: validates message
- Post-commit: runs after successful commit
- Must be executable (chmod +x)

---

## Exercise 10: Advanced Workflow Integration

**Objective:** Combine all advanced concepts in realistic scenario

**Instructions:**

1. **Create Release Branch**
   ```bash
   git checkout -b release/v2.0.0
   ```

2. **Version Bump**
   ```bash
   echo "Version: 2.0.0" > VERSION
   git add VERSION
   git commit -m "chore: Bump version to 2.0.0"
   ```

3. **Create Release Notes**
   ```bash
   cat > RELEASE_NOTES.md << EOF
   # Version 2.0.0 Release Notes
   
   ## New Features
   - User authentication system
   - Real-time notifications
   - Advanced search capabilities
   
   ## Bug Fixes
   - Fixed memory leak in service
   - Improved performance by 40%
   - Security vulnerability patching
   
   ## Breaking Changes
   - API v1 deprecated (use v2)
   - Database schema changes
   - Configuration file format updated
   EOF
   
   git add RELEASE_NOTES.md
   git commit -m "docs: Add release notes for v2.0.0"
   ```

4. **Create Release Tag**
   ```bash
   git tag -a v2.0.0 -m "Release Version 2.0.0

   Major features:
   - Authentication system
   - Real-time notifications
   - Advanced search
   
   Breaking changes included."
   ```

5. **Merge Back to Main**
   ```bash
   git checkout main
   git merge --no-ff release/v2.0.0 -m "merge: Release v2.0.0"
   ```

6. **Handle Hotfix During Release**
   ```bash
   git checkout -b hotfix/critical-security-fix
   
   echo "Security patch applied" > security.md
   git add security.md
   git commit -m "fix: Critical security vulnerability"
   
   git checkout main
   git merge --no-ff hotfix/critical-security-fix
   
   git checkout release/v2.0.0
   git merge --no-ff hotfix/critical-security-fix
   ```

7. **Create Patch Release**
   ```bash
   git tag -a v2.0.1 -m "Patch Release v2.0.1 - Security fix"
   ```

8. **Push Everything**
   ```bash
   git push origin main
   git push origin release/v2.0.0
   git push origin --tags
   ```

9. **Create Release on GitHub**
   - Go to "Releases"
   - Create release from v2.0.0 tag
   - Add comprehensive release notes
   - Mark as "Latest release"
   - Attach any artifacts

10. **Cleanup**
    ```bash
    git branch -d release/v2.0.0
    git branch -d hotfix/critical-security-fix
    git push origin :release/v2.0.0  # Delete remote branch
    ```

**Verification Checklist:**
- [ ] Release branch created with version bump
- [ ] Release notes documented
- [ ] Release tag created with metadata
- [ ] Release merged back to main
- [ ] Hotfix handled and merged both places
- [ ] Patch tag created
- [ ] All tags pushed to GitHub
- [ ] Release published on GitHub
- [ ] Cleanup completed

**Key Concepts:**
- Release branches manage version releases
- Tags mark stable versions
- Hotfixes handled in parallel
- Merges back to both main and release branches
- GitHub Releases distribute versions
- Clean branching hygiene important

---

## Chapter 3 Challenge Project

**Objective:** Execute a complete release workflow

**Project:** Full Release Cycle Management

**Requirements:**

1. Create feature branch with multiple commits
2. Use interactive rebase to clean history
3. Cherry-pick hotfix commits to separate branch
4. Create semantic version tags
5. Use GitHub Actions for automation
6. Create detailed release notes
7. Publish release on GitHub
8. Tag version with release information
9. Handle concurrent hotfix scenario
10. Complete cleanup and documentation

**Success Criteria:**
- [ ] Clean feature branch history via rebase
- [ ] Selective commits applied via cherry-pick
- [ ] Proper semantic versioning
- [ ] Automated workflows executing
- [ ] Release published on GitHub
- [ ] Complete release documentation
- [ ] Proper branch management and cleanup

---

## Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| Interactive rebase conflicts | Resolve files, `git add`, `git rebase --continue` |
| Cherry-pick ends in conflict | Resolve conflict, `git cherry-pick --continue` |
| Lost tag | Check `git reflog` or local `.git/refs/tags` |
| Hook rejecting valid commit | Check hook script logic and permissions |
| Workflow not running | Check `.github/workflows` directory syntax |
| Bisect stuck | Use `git bisect reset` to exit |
| Worktree permission issues | Ensure proper directory permissions |

---

## Next Steps

Congratulations! You've completed all Chapter 3exercises! You now understand:
- ✅ Interactive rebase for history cleanup
- ✅ Cherry-picking selective commits
- ✅ Reset types and reflog recovery
- ✅ Advanced stashing techniques
- ✅ Semantic versioning and tags
- ✅ GitHub Actions automation
- ✅ Binary search debugging with bisect
- ✅ Parallel work with worktrees
- ✅ Git hooks for automation
- ✅ Complete release cycle management

**You have completed the entire 1-day Git & GitHub intensive course!**

---

## What's Next?

- **Apply these skills** to real projects
- **Contribute to open source** using these workflows
- **Teach others** what you've learned
- **Experiment with edge cases** to deepen knowledge
- **Explore advanced topics**: submodules, subtrees, and monorepo strategies

---

**[← Back to Chapter 3 Overview](./README.md)** | **[Return to Course Home](../../README.md)**
