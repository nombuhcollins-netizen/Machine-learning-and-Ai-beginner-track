# Chapter 3 - Module 1: Stashing & Tags

**Duration:** 30 minutes | **Difficulty:** Intermediate

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use stashing to save work temporarily
2. Apply and pop stashes
3. Manage multiple stashes
4. Create tags for releases
5. Understand semantic versioning
6. Create GitHub releases

---

## What is Stashing?

**Stashing** is temporary storage for uncommitted changes.

### Scenario

You're working on feature-A:

```
feature-A:
├── Modified: file.py
└── New: utils.py
```

Suddenly you need to switch to main to fix a bug.

**Problem:** You can't switch branches with uncommitted changes

**Solution:** Stash the changes, switch, fix bug, then restore

---

## Stash Commands

### Create Stash

```bash
git stash                      # Stash all changes
git stash save "description"   # Stash with message
git stash push -m "msg"        # Alternative syntax
```

### List Stashes

```bash
git stash list
# Output:
# stash@{0}: On feature-A: Save progress
# stash@{1}: WIP on feature-B
# stash@{2}: Updated files
```

### Apply Stash

```bash
git stash apply                # Apply most recent
git stash apply stash@{1}      # Apply specific stash
git stash apply --index        # Also restore staging area
```

### Pop Stash

```bash
git stash pop                  # Apply and remove
git stash pop stash@{1}        # Pop specific stash
```

### Delete Stash

```bash
git stash drop                 # Delete most recent
git stash drop stash@{1}       # Delete specific
git stash clear                # Delete all stashes
```

---

## Stash Workflow

### Scenario: Fix Bug on Main While Working on Feature

```
1. Working on feature-login
   └─ Modified: auth.py, tests.py

2. Manager: "Fix critical bug on main!"

3. Stash changes
   git stash save "Login feature in progress"

4. Switch to main and fix bug
   git switch main
   # Fix bug
   git commit -m "Fix critical bug"
   git push

5. Back to feature
   git switch feature-login
   git stash pop
   # Resume working on login

6. Continue development
   # Original files restored with changes
```

---

## Tags

### What is a Tag?

A **tag** is a named reference to a specific commit.

```
main: A → B → C (v1.0) → D (v1.1) → E
```

### Uses

- **Releases:** Mark version releases
- **Milestones:** Important points in history
- **Annotations:** Tag with message and metadata

### Lightweight vs Annotated

**Lightweight:** Simple name
```bash
git tag v1.0
```

**Annotated:** Metadata (author, message, timestamp)
```bash
git tag -a v1.0 -m "Release 1.0"
```

---

## Creating Tags

### Simple Tag

```bash
git tag v1.0                   # Tag current commit
git tag v1.0 a1b2c3d          # Tag specific commit
```

### Annotated Tag (Recommended)

```bash
git tag -a v1.0 -m "Release version 1.0"
```

### Listing Tags

```bash
git tag                        # List all tags
git tag -l "v1.*"              # Pattern matching
git tag -l -n                  # List with messages
```

### Viewing Tag

```bash
git show v1.0                  # Show tag commit
git log v1.0                   # History from tag
```

### Deleting Tag

```bash
git tag -d v1.0                # Delete local
git push origin --delete v1.0  # Delete remote
```

### Pushing Tags

```bash
git push origin v1.0           # Push specific tag
git push origin --tags         # Push all tags
```

---

## Semantic Versioning

**Semantic Versioning (SemVer):** MAJOR.MINOR.PATCH

```
v1.2.3
├─ 1 = MAJOR version (breaking changes)
├─ 2 = MINOR version (new features, backward compatible)
└─ 3 = PATCH version (bug fixes)
```

### Examples

```
v0.1.0 - Initial release (often 0.x for pre-release)
v1.0.0 - First stable release
v1.1.0 - New features added
v1.1.1 - Bug fix
v2.0.0 - Breaking changes
```

### Rules

- MAJOR: New features with breaking changes
- MINOR: New features, backward compatible
- PATCH: Bug fixes only

### Examples by Scenario

```
Current: v1.2.3

Add backward-compatible feature:    v1.3.0
Fix a bug:                           v1.2.4
Redesign with breaking changes:     v2.0.0
```

---

## GitHub Releases

### What is a Release?

A **release** is a published version with:
- Tag
- Release notes
- Downloadable assets (binaries, etc.)
- Metadata

### Create Release on GitHub

1. Go to "Releases" tab
2. Click "Draft a new release"
3. **Tag version:** `v1.0.0`
4. **Target:** `main` branch
5. **Title:** "Version 1.0.0"
6. **Description:**
   ```markdown
   ## Features
   - New login system
   - Mobile app support
   
   ## Bug Fixes
   - Fixed timeout issue
   - Improved performance
   
   ## Breaking Changes
   - Old API endpoints removed
   
   ## Installation
   ```
   pip install myproject==1.0.0
   ```
   ```
7. **Attach binaries** if applicable
8. Mark as pre-release (if not stable)
9. Publish

---

## Exercises

### Exercise 1: Stash and Pop

**Objective:** Practice saving and restoring work

**Instructions:**

1. **Create feature branch**
   ```bash
   git switch -c feature-stash-demo
   ```

2. **Make uncommitted changes**
   ```bash
   echo "Feature work in progress" > feature.txt
   git add feature.txt
   # Don't commit yet
   ```

3. **Verify status**
   ```bash
   git status
   # Shows: Changes to be committed
   ```

4. **Stash the changes**
   ```bash
   git stash save "Feature work in progress"
   ```

5. **Verify stashed**
   ```bash
   git status
   # Changes should be gone
   
   git stash list
   # Should show your stash
   ```

6. **Switch branches (now possible)**
   ```bash
   git switch main
   # Work on main...
   git switch feature-stash-demo
   ```

7. **Restore stashed work**
   ```bash
   git stash pop
   ```

8. **Verify restoration**
   ```bash
   git status
   # feature.txt is back, ready to commit
   ```

**Verification Checklist:**
- [ ] Created stash successfully
- [ ] Able to switch branches after stashing
- [ ] Stash restored with pop
- [ ] Files restored correctly

---

### Exercise 2: Create and Push Tags

**Objective:** Tag releases and push to GitHub

**Instructions:**

1. **Ensure main is up to date**
   ```bash
   git switch main
   git pull
   ```

2. **Create first tag**
   ```bash
   git tag -a v1.0.0 -m "First stable release"
   ```

3. **Verify tag**
   ```bash
   git tag -l -n
   # Shows: v1.0.0 First stable release
   
   git show v1.0.0
   # Shows commit details
   ```

4. **Push tag to GitHub**
   ```bash
   git push origin v1.0.0
   ```

5. **Verify on GitHub**
   - GitHub → "Releases" tab
   - Should see v1.0.0 tag

6. **Create more tags** (simulating development)
   ```bash
   # Make a small change
   echo "Feature update" >> README.md
   git add README.md
   git commit -m "Update for v1.1.0"
   
   # Tag new version
   git tag -a v1.1.0 -m "Add new features"
   git push origin v1.1.0
   ```

**Verification Checklist:**
- [ ] Tags created successfully
- [ ] Tags pushed to GitHub
- [ ] Tags visible in Releases tab
- [ ] Can view tag commits

---

### Exercise 3: Create GitHub Release

**Objective:** Create a formal release with notes

**Instructions:**

1. **Go to GitHub repository**

2. **Click "Releases" tab**

3. **Click "Draft a new release"**

4. **Fill in details:**
   ```
   Tag version: v2.0.0
   Target: main
   Title: Version 2.0.0 - Major Update
   
   Description:
   ## 🎉 Major Features
   - Complete redesign of UI
   - Performance improvements
   - Mobile app support
   
   ## 🐛 Bug Fixes
   - Fixed incorrect calculations
   - Improved error handling
   
   ## ⚠️ Breaking Changes
   - Old API endpoints removed
   - Python 2.7 support dropped
   
   ## 📥 Installation
   ```bash
   pip install myapp==2.0.0
   ```

   ## 👏 Credits
   Thanks to all contributors!
   ```

5. **Choose options:**
   - Check "Create a discussion for this release" (optional)
   - Mark as pre-release if not stable
   - Mark as latest

6. **Publish Release**

7. **View on GitHub:**
   - Releases tab shows your release
   - Can click to view details

**Verification Checklist:**
- [ ] Release created on GitHub
- [ ] Release notes are clear
- [ ] Tag associated with release
- [ ] Release visible to public

---

## Stash Best Practices

✅ Use descriptive messages
✅ Pop or drop old stashes regularly
✅ Clean up: `git stash clear` when done

❌ Don't stash and forget
❌ Don't use as main workflow (commit instead)

---

## Tagging Best Practices

✅ Use semantic versioning
✅ Annotated tags for releases
✅ Include release notes
✅ Push tags to GitHub

❌ Don't reuse tag names
❌ Don't tag random commits
❌ Don't forget to document changes

---

## Command Reference

| Command | Purpose |
|---------|---------|
| `git stash` | Save uncommitted changes |
| `git stash list` | View all stashes |
| `git stash pop` | Apply and remove |
| `git tag v1.0` | Create lightweight tag |
| `git tag -a v1.0 -m "msg"` | Create annotated tag |
| `git push origin v1.0` | Push tag |

---

## Key Takeaways

✅ Stashing saves work without committing
✅ Useful for switching branches mid-work
✅ Tags mark important commits
✅ Semantic versioning communicates changes
✅ GitHub releases publicize versions

---

## Workflow with Stashing

```
1. Working on feature A
2. Need to fix bug: git stash
3. Switch to main: git switch main
4. Fix bug: git commit and push
5. Back to feature: git switch feature-A
6. Resume: git stash pop
7. Continue development
```

---

## Next Steps

You've learned stashing and tagging! **Module 2** covers GitHub's automation and advanced features.

---

**[← Back to Module 0](./Module-0-Rebasing-and-History.md)** | **[Next: Module 2 →](./Module-2-GitHub-Advanced-Features.md)**
