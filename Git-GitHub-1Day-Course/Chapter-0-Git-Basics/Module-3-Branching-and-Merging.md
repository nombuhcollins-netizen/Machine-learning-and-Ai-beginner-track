# Chapter 0 - Module 3: Branching and Merging

**Duration:** 45 minutes | **Difficulty:** Intermediate

---

## Learning Objectives

By the end of this module, you will understand:

1. What branches are and why they're important
2. How to create and switch branches
3. How to merge branches
4. How to resolve merge conflicts
5. Best practices for branch management

---

## What is a Branch?

A **branch** is an independent line of development in your repository.

- Each branch can have different commits
- Branches allow multiple people to work on different features simultaneously
- The default branch is usually `master` or `main`

```
master:     A → B → C → D
                  ↓
feature:    A → B → E → F

bugfix:     A → B → G

# A & B are common history
# After B, branches diverge with different commits
```

---

## Why Use Branches?

✅ **Parallel Development** - Multiple features at once
✅ **Isolation** - Changes don't affect main code
✅ **Organization** - Keep features organized
✅ **Collaboration** - Team members work independently
✅ **Stability** - Main branch remains stable

---

## Branch Operations

### Creating Branches

#### `git branch`
List and create branches.

```bash
git branch                          # List local branches
git branch -a                       # List all branches (local + remote)
git branch feature-login            # Create new branch
git branch -d feature-login         # Delete branch
git branch -D feature-login         # Force delete branch
```

**Output Example:**
```
* master
  feature-login
  bugfix-123
```
(asterisk `*` marks current branch)

---

### Switching Branches

#### `git switch` (or `git checkout`)
Move to a different branch.

```bash
git switch master                   # Switch to master
git switch feature-login            # Switch to feature-login
git switch -c feature-new           # Create and switch in one command
```

---

## The Branching Workflow

```
1. Create branch from master
   git switch -c feature-login

   master:  A → B → C
            └─ feature-login: (empty)

2. Make commits on feature branch
   git add . && git commit -m "Add login form"
   git add . && git commit -m "Add validation"

   master:  A → B → C
            └─ feature-login: D → E

3. Switch back to master
   git switch master

4. Merge feature into master
   git merge feature-login

   master:  A → B → C → F (merge commit)
             \ D → E ↗
```

---

## Merging Branches

### `git merge`
Combines two branches.

```bash
git merge feature-login             # Merge feature-login into current branch
git merge feature-login -m "msg"    # Merge with custom message
git merge --squash feature-login    # Combine all commits into one
```

---

## Merge Scenarios

### Scenario 1: Fast-Forward Merge
When the target branch hasn't changed since the feature branch was created.

```
Before merge:
master:  A → B
         └─ feature: C → D

After merge (fast-forward):
master:  A → B → C → D
```

**Git command:**
```bash
git switch master
git merge feature
```

---

### Scenario 2: Three-Way Merge
When both branches have new commits.

```
Before merge:
master:  A → B → E
         └─ feature: C → D

After merge (creates merge commit):
master:  A → B → E → F (merge commit)
         └─ C → D ↗
```

**Git command:**
```bash
git switch master
git merge feature
```

Creates a merge commit automatically if there are no conflicts.

---

## Merge Conflicts

A **conflict** occurs when changes overlap and Git can't automatically determine which to keep.

### Conflict Example

**File during conflict:**
```
Login form
<<<<<<< HEAD
Email field (from master)
=======
Username field (from feature branch)
>>>>>>> feature-login

Password field
```

### Resolving Conflicts

1. **Identify conflicted files**
   ```bash
   git status
   # Shows: both added, both modified, etc.
   ```

2. **Edit the file** - Choose which changes to keep
   ```
   (Edit file to keep desired content)
   Login form
   Email field & Username field
   Password field
   ```

3. **Remove conflict markers** - Delete `<<<<<<<`, `=======`, `>>>>>>>`

4. **Stage the resolved file**
   ```bash
   git add login-form.html
   ```

5. **Complete the merge**
   ```bash
   git commit -m "Merge feature-login: resolve form field conflict"
   ```

---

## Branch Naming Conventions

Good naming helps team coordination:

```
feature/login-form           # New feature
bugfix/issue-123             # Bug fix
hotfix/production-error      # Urgent production fix
docs/update-readme           # Documentation
refactor/database-queries    # Code refactoring
```

---

## Exercises

### Exercise 1: Create and Switch Branches

**Objective:** Practice branch creation and switching

**Instructions:**
```bash
# Ensure you're in your repository
cd my-first-repo

# View current branch
git branch

# Create new branch
git branch feature-readme

# List branches
git branch

# Switch to new branch
git switch feature-readme

# Verify you're on correct branch
git branch

# Create and switch in one command
git switch -c feature-docs
```

**Expected Output:**
```
* feature-docs
  feature-readme
  master
```

**Verification Checklist:**
- [ ] Created feature-readme branch
- [ ] Created feature-docs branch
- [ ] Currently on feature-docs
- [ ] `git branch` shows all branches

---

### Exercise 2: Make Commits on Feature Branch

**Objective:** Practice isolated development on a branch

**Instructions:**
```bash
# Ensure you're on feature-docs
git switch feature-docs

# Create a README file
cat > README.md << 'EOF'
# My Project

This is my first Git project.

## Getting Started
1. Clone the repository
2. Read the documentation
EOF

# Stage and commit
git add README.md
git commit -m "Add README.md"

# Make another change
echo " " >> README.md
echo "## Usage" >> README.md
echo "TBD" >> README.md

# Commit again
git add README.md
git commit -m "Add usage section to README"

# View commits on this branch
git log --oneline
```

**Verification Checklist:**
- [ ] README.md created on feature-docs branch
- [ ] Two commits made
- [ ] `git log` shows commits with correct messages
- [ ] `git branch` confirms we're on feature-docs

---

### Exercise 3: Merge Branches

**Objective:** Practice merging feature branches into master

**Instructions:**
```bash
# View current branch (should be feature-docs)
git branch

# Switch to master
git switch master

# View master's content (no README yet)
ls -la | grep README

# Merge feature-docs
git merge feature-docs -m "Merge documentation branch"

# Verify the merge
ls -la | grep README
cat README.md

# View merged history
git log --oneline --graph
```

**Expected Output:**
```
*   abc1234 (HEAD -> master) Merge documentation branch
|\
| * def5678 Add usage section to README
| * ghi9012 Add README.md
|/
* jkl3456 Update hello.txt with more content
...
```

**Verification Checklist:**
- [ ] Switched to master successfully
- [ ] Merge completed without errors
- [ ] README.md exists on master
- [ ] Git log shows merge commit
- [ ] Both branches show in history graph

---

### Exercise 4: Create and Resolve a Merge Conflict

**Objective:** Practice handling merge conflicts

**Instructions:**

1. **Create conflicting branches**
   ```bash
   # On master, create a file
   echo "Version 1.0" > version.txt
   git add version.txt
   git commit -m "Add version.txt"
   ```

2. **Create feature branch**
   ```bash
   git switch -c feature-update
   echo "Version 2.0" > version.txt
   git add version.txt
   git commit -m "Update to 2.0"
   ```

3. **Make conflicting change on master**
   ```bash
   git switch master
   echo "Version 1.1" > version.txt
   git add version.txt
   git commit -m "Update to 1.1"
   ```

4. **Try to merge (will cause conflict)**
   ```bash
   git merge feature-update
   # Git will report: CONFLICT (content merge)
   ```

5. **View conflict**
   ```bash
   cat version.txt
   git status
   ```

6. **Resolve the conflict**
   ```bash
   # Edit version.txt to:
   # Version 2.0 (choosing feature version)
   ```

7. **Complete the merge**
   ```bash
   git add version.txt
   git commit -m "Resolve version conflict - use 2.0"
   git log --oneline --graph
   ```

---

## Branch Management Commands

| Command | Purpose |
|---------|---------|
| `git branch` | List branches |
| `git branch <name>` | Create branch |
| `git switch <branch>` | Switch branch |
| `git switch -c <branch>` | Create and switch |
| `git merge <branch>` | Merge branch |
| `git branch -d <branch>` | Delete branch (safe) |
| `git branch -D <branch>` | Force delete branch |

---

## Best Practices

✅ Create a branch for each feature or bugfix
✅ Use descriptive branch names
✅ Keep branches focused (one feature per branch)
✅ Delete branches after merging
✅ Review changes before merging
✅ Communicate with teammates about branch purposes

❌ Don't merge to master without review
❌ Don't work directly on master
❌ Don't keep stale branches

---

## Key Takeaways

✅ Branches enable parallel development
✅ Always create a feature branch for new work
✅ Merge when feature is complete
✅ Conflicts are normal and manageable
✅ Clear branch names improve team coordination

---

## Next Steps

You now understand local Git workflow! Ready to move to **Chapter 1** to learn about GitHub and remote collaboration.

---

**[← Back to Module 2](./Module-2-Basic-Commands.md)** | **[Next: Chapter 1 →](../Chapter-1-GitHub-Fundamentals/Module-0-GitHub-Basics.md)**
