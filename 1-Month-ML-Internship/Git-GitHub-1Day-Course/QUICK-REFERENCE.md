# Quick Reference Guide - Git & GitHub Commands

**Keep this handy while learning Git!**

---

## Table of Contents

1. [Configuration](#configuration)
2. [Repository Basics](#repository-basics)
3. [Staging & Committing](#staging--committing)
4. [Viewing History](#viewing-history)
5. [Branches](#branches)
6. [Remote Repositories](#remote-repositories)
7. [Merging & Rebasing](#merging--rebasing)
8. [Stashing](#stashing)
9. [Tagging](#tagging)
10. [Advanced](#advanced)

---

## Configuration

```bash
# Set user info (do this first!)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# View configuration
git config --list
git config user.name

# Change/override locally
git config --local user.name "Different Name"
```

---

## Repository Basics

```bash
# Create new repository
git init

# Clone existing repository
git clone https://github.com/user/repo.git
git clone https://github.com/user/repo.git my-folder

# Check status
git status
git status -s  # Short format
```

---

## Staging & Committing

```bash
# Stage files
git add file.txt           # Stage specific file
git add .                  # Stage all changes
git add *.html             # Stage pattern match
git add -A                 # Stage all (including deletions)

# Unstage files
git restore --staged file.txt
git reset file.txt

# Commit
git commit -m "Commit message"
git commit --amend         # Modify last commit
git commit -am "msg"       # Add tracked files + commit

# View changes before committing
git diff                   # Unstaged changes
git diff --staged          # Staged changes
```

---

## Viewing History

```bash
# View commits
git log                    # Full log
git log --oneline          # One line per commit
git log -n 5               # Last 5 commits
git log -p                 # With full diffs
git log --graph --all      # Visual branch graph

# View specific commit
git show <hash>            # Full details
git show <hash>:file.txt   # File contents at commit

# View specific file history
git log file.txt           # Commits affecting file
git log -p file.txt        # Changes to file

# Blame (who changed what)
git blame file.txt         # Line by line
```

---

## Branches

```bash
# List branches
git branch                 # Local only
git branch -a              # All (local + remote)
git branch -v              # With last commit

# Create branches
git branch feature-name
git switch -c feature-name # Create and switch

# Switch/checkout
git switch main            # Switch branch
git switch -                # Switch to previous branch
git checkout main          # (older syntax)

# Rename branch
git branch -m old-name new-name
git branch -M main         # Force rename

# Delete branches
git branch -d feature-name # Safe delete
git branch -D feature-name # Force delete

# See merged branches
git branch --merged        # Already merged
git branch --no-merged     # Not yet merged
```

---

## Remote Repositories

```bash
# Manage remotes
git remote                 # List remotes
git remote -v              # With URLs
git remote add origin <url>
git remote set-url origin <new-url>
git remote remove origin
git remote show origin     # Details about remote

# Fetch vs Pull
git fetch                  # Download, don't merge
git fetch origin           # Specific remote
git pull                   # Fetch + merge
git pull --rebase          # Fetch + rebase

# Push
git push                   # Push to default
git push origin main       # Specific branch
git push -u origin main    # Set upstream
git push origin branch-name
git push --all             # All branches
git push origin --delete branch  # Delete remote branch

# Tracking branches
git branch -u origin/main  # Set tracking
git branch --vv            # View tracking status
```

---

## Merging & Rebasing

```bash
# Merge
git merge branch-name      # Merge into current
git merge --no-ff branch   # Create merge commit
git merge --squash branch  # Squash commits

# Rebase
git rebase main            # Rebase onto main
git rebase -i HEAD~3       # Interactive rebase 3 commits

# During merge/rebase conflict
git status                 # See conflicts
# Edit files to resolve
git add resolved-file.txt
git commit                 # Complete merge
git rebase --continue      # Continue rebase

# Abort merge/rebase
git merge --abort
git rebase --abort
```

---

## Undoing Changes

```bash
# Discard changes
git restore file.txt       # Undo file changes
git restore .              # Undo all changes
git restore --staged file.txt  # Unstage file

# Undo commits
git revert <hash>          # Create undo commit
git reset --soft HEAD~1    # Undo commit, keep changes staged
git reset --mixed HEAD~1   # Undo commit, keep changes unstaged
git reset --hard HEAD~1    # Undo commit, discard changes fully
```

⚠️ **Never use `--hard` on shared branches!**

---

## Stashing

```bash
# Create stash
git stash                  # Stash all
git stash save "message"   # With message
git stash push -m "msg"    # Alternative

# List stashes
git stash list

# Apply stash
git stash apply            # Apply most recent
git stash apply stash@{1}  # Apply specific
git stash pop              # Apply and remove

# Delete stash
git stash drop             # Delete most recent
git stash drop stash@{1}   # Delete specific
git stash clear            # Delete all
```

---

## Tagging

```bash
# Create tags
git tag v1.0.0             # Lightweight tag
git tag -a v1.0.0 -m "Release 1.0"  # Annotated

# List tags
git tag                    # All tags
git tag -l "v1.*"          # Pattern match
git tag -l -n              # With messages

# View tag
git show v1.0.0

# Delete tags
git tag -d v1.0.0          # Local
git push origin --delete v1.0.0  # Remote

# Push tags
git push origin v1.0.0     # Single tag
git push origin --tags     # All tags
```

---

## Advanced

```bash
# Cherry-pick (apply specific commit)
git cherry-pick <hash>     # Apply commit to current branch

# Reflog (recovery)
git reflog                 # Show all operations
git reset --hard <ref>     # Reset to point in reflog

# Search history
git log -S "search text"   # Commits with text
git log --author="name"    # Commits by author
git log --since="2 weeks ago"  # Recent commits

# Bisect (find bug)
git bisect start
git bisect bad HEAD
git bisect good v1.0
# ... narrow down

# Grep (search codebase)
git grep "search term"     # Search in files

# Show diff between versions
git diff v1.0 v2.0
git diff branch1 branch2
```

---

## Workflow Examples

### Feature Branch Workflow

```bash
# Start new feature
git switch -c feature-login
# ... make commits ...
git push -u origin feature-login

# Create PR on GitHub, get review

# Address feedback
# ... make commits ...
git push

# Merge when approved
# Delete branch
git branch -d feature-login
```

### Fixing Mistakes

```bash
# Oops, committed on wrong branch
git reflog                 # Find commit hash
git reset --soft abc123    # Move commit to staging
git switch correct-branch
git commit -m "Right message"

# Oops, committed to main directly
git reset HEAD~1           # Undo last commit
git stash                  # Save changes
git switch -c feature-fix
git stash pop
git commit -m "Fix"
git switch main
git merge feature-fix
```

---

## Git Tips & Tricks

```bash
# Short status
git status -s

# Ammend last commit
git commit --amend

# Stage hunks interactively
git add -p

# Undo last n commits
git reset --hard HEAD~n

# Revert last commit (safe)
git revert HEAD

# See what will be deleted
git clean -n

# View current branch in terminal
# Add to your shell prompt: $(git branch --show-current)

# Ignore whitespace
git diff -w

# Find large files
git ls-files -z | xargs -0 du -sh | sort -rh | head -20
```

---

## Common Workflows

### Before Creating Pull Request

```bash
git switch feature-branch
git fetch origin
git rebase origin/main
git push -f
# Now create PR
```

### Cleaning Up Local Branches

```bash
# Delete all local branches except current
git branch | grep -v '\*' | xargs git branch -d

# List branches to be deleted
git branch --merged main | grep -v "main"
```

### Update Branch with Main Changes

```bash
git fetch origin
git rebase origin/main
# or
git merge origin/main
```

---

## Helpful Aliases

Add to `~/.gitconfig` or use `git config --global`:

```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'restore --staged'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --all'
```

Then use:
```bash
git st          # instead of git status
git co feature  # instead of git switch feature
git ci -m "msg" # instead of git commit -m "msg"
```

---

## Useful .gitignore Patterns

```
# Python
__pycache__/
*.py[cod]
*$py.class
venv/
.venv/
*.egg-info/
dist/
build/

# Node.js
node_modules/
npm-debug.log
yarn-error.log

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local
.env.*.local

# Temporary
temp/
tmp/
*.tmp
*.bak

# Dependencies (can be reinstalled)
vendor/
lib/
```

---

## Emergency Commands

**Warning:** Use with caution!

```bash
# Find lost commits
git reflog
git log --all --oneline --decorate

# Recover deleted branch
git reflog                 # Find branch tip
git switch -c branch-name <hash>

# Undo accidental reset
git reflog
git reset --hard OLD_HEAD

# View all branches (including deleted)
git branch -a
git reflog show --all
```

---

## Need Help?

```bash
# Man pages
git help <command>
git <command> --help

# Quick help
git --help

# List all commands
git help

# Examples in terminal
git log --help
man git-log
```

---

## Remember

| Concept | Key Rule |
|---------|----------|
| **Commit** | Save frequently |
| **Branch** | One feature per branch |
| **Push** | Push before switching machines |
| **Pull** | Pull before starting work |
| **Review** | Code review improves quality |
| **Rebase** | Only on personal branches |
| **Tags** | Mark releases, use semantic versioning |
| **Stash** | Temporary, not for storage |

---

## Keyboard Shortcuts (In Terminal)

```
Ctrl+C         Cancel current operation
Ctrl+D         Exit (in text editors)
Ctrl+Z         Suspend command
Tab            Auto-complete
Up Arrow       Previous command
Down Arrow     Next command
```

---

## Git One-Liners

Save time with these:

```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# See who changed a line
git blame file.txt

# Find commits that touch a function
git log -S"FunctionName" -p

# Squash last 5 commits
git rebase -i HEAD~5

# Revert a public commit
git revert abc123

# Get someone's PR locally
git fetch origin pull/PR_NUMBER/head:BRANCH_NAME
```

---

## Version Control Best Practices

✅ Commit frequently
✅ Write clear messages
✅ Keep commits atomic (one idea)
✅ Pull before working
✅ Push regularly
✅ Review before merging
✅ Use issues to track work
✅ Tag releases
✅ Keep main stable

❌ Don't push without testing
❌ Don't force-push shared branches
❌ Don't commit secrets
❌ Don't commit large binaries
❌ Don't ignore conflicts

---

## Troubleshooting Guide

| Problem | Solution |
|---------|----------|
| Can't push | `git pull` first, then `git push` |
| Merge conflict | Edit files, `git add`, `git commit` |
| Wrong branch | `git switch correct-branch` |
| Wrong commit message | `git commit --amend` |
| Lost commits | `git reflog` to find them |
| Huge .git folder | `git gc --aggressive` |
| Wrong remote URL | `git remote set-url origin <new-url>` |

---

## GitHub PR Lifecycle

```
1. Create branch
   git switch -c feature-X
   
2. Make changes & commits
   git add .
   git commit -m "..."
   
3. Push branch
   git push -u origin feature-X
   
4. Create PR on GitHub
   
5. Get review & feedback
   
6. Make changes
   git add .
   git commit -m "Address feedback"
   git push
   
7. Approve & merge
   PR merged on GitHub
   
8. Cleanup
   git switch main
   git pull
   git branch -d feature-X
```

---

## Keep Learning

- Read Pro Git book (free online)
- Practice daily
- Try challenging scenarios
- Help others
- Review others' code

---

**Print this guide or bookmark it! Reference it whenever you git confused 😉**

---

**[← Back to Course Overview](./README.md)**
