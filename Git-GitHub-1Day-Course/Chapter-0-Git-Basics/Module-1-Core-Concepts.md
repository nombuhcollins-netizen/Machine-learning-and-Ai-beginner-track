# Chapter 0 - Module 1: Core Concepts

**Duration:** 30 minutes | **Difficulty:** Beginner

---

## Learning Objectives

By the end of this module, you will understand:

1. The Git workflow and its stages
2. How Git stores information
3. The three main areas: Working Directory, Staging Area, and Repository
4. How commits work

---

## The Three Areas of Git

### 1. Working Directory
- Your local folder where you edit files
- Contains the project files you're actively working on
- Changes haven't been tracked yet

### 2. Staging Area (Index)
- Temporary area for changes you want to commit
- You choose which changes to include
- Also called the "staging area" or "index"

### 3. Repository
- Contains all committed changes and history
- Stored in the `.git` folder
- Includes all branches and commits

---

## The Git Workflow

```
┌─────────────────────────────────────────────────────────┐
│                   Your Project                          │
│                   (Working Directory)                   │
│                                                         │
│  ┌────────────┐  ┌──────────────┐  ┌────────────────┐ │
│  │  Modified  │→→│ Staged Files  │→→│   Committed   │ │
│  │   Files    │  │ (Staging Area)│  │  History      │ │
│  │            │  │               │  │ (.git folder) │ │
│  └────────────┘  └──────────────┘  └────────────────┘ │
│      git add  →      git commit →                      │
└─────────────────────────────────────────────────────────┘
```

---

## Key Concepts

### Commit
A **commit** is a snapshot of your project at a specific point in time. It includes:
- Changes (diff)
- Author information
- Timestamp
- Commit message
- Parent commit reference

### Hash
Every commit has a unique identifier (hash/SHA-1):
```
a3f4d7e9c8b2e1f6a4c5d8e9f0b1c2d3
```

### HEAD
A **pointer** that indicates your current location in the repository:
- Usually points to the current branch
- Moves when you switch branches or commit

---

## Git State Example

**Stage 1: Initial State**
```
Working Directory:
├── file1.txt (unchanged)
└── file2.txt (unchanged)

Staging Area: (empty)

Repository: 
└── Add (initial commit)
```

**Stage 2: Make Changes**
```
Working Directory:
├── file1.txt (modified)
└── file2.txt (new file)

Staging Area: (empty)

Repository: 
└── Add (initial commit)
```

**Stage 3: Stage Changes**
```
Working Directory:
├── file1.txt (modified)
└── file2.txt (new file)

Staging Area:
├── file1.txt (changes)
└── file2.txt (new)

Repository: 
└── Add (initial commit)
```

**Stage 4: Commit**
```
Working Directory: (clean)

Staging Area: (empty)

Repository: 
├── Add (initial commit)
└── Commit 123: Add file2.txt and update file1.txt
```

---

## Exercises

### Exercise 1: Understand Git Areas

**Objective:** Conceptually understand the three areas

**Instructions:**
1. Create a mental model of the three areas
2. Draw a diagram showing the flow: Working Directory → Staging Area → Repository
3. Explain each area in your own words

**Expected Outcome:**
You can explain what happens in each area and why separation is useful (selective commits, review changes before committing).

---

### Exercise 2: Initialize Your First Repository

**Objective:** Create a local Git repository

**Commands:**
```bash
# Create a new directory
mkdir my-first-repo
cd my-first-repo

# Initialize Git repository
git init

# Check status
git status
```

**Expected Output:**
```
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

**Verification Checklist:**
- [ ] Directory created
- [ ] `git init` executed successfully
- [ ] `.git` folder exists (use `ls -la` or `dir /a`)
- [ ] `git status` shows initial state

---

### Exercise 3: Create and Stage Files

**Objective:** Practice the add/commit workflow

**Commands:**
```bash
# Create a file
echo "Hello Git!" > hello.txt

# Check status (should show "Untracked files")
git status

# Stage the file
git add hello.txt

# Check status again (should show "Changes to be committed")
git status

# Commit the file
git commit -m "Add hello.txt"

# Check status (should show "nothing to commit")
git status

# View commit log
git log
```

**Expected Output After Last Command:**
```
commit abc123def456 (HEAD -> master)
Author: Your Name <your.email@example.com>
Date:   [timestamp]

    Add hello.txt
```

**Verification Checklist:**
- [ ] File created
- [ ] File staged successfully
- [ ] Commit created
- [ ] Commit message is clear
- [ ] `git log` shows your commit

---

## Key Takeaways

✅ Git has three distinct areas: Working Directory, Staging Area, Repository
✅ A commit is a snapshot of your project
✅ Staging allows selective commits
✅ Each commit has a unique hash identifier
✅ HEAD points to your current location

---

## Common Commands Reference

```bash
git init                    # Initialize repository
git status                  # Check status
git add <file>              # Stage file
git add .                   # Stage all changes
git commit -m "message"     # Commit staged changes
git log                     # View commit history
```

---

## Next Steps

Your repository has history! In **Module 2**, you'll learn more commands to manage your code effectively.

---

**[← Back to Module 0](./Module-0-Introduction-and-Installation.md)** | **[Next: Module 2 →](./Module-2-Basic-Commands.md)**
