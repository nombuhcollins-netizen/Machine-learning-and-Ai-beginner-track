# Chapter 1 - Module 1: Remote Operations

**Duration:** 30 minutes | **Difficulty:** Beginner

---

## Learning Objectives

By the end of this module, you will be able to:

1. Understand what a remote repository is
2. Connect local repository to GitHub
3. Push changes to remote
4. Pull changes from remote
5. Manage remote branches
6. Synchronize between local and remote

---

## What is a Remote?

A **remote** is a Git repository hosted on a server (usually GitHub).

- **Local:** Repository on your computer
- **Remote:** Repository on GitHub (or another server)
- **Origin:** Default name for your primary remote

```
Your Computer              GitHub
┌──────────────┐           ┌──────────────┐
│ Local Repo   │ ← Push →  │ Remote Repo  │
│              │ ← Pull ←  │ (Origin)     │
└──────────────┘           └──────────────┘
```

---

## Remote Commands

### `git remote`

Lists and manages remotes.

```bash
git remote                          # List remotes
git remote -v                       # List with URLs (verbose)
git remote add <name> <url>         # Add new remote
git remote set-url origin <new-url> # Change URL
git remote remove <name>            # Remove remote
git remote show <name>              # Show details
```

**Example output:**
```
origin  git@github.com:username/repo.git (fetch)
origin  git@github.com:username/repo.git (push)
```

---

## Pushing to Remote

### `git push`

Uploads your local commits to remote.

```bash
git push                            # Push to default remote
git push origin master              # Push to specific branch
git push origin feature-1           # Push feature branch
git push --all                      # Push all branches
git push origin --delete branch     # Delete remote branch
```

---

## Pulling from Remote

### `git pull`

Downloads remote changes and merges them locally.

```bash
git pull                            # Pull from default remote
git pull origin master              # Pull specific branch
git pull --rebase                   # Rebase instead of merge
```

---

## Setting Up Tracking Branches

### Push with Upstream

The `-u` flag sets up tracking:

```bash
git push -u origin master
# Same as:
git push --set-upstream origin master
```

Once tracking is set:
- `git push` = `git push origin master`
- `git pull` = `git pull origin master`

---

## The Full Push/Pull Setup

### First Time: Connect Local to Remote

1. **Create repository on GitHub** (you did this!)

2. **In local repository, add remote:**
   ```bash
   git remote add origin https://github.com/username/repo.git
   # or use SSH:
   git remote add origin git@github.com:username/repo.git
   ```

3. **Verify connection:**
   ```bash
   git remote -v
   ```

4. **Push with upstream tracking:**
   ```bash
   git push -u origin master
   # or if default branch is 'main':
   git push -u origin main
   ```

5. **Verify on GitHub:**
   - Visit your repository on github.com
   - You should see your files!

### Subsequent Times: Regular Workflow

```bash
# Make changes locally
git add .
git commit -m "message"

# Push changes
git push

# Others make changes on GitHub or another computer
# Pull those changes
git pull

# Continue working...
```

---

## Fetch vs Pull

### `git fetch`
Downloads remote changes but doesn't merge them.

```bash
git fetch                           # Fetch all remotes
git fetch origin                    # Fetch specific remote
```

Use when you want to see changes before merging.

### `git pull`
Fetches AND merges in one command.

```bash
git pull                            # = git fetch + git merge
git pull --rebase                   # = git fetch + git rebase
```

---

## Remote Branches

### View Remote Branches

```bash
git branch -r                       # View remote branches
git branch -a                       # View all (local + remote)
```

### Track Remote Branch

```bash
git switch --track origin/feature-1
# Creates local branch tracking remote
```

---

## Common Workflows

### Workflow 1: Solo Developer

```bash
# Day 1: Initial setup
git remote add origin https://...
git push -u origin main

# Day 2: Make changes
git add .
git commit -m "Feature"
git push

# Day 3: Pull changes (if made on another computer)
git pull
```

### Workflow 2: Using Cloned Repository

```bash
# Clone repository
git clone https://github.com/username/repo.git
cd repo

# Make changes
git add .
git commit -m "Update"

# Push
git push
```

---

## Exercises

### Exercise 1: Connect Local Repository to Remote

**Objective:** Connect your local repo to GitHub

**Prerequisites:** Complete your local repository and create GitHub account

**Instructions:**

1. **Create repository on GitHub** (if not done in previous module)
   - Go to github.com
   - Click "+" and "New repository"
   - Name it `demo-repo`
   - Initialize with README
   - Copy the HTTPS or SSH URL

2. **Connect local repository**
   ```bash
   cd my-first-repo
   
   # Add GitHub as remote
   git remote add origin https://github.com/YOUR-USERNAME/demo-repo.git
   ```

3. **Verify connection**
   ```bash
   git remote -v
   ```

   **Expected output:**
   ```
   origin  https://github.com/YOUR-USERNAME/demo-repo.git (fetch)
   origin  https://github.com/YOUR-USERNAME/demo-repo.git (push)
   ```

4. **Rename branch if needed**
   ```bash
   # Check default branch
   git branch
   
   # If using 'master', rename to 'main'
   git branch -M main
   ```

**Verification Checklist:**
- [ ] Remote added successfully
- [ ] `git remote -v` shows your GitHub URL
- [ ] Local branch matches GitHub default branch

---

### Exercise 2: Push Changes to GitHub

**Objective:** Upload your local commits to GitHub

**Instructions:**

1. **Make sure you have commits**
   ```bash
   git log --oneline
   # Should show your commits
   ```

2. **Push with upstream tracking**
   ```bash
   git push -u origin main
   # (or 'master' if that's your branch)
   ```

   **First time push may need authentication:**
   - SSH: Confirm with passphrase
   - HTTPS: No additional auth needed (already verified)

3. **Verify on GitHub**
   - Visit github.com/YOUR-USERNAME/demo-repo
   - You should see your files!
   - Click on commits to see history

4. **Check tracking**
   ```bash
   git log --oneline -n 3
   # Should show "(HEAD -> main, origin/main)"
   ```

**Verification Checklist:**
- [ ] Push successful (no errors)
- [ ] Files visible on GitHub
- [ ] Commit history visible on GitHub
- [ ] Branch shows as tracked

---

### Exercise 3: Create and Push Feature Branch

**Objective:** Practice pushing feature branches to GitHub

**Instructions:**

1. **Create feature branch locally**
   ```bash
   git switch -c feature-new-feature
   ```

2. **Make changes and commit**
   ```bash
   echo "Feature content" > feature.txt
   git add feature.txt
   git commit -m "Add new feature"
   ```

3. **Push feature branch to GitHub**
   ```bash
   git push -u origin feature-new-feature
   ```

4. **View on GitHub**
   - Visit your repository
   - Click "Branches" tab
   - You should see `feature-new-feature`

5. **Switch back to main (in preparation for next exercise)**
   ```bash
   git switch main
   ```

**Verification Checklist:**
- [ ] Feature branch pushed successfully
- [ ] Branch visible on GitHub
- [ ] Commits visible in branch history
- [ ] Can switch between branches locally

---

### Exercise 4: Simulate Collaboration (Pull Changes)

**Objective:** Practice pulling changes from GitHub

**Instructions:**

1. **Make a change on GitHub directly**
   - Go to github.com/YOUR-USERNAME/demo-repo
   - Click on a file (like README.md)
   - Click pencil icon to edit
   - Add a line: "Updated from GitHub"
   - Click "Commit changes"
   - Add commit message

2. **Return to local terminal**
   ```bash
   git status
   # Status shows nothing yet (GitHub change not reflected)
   ```

3. **Pull changes from GitHub**
   ```bash
   git pull
   ```

   **Output:**
   ```
   remote: Counting objects: 3, done.
   From github.com:...
   [details of pull]
   ```

4. **Verify the change**
   ```bash
   cat README.md
   # Should contain "Updated from GitHub"
   ```

5. **View in log**
   ```bash
   git log --oneline -n 2
   # Should show the pull commit
   ```

**Verification Checklist:**
- [ ] Change made on GitHub
- [ ] Pull successful
- [ ] Local file updated with GitHub changes
- [ ] Log shows new commit

---

## Command Reference

| Command | Purpose |
|---------|---------|
| `git remote -v` | List remotes |
| `git remote add origin <url>` | Add remote |
| `git push -u origin main` | Push with tracking |
| `git push` | Push changes |
| `git pull` | Fetch and merge |
| `git fetch` | Download changes only |
| `git branch -r` | View remote branches |

---

## SSH vs HTTPS Quickly

| SSH | HTTPS |
|-----|-------|
| Secure key-based auth | Password-based |
| No password each time | May need credentials |
| Setup required | Works immediately |
| `git@github.com:...` | `https://github.com/...` |

---

## Key Takeaways

✅ Remote repositories allow cloud backup
✅ `git push` sends local changes to GitHub
✅ `git pull` downloads remote changes
✅ Tracking branches simplify push/pull
✅ GitHub becomes your central collaboration hub

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `fatal: not a git repository` | You're not in a Git folder |
| Remote URL wrong | Use `git remote set-url origin <new-url>` |
| Authentication failed | Check SSH keys or HTTPS credentials |
| Can't push | Ensure you have commits to push |

---

## Next Steps

You're now syncing with GitHub! In **Module 2**, you'll learn about managing repositories and working with .gitignore and README files.

---

**[← Back to Module 0](./Module-0-GitHub-Basics.md)** | **[Next: Module 2 →](./Module-2-Repository-Management.md)**
