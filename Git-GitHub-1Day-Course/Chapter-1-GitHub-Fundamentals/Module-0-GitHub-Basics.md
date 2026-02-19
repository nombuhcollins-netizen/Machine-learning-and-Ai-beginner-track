# Chapter 1 - Module 0: GitHub Basics

**Duration:** 30 minutes | **Difficulty:** Beginner

---

## Learning Objectives

By the end of this module, you will be able to:

1. Understand what GitHub is and why it's essential
2. Create and configure a GitHub account
3. Set up authentication (SSH or HTTPS)
4. Create your first GitHub repository
5. Understand GitHub's interface

---

## What is GitHub?

GitHub is a **web-based platform** built on top of Git that provides:

- **Repository Hosting** - Store your code in the cloud
- **Collaboration** - Multiple developers working together
- **Code Review** - Team review before merging
- **Project Management** - Issues, Projects, Wikis
- **CI/CD** - Automated testing and deployment
- **Social Features** - Follow others, contribute to open source
- **Free & Paid Plans** - Free for public and private repositories

### GitHub vs Git

| Git | GitHub |
|-----|--------|
| Version control system (local) | Web platform for collaboration |
| Stores code history | Hosts Git repositories |
| Command-line tool | Web interface + API |
| Free and open-source | Free with premium options |

---

## Creating Your GitHub Account

### Step 1: Visit GitHub

Go to [github.com](https://github.com)

### Step 2: Sign Up

Click "Sign up" and fill in:
- Email address
- Password
- Username (choose wisely - it's your identity!)

### Step 3: Verify Email

Check your email for verification link

### Step 4: Complete Setup

- Select plan (Free is fine for learning)
- Answer setup questions (optional)

### Step 5: Set Up SSH Keys (Recommended)

SSH keys allow secure, passwordless authentication.

#### Generate SSH Key

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

When prompted:
- **Enter file location:** Press Enter (default: ~/.ssh/id_ed25519)
- **Enter passphrase:** Create a secure passphrase

#### Add SSH Key to GitHub

1. Copy your public key:
   ```bash
   # macOS/Linux
   cat ~/.ssh/id_ed25519.pub
   
   # Windows (PowerShell)
   type $env:USERPROFILE\.ssh\id_ed25519.pub
   ```

2. Go to [GitHub Settings > SSH Keys](https://github.com/settings/keys)

3. Click "New SSH key"

4. Paste your public key and save

#### Test SSH Connection

```bash
ssh -T git@github.com
```

**Expected output:**
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

---

### Alternative: HTTPS Authentication

If SSH is too complex, use HTTPS instead:

1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)

2. Click "Generate new token"

3. Select scopes: `repo`, `write:packages`, `read:packages`

4. Copy the token and keep it safe

5. When pushing, use your token as password

---

## GitHub Interface Overview

### Your Dashboard
- Shows your repositories
- Activity feed
- Trending repositories

### Repository Page

```
┌──────────────────────────────────┐
│ username/repository-name          │
├──────────────────────────────────┤
│ Code | Issues | Pull requests    │
│ Projects | Wiki | Security       │
├──────────────────────────────────┤
│ Main branch: master              │
├──────────────────────────────────┤
│ File browser                      │
│ ├── README.md                     │
│ ├── src/                          │
│ └── ...                           │
└──────────────────────────────────┘
```

### Key Areas

**Code Tab:** View files and commit history
**Issues:** Track bugs, features, discussions
**Pull Requests:** Review changes before merging
**Projects:** Kanban boards for project management
**Settings:** Repository configuration

---

## Creating Your First GitHub Repository

### Step 1: New Repository

On GitHub.com:
1. Click "+" in top right
2. Select "New repository"

### Step 2: Configure

Fill in:
- **Repository name:** `my-first-repo` (or any name)
- **Description:** "My first GitHub repository"
- **Public/Private:** Choose one (Public recommended for learning)
- **Initialize with README:** Check this

### Step 3: Create

Click "Create repository"

### Step 4: Note the URL

You'll see options to clone:
- **HTTPS:** `https://github.com/username/my-first-repo.git`
- **SSH:** `git@github.com:username/my-first-repo.git`

---

## Exercises

### Exercise 1: Create GitHub Account

**Objective:** Set up your GitHub account

**Steps:**

1. Visit [github.com](https://github.com)
2. Click "Sign up"
3. Enter email, password, and username
4. Verify email address
5. Complete setup

**Verification Checklist:**
- [ ] Account created
- [ ] Email verified
- [ ] Can log in to github.com
- [ ] Dashboard visible with "New" button

---

### Exercise 2: Set Up SSH Authentication

**Objective:** Configure secure authentication

**Steps (choose SSH or HTTPS):**

**Option A: SSH (Recommended)**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# (Press Enter for file location, enter passphrase)

# View public key
cat ~/.ssh/id_ed25519.pub
```

1. Copy the output (starts with `ssh-ed25519`)
2. Go to GitHub Settings > SSH and GPG keys
3. Click "New SSH key"
4. Paste your key
5. Test: `ssh -T git@github.com`

**Option B: HTTPS**
```bash
# Create personal access token on GitHub Settings
# Use token as password when pushing
```

**Verification Checklist:**
- [ ] SSH key generated (or token created for HTTPS)
- [ ] Key added to GitHub
- [ ] SSH connection test successful (if using SSH)

---

### Exercise 3: Create Repository on GitHub

**Objective:** Create your first GitHub repository

**Steps:**

1. On github.com, click "+" and "New repository"
2. **Name:** `my-github-repo`
3. **Description:** "Learning Git and GitHub"
4. **Public:** Yes
5. **Initialize with README:** Check
6. Click "Create repository"

**After Creation:**
- Note your repository URL
- Click "Code" button to see clone options
- Copy your HTTPS or SSH URL

**Verification Checklist:**
- [ ] Repository created
- [ ] Visible on your GitHub profile
- [ ] URL copied and saved
- [ ] README.md file exists

---

## GitHub Key Features

### README.md
Shows when visiting repository. Use for:
- Project description
- Installation instructions
- Usage examples
- Contribution guidelines

### .gitignore
Specifies files Git should ignore:
- Temporary files
- Dependency folders (node_modules, venv)
- Secrets (API keys, passwords)

### Branches
Visible in "Code" tab, usually `main` or `master`

### Releases
Published versions of your code (on Releases tab)

---

## Working with GitHub via Command Line

You'll connect your local repository to GitHub in the next module. here are the commands you'll use:

```bash
git remote add origin https://github.com/username/repo.git
git branch -M main
git push -u origin main
```

---

## Key Takeaways

✅ GitHub is the central hub for collaborative development
✅ Create an account and set up authentication first
✅ SSH keys provide secure, passwordless authentication
✅ Each repository has a URL for cloning and pushing
✅ GitHub provides version control plus collaboration tools

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| SSH key not working | Check passphrase, verify key on GitHub |
| HTTPS password rejected | Use personal access token, not password |
| Repository not visible | Check visibility settings (Public/Private) |
| Can't find SSH settings | Go to Settings > SSH and GPG keys |

---

## Next Steps

Now that you have GitHub set up, in **Module 1** you'll learn how to push your local code to GitHub and work with remotes.

---

## Resources

- [GitHub Docs: Getting Started](https://docs.github.com/en/get-started)
- [GitHub Docs: SSH Keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [GitHub Docs: Setting Up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)

---

**[← Back to Chapter 1 Overview](./README.md)** | **[Next: Module 1 →](./Module-1-Remote-Operations.md)**
