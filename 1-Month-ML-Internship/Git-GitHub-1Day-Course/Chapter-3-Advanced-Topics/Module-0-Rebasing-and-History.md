# Chapter 3 - Module 0: Rebasing & History Management

**Duration:** 30 minutes | **Difficulty:** Intermediate

---

## Learning Objectives

By the end of this module, you will be able to:

1. Understand rebasing vs merging
2. Use `git rebase` to update branches
3. Perform interactive rebasing
4. Squash commits for clean history
5. Rewrite commit history safely
6. Clean up commits before merging

---

## Rebasing vs Merging

### Merging

Creates a **merge commit** combining two branches.

```
Before merge:
main:     A → B → C
            └─ feature: D → E

After git merge feature:
main:     A → B → C → M (merge commit)
            \ D → E ↗
```

**Pros:**
- Clear history of when merge happened
- Safe, preserves all commits
- Easy to understand

**Cons:**
- History becomes tangled with large teams
- Merge commits can clutter log

### Rebasing

**Re-applies** commits on top of new base.

```
Before rebase:
main:     A → B → C
            └─ feature: D → E

After git rebase main:
main:     A → B → C
                   └─ feature: D' → E'
                   (D and E replayed on C)

After git merge feature:
main:     A → B → C → D' → E'
        (clean linear history)
```

**Pros:**
- Clean, linear history
- Easy to follow code evolution
- Looks like features were done serially

**Cons:**
- Rewrites history (dangerous on shared branches)
- More complex for beginners
- Can confuse team members

---

## When to Rebase

### Safe to Rebase

✅ Personal/local feature branches (not shared)
✅ Before creating PR (clean history)
✅ Moving commits to correct branch
✅ Updating feature branch with main changes

### NOT Safe to Rebase

❌ Shared branches (team is using it)
❌ Main/master branch
❌ Public repositories
❌ After publishing commits others depend on

---

## Rebasing Commands

### `git rebase`

Rebase current branch onto another.

```bash
git rebase main              # Rebase onto main
git rebase main feature      # Rebase feature onto main
git rebase -i HEAD~3         # Interactive rebase last 3 commits
```

### Process

1. **Identify commits** to replay
2. **Find new base**
3. **Re-apply commits** one by one
4. **Resolve conflicts** if needed

---

## Interactive Rebasing

**`git rebase -i`** gives control over each commit.

### Setup

```bash
git rebase -i HEAD~3
# Shows editor with last 3 commits
```

### Editor Display

```
pick a1b2c3d Add login form
pick d4e5f6g Add password validation
pick h7i8j9k Update requirements.txt

# Commands:
# p, pick = use commit
# r, reword = use commit, but edit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous
# f, fixup = like squash, but discard this commit's log message
# x, exec = run command (the rest of the line) using shell
```

### Common Operations

#### Squash (Combine Commits)

```
Before (3 commits):
pick a1b2c3d Add login form
pick d4e5f6g Fix typo
pick h7i8j9k Another fix

After (change to):
pick a1b2c3d Add login form
squash d4e5f6g Fix typo
squash h7i8j9k Another fix

Result: 1 commit with all changes
```

#### Reorder Commits

```
Before:
pick a1b2c3d Feature A
pick d4e5f6g Feature B

After (reorder):
pick d4e5f6g Feature B
pick a1b2c3d Feature A

Result: Commits in different order
```

#### Drop/Remove Commit

```
Before:
pick a1b2c3d Keep this
pick d4e5f6g Remove this
pick h7i8j9k Keep this

After (change to):
pick a1b2c3d Keep this
drop d4e5f6g Remove this
pick h7i8j9k Keep this

Result: Middle commit removed
```

#### Edit Message

```
Before:
pick a1b2c3d bad message

After (change to):
reword a1b2c3d bad message

Git stops and lets you edit the message
```

---

## Conflict Resolution During Rebase

### When Conflicts Occur

```
$ git rebase main
# Git tries to apply commits
# ERROR: Conflict in file.txt
# Rebasing halted
```

### Resolve

1. **Edit conflicted files**
   ```
   Mark conflicts as resolved
   git add file.txt
   ```

2. **Continue rebase**
   ```bash
   git rebase --continue
   ```

3. **Or abort**
   ```bash
   git rebase --abort  # Back to original state
   ```

---

## Rebase Workflow for PRs

**Clean feature branch before merging:**

```bash
# Start on feature branch
git switch feature-login

# Rebase onto latest main
git fetch origin
git rebase origin/main

# Resolve any conflicts if needed
# ...

# Force push (only on personal branches!)
git push -f

# PR now has clean history with main changes
```

---

## Squashing Commits

**Combine multiple commits into one.**

### Scenario

You made 5 commits to fix one feature:

```
a1b2c3d Initial implementation
d4e5f6g Fix typo
h7i8j9k Add missing function
i1j2k3l Fix function name
m4n5o6p Update tests
```

### Squash Before Merging

```bash
git rebase -i HEAD~5
# Change all to 's' (squash) except first to 'p' (pick)

# Save, then edit combined message
```

### Result

```
New commit with all changes combined
```

---

## Exercises

### Exercise 1: Rebase Feature Branch

**Objective:** Update feature branch with main changes

**Prerequisites:**
- feature branch with commits
- main branch has new commits

**Instructions:**

1. **Ensure feature branch**
   ```bash
   git switch feature-example
   git log --oneline -n 3
   ```

2. **Make sure main is updated**
   ```bash
   git fetch origin
   # or if local-only:
   git switch main
   git pull
   git switch feature-example
   ```

3. **Rebase feature onto main**
   ```bash
   git rebase main
   ```

4. **Check result**
   ```bash
   git log --oneline -n 5
   # Should show feature commits after main commits
   ```

5. **Push (force if shared branch)**
   ```bash
   git push origin feature-example
   # If branch was already pushed:
   # git push -f  (force push - dangerous!)
   ```

**Verification Checklist:**
- [ ] Feature branch rebased successfully
- [ ] No conflicts
- [ ] Commits appear in correct order
- [ ] Changes pushed to GitHub

---

### Exercise 2: Interactive Rebase to Clean Commits

**Objective:** Clean up messy commit history

**Instructions:**

1. **Create multiple commits to clean up**
   ```bash
   git switch -c feature-cleanup
   
   echo "Line 1" > file1.txt
   git add file1.txt
   git commit -m "Add file1"
   
   echo "Line 2" >> file1.txt
   git add file1.txt
   git commit -m "Fix typo"
   
   echo "Line 3" >> file1.txt
   git add file1.txt
   git commit -m "Update content"
   ```

2. **View commits**
   ```bash
   git log --oneline -n 3
   ```

3. **Interactive rebase**
   ```bash
   git rebase -i HEAD~3
   ```

4. **In editor:**
   ```
   Change to:
   pick a1b2c3d Add file1
   squash b2c3d4e Fix typo
   squash c3d4e5f Update content
   ```

5. **Save (depends on editor)**
   - Vim: `:wq`
   - Nano: Ctrl+X, then Y, then Enter

6. **Edit combined commit message**
   ```
   Add file1 with content

   - Initial implementation
   - Fixed typo
   - Updated content
   ```

7. **Verify result**
   ```bash
   git log --oneline -n 1
   # Should show 1 commit instead of 3
   ```

**Verification Checklist:**
- [ ] Multiple commits created
- [ ] Interactive rebase executed
- [ ] Commits squashed successfully
- [ ] Combined message makes sense

---

### Exercise 3: Reword Commit Message

**Objective:** Fix existing commit messages

**Instructions:**

1. **Create commit with bad message**
   ```bash
   echo "important changes" > important.txt
   git add important.txt
   git commit -m "asdfgh"
   ```

2. **Interactive rebase**
   ```bash
   git rebase -i HEAD~1
   ```

3. **In editor:**
   ```
   Change from:
   pick a1b2c3d asdfgh
   
   To:
   reword a1b2c3d asdfgh
   ```

4. **Save editor**

5. **In next editor, fix message**
   ```
   Remove: asdfgh
   Add: Add important changes file
   ```

6. **Verify**
   ```bash
   git log --oneline -n 1
   # Should show: Add important changes file
   ```

**Verification Checklist:**
- [ ] Commit message reworded
- [ ] New message is clear
- [ ] Log shows updated message

---

## Important Safety Rules

⚠️ **Never rebase:**
- main branch
- Shared branches (others using it)
- Commits already pushed to shared repo
- Work others depend on

✅ **Safe to rebase:**
- Personal feature branches
- Before creating PR
- Commits not yet shared

---

## Rebase Command Reference

| Command | Purpose |
|---------|---------|
| `git rebase main` | Rebase on main |
| `git rebase -i HEAD~n` | Interactive rebase n commits |
| `git rebase --continue` | Continue after conflict |
| `git rebase --abort` | Cancel rebase |
| `git push -f` | Force push rebased commits |

---

## Key Takeaways

✅ Rebase creates linear history
✅ Interactive rebase gives fine-grained control
✅ Squashing combines commits
✅ Only rebase personal branches
✅ Always clean before merging to main
✅ Conflicts during rebase are handled like merge conflicts

---

## When to Use Rebase

**YES:**
- Cleaning feature branch before PR
- Updating feature with main changes
- Fixing commit messages
- Squashing noisy commits

**NO:**
- main branch
- Shared branches
- Published commits

---

## Next Steps

You've mastered clean history management! **Module 1** covers stashing and tagging for organizing work.

---

**[← Back to Chapter 3 Overview](./README.md)** | **[Next: Module 1 →](./Module-1-Stashing-and-Tags.md)**
