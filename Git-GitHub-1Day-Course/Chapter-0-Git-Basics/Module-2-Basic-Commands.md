# Chapter 0 - Module 2: Basic Commands

**Duration:** 40 minutes | **Difficulty:** Beginner

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use essential Git commands for daily work
2. View and understand commit history
3. Understand differences between versions
4. Navigate your repository history

---

## Essential Git Commands

### Repository Status

#### `git status`
Shows the current state of your repository.

```bash
git status
# Output: 
# On branch master
# Changes not staged for commit:
#   modified: file.txt
# Untracked files:
#   newfile.txt
```

**When to use:** After making changes, before staging

---

### Staging and Committing

#### `git add`
Stages files for commit.

```bash
git add file.txt              # Stage specific file
git add .                     # Stage all changes
git add *.txt                 # Stage files matching pattern
git add -A                    # Stage all (including deletions)
```

#### `git commit`
Creates a snapshot of staged changes.

```bash
git commit -m "Fix login bug"                    # With message
git commit                                        # Opens editor
git commit --amend                                # Modify last commit
git commit -am "Update file"                      # Add + commit tracked files
```

---

### Viewing History

#### `git log`
Shows commit history.

```bash
git log                          # Full log
git log --oneline               # Condensed view
git log -n 5                     # Last 5 commits
git log --graph --all --decorate # Visual branch history
git log --author="Name"         # Commits by author
git log --since="2 weeks ago"   # Recent commits
```

**Output Example:**
```
commit a1b2c3d4 (HEAD -> master)
Author: John Doe <john@example.com>
Date:   Wed Feb 19 10:30:00 2026 +0000

    Fix login validation
```

---

#### `git show`
Shows detailed information about a commit.

```bash
git show                        # Current commit (HEAD)
git show a1b2c3d4              # Specific commit
git show a1b2c3d4:file.txt     # File contents at commit
```

---

### Comparing Changes

#### `git diff`
Shows differences between versions.

```bash
git diff                        # Working directory vs staging area
git diff --staged              # Staging area vs repository
git diff HEAD~1                # Current vs previous commit
git diff branch1 branch2       # Between two branches
```

**Output Example:**
```
diff --git a/file.txt b/file.txt
index abc..def 100644
--- a/file.txt
+++ b/file.txt
@@ -1,3 +1,3 @@
 Hello
-Old line
+New line
 World
```

---

### Undoing Changes

#### `git restore` (or `git checkout`)
Discard changes in working directory.

```bash
git restore file.txt            # Discard changes in file
git restore .                   # Discard all changes
git restore --staged file.txt   # Unstage file
```

#### `git revert`
Create a new commit that undoes changes.

```bash
git revert a1b2c3d4            # Undo specific commit
git revert HEAD                 # Undo last commit
```

---

### Working with History

#### `git reset`
Move HEAD to different commit (use with caution!).

```bash
git reset --soft HEAD~1        # Undo last commit, keep changes staged
git reset --mixed HEAD~1       # Undo last commit, keep changes unstaged
git reset --hard HEAD~1        # Undo last commit, discard changes
```

⚠️ **Warning:** `--hard` discards changes permanently!

---

## Exercise 1: Practice Basic Commands

**Objective:** Master the essential Git commands

**Setup:**
```bash
cd my-first-repo  # From previous module
```

**Steps:**

1. **Check Status**
   ```bash
   git status
   ```

2. **Create and Modify Files**
   ```bash
   echo "Feature 1" > feature1.txt
   echo "Feature 2" > feature2.txt
   
   # Modify existing file
   echo "Hello Git updated!" > hello.txt
   ```

3. **View Changes**
   ```bash
   git status
   git diff hello.txt
   ```

4. **Stage Selectively**
   ```bash
   git add hello.txt feature1.txt
   git status
   ```

5. **View Staged Changes**
   ```bash
   git diff --staged
   ```

6. **Commit**
   ```bash
   git commit -m "Add feature1 and update hello.txt"
   ```

7. **View History**
   ```bash
   git log
   git log --oneline
   ```

8. **View Specific Commit**
   ```bash
   git show HEAD
   ```

---

## Exercise 2: Explore Differences

**Objective:** Understand how to compare versions

**Steps:**

1. **Modify a File**
   ```bash
   echo "More content" >> hello.txt
   ```

2. **View Unstaged Changes**
   ```bash
   git diff hello.txt
   ```

3. **Stage the Change**
   ```bash
   git add hello.txt
   ```

4. **View Staged Changes**
   ```bash
   git diff --staged
   ```

5. **Create Another Commit**
   ```bash
   git commit -m "Update hello.txt with more content"
   ```

6. **Compare Two Commits**
   ```bash
   git log --oneline       # Note commit hashes
   git show <first-commit-hash>
   git diff <first-hash> <second-hash>
   ```

---

## Exercise 3: Undo Changes

**Objective:** Learn to undo mistakes safely

**Steps:**

1. **Make a Mistake**
   ```bash
   echo "Oops, wrong content" > feature1.txt
   ```

2. **View the Mistake**
   ```bash
   git diff feature1.txt
   ```

3. **Restore the File**
   ```bash
   git restore feature1.txt
   git diff feature1.txt       # Should show no changes
   ```

4. **Verify History**
   ```bash
   git log
   cat feature1.txt            # Should have original content
   ```

---

## Command Quick Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `git status` | View current state | `git status` |
| `git add` | Stage changes | `git add .` |
| `git commit` | Create snapshot | `git commit -m "msg"` |
| `git log` | View history | `git log --oneline` |
| `git show` | View commit details | `git show HEAD` |
| `git diff` | Compare versions | `git diff HEAD~1` |
| `git restore` | Discard changes | `git restore file.txt` |
| `git revert` | Undo commit | `git revert HEAD` |

---

## Key Takeaways

✅ `git status` is your best friend - use it often
✅ Commit messages should be clear and descriptive
✅ `git log` helps you understand project history
✅ `git diff` shows exactly what changed
✅ Use `git restore` to safely undo changes
✅ Never use `git reset --hard` on shared branches

---

## Common Mistakes

| Mistake | Solution |
|---------|----------|
| Committed something by mistake | `git revert <commit-hash>` |
| Staged wrong file | `git restore --staged file.txt` |
| Wrong commit message | `git commit --amend -m "New message"` |
| Forgot to add a file | `git add file.txt` then `git commit --amend` |

---

## Next Steps

You've mastered the basics! Next, learn about **branches** - one of Git's most powerful features.

---

**[← Back to Module 1](./Module-1-Core-Concepts.md)** | **[Next: Module 3 →](./Module-3-Branching-and-Merging.md)**
