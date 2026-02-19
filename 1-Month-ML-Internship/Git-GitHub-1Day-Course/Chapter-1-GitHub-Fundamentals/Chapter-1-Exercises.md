# Chapter 1: GitHub Fundamentals - Comprehensive Exercises

**Difficulty:** Intermediate | **Estimated Time:** 1.5 hours | **Prerequisites:** Chapter 0 completed

---

## Overview

This exercise file consolidates and expands on all exercises from Chapter 1 modules. Complete these exercises to master GitHub and remote repository operations.

---

## Exercise 1: GitHub Account Setup and SSH Configuration

**Objective:** Set up GitHub account and secure authentication

**Instructions:**

1. **Create/Access GitHub Account**
   - Go to https://github.com
   - Sign up for an account if needed
   - Verify your email address

2. **Generate SSH Key**
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   # Press Enter to accept default location
   # Enter passphrase (optional but recommended)
   ```

3. **Add SSH Key to SSH Agent**
   ```bash
   # On Windows with Git Bash:
   eval $(ssh-agent -s)
   ssh-add ~/.ssh/id_ed25519
   
   # Or using Windows native SSH:
   ssh-add C:\Users\YourUsername\.ssh\id_ed25519
   ```

4. **Copy SSH Public Key**
   ```bash
   # Display the public key
   cat ~/.ssh/id_ed25519.pub
   # Copy the entire output to clipboard
   ```

5. **Add SSH Key to GitHub**
   - Go to GitHub Settings → SSH and GPG keys
   - Click "New SSH key"
   - Paste your public key
   - Give it a title (e.g., "My Work Machine")
   - Click "Add SSH key"

6. **Test SSH Connection**
   ```bash
   ssh -T git@github.com
   # Should output: Hi username! You've successfully authenticated...
   ```

**Verification Checklist:**
- [ ] GitHub account created and verified
- [ ] SSH key pair generated
- [ ] SSH key added to GitHub account
- [ ] SSH connection test successful
- [ ] No password required for authentication

**Key Concepts:**
- SSH provides secure, passwordless authentication
- Public key is shared with GitHub
- Private key stays on your machine

---

## Exercise 2: Create Your First Remote Repository

**Objective:** Create a repository on GitHub and understand remote structure

**Instructions:**

1. **Create Repository on GitHub**
   - Go to https://github.com/new
   - Repository name: `github-practice`
   - Description: "Learning GitHub fundamentals"
   - Choose "Public" or "Private"
   - **Skip** "Initialize this repository" (we'll do it locally)
   - Click "Create repository"

2. **Note the Repository URL**
   - Copy the SSH URL (e.g., `git@github.com:username/github-practice.git`)

3. **Initialize Local Repository**
   ```bash
   mkdir github-practice
   cd github-practice
   git init
   git config user.name "Your Name"
   git config user.email "your.email@example.com"
   ```

4. **Add Remote**
   ```bash
   git remote add origin git@github.com:username/github-practice.git
   # Replace "username" with your GitHub username
   ```

5. **Verify Remote**
   ```bash
   git remote -v
   # Should show:
   # origin  git@github.com:username/github-practice.git (fetch)
   # origin  git@github.com:username/github-practice.git (push)
   ```

6. **Create and Commit Files**
   ```bash
   echo "# GitHub Practice Repository" > README.md
   git add README.md
   git commit -m "docs: Initial commit with README"
   ```

7. **Push to GitHub**
   ```bash
   git branch -M main
   git push -u origin main
   ```

8. **Verify on GitHub**
   - Refresh your GitHub repository page
   - Confirm README.md is visible

**Verification Checklist:**
- [ ] Repository created on GitHub
- [ ] SSH URL copied correctly
- [ ] Local repository initialized
- [ ] Remote added with correct URL
- [ ] Files pushed to GitHub
- [ ] Files visible on GitHub web interface

**Key Concepts:**
- Remote repositories live on GitHub servers
- "origin" is the default remote name
- `git push -u` sets upstream tracking

---

## Exercise 3: Clone a Repository

**Objective:** Clone an existing repository and work with it

**Instructions:**

1. **Create Another Repository on GitHub**
   - Go to https://github.com/new
   - Name: `github-practice-clone`
   - Initialize with README
   - Click "Create repository"

2. **Clone the Repository**
   ```bash
   cd ~
   git clone git@github.com:username/github-practice-clone.git
   cd github-practice-clone
   ```

3. **Verify Cloned Content**
   ```bash
   ls -la          # Should show README.md
   git remote -v   # Should show origin
   git log         # Should show clone history
   ```

4. **Make Changes to Cloned Repository**
   ```bash
   echo "## Getting Started" >> README.md
   echo "This repository is cloned from GitHub." >> README.md
   ```

5. **Commit Changes**
   ```bash
   git add README.md
   git commit -m "docs: Update README with getting started section"
   ```

6. **Push Changes Back**
   ```bash
   git push origin main
   ```

7. **Verify on GitHub**
   - Refresh repository page
   - Confirm changes are visible

**Verification Checklist:**
- [ ] Repository cloned successfully to local machine
- [ ] Original content from GitHub is present
- [ ] Can make and commit local changes
- [ ] Changes pushed back to GitHub successfully
- [ ] Changes visible on GitHub web interface

**Key Concepts:**
- `git clone` creates local copy from remote
- Cloned repository automatically sets up origin
- Changes require commit and push

---

## Exercise 4: Manage Branches on GitHub

**Objective:** Create and manage branches with remote tracking

**Instructions:**

1. **Create Local Feature Branch**
   ```bash
   git checkout -b feature/add-contributing-guide
   ```

2. **Create Changes on Feature Branch**
   ```bash
   echo "# Contributing Guide" > CONTRIBUTING.md
   echo "" >> CONTRIBUTING.md
   echo "## How to Contribute" >> CONTRIBUTING.md
   echo "1. Fork the repository" >> CONTRIBUTING.md
   echo "2. Create a feature branch" >> CONTRIBUTING.md
   echo "3. Make your changes" >> CONTRIBUTING.md
   ```

3. **Commit Changes**
   ```bash
   git add CONTRIBUTING.md
   git commit -m "docs: Add contributing guide"
   ```

4. **Push Feature Branch to GitHub**
   ```bash
   git push -u origin feature/add-contributing-guide
   ```

5. **Verify on GitHub**
   - Go to repository
   - Click "Branches" tab
   - Confirm your feature branch appears

6. **Create Additional Branch**
   ```bash
   git checkout main
   git checkout -b feature/add-license
   echo "MIT License" > LICENSE
   git add LICENSE
   git commit -m "docs: Add MIT license"
   git push -u origin feature/add-license
   ```

7. **List All Branches**
   ```bash
   git branch -a      # Shows local and remote branches
   git branch -r      # Shows only remote branches
   ```

8. **Delete Branch (Locally and Remotely)**
   ```bash
   git branch -d feature/add-license           # Delete locally
   git push origin --delete feature/add-license # Delete on GitHub
   ```

**Verification Checklist:**
- [ ] Feature branches created locally
- [ ] Branches pushed to GitHub successfully
- [ ] Branches visible on GitHub "Branches" tab
- [ ] Can list remote branches with `git branch -r`
- [ ] Branch deletion works locally and remotely
- [ ] Remaining branch visible on GitHub

**Key Concepts:**
- Remote tracking branches follow pattern: `origin/branch-name`
- `git push -u` establishes upstream tracking
- Branches can be deleted locally and remotely separately

---

## Exercise 5: Sync with Remote Repository

**Objective:** Keep local repository synchronized with remote changes

**Instructions:**

1. **Make Changes on GitHub Directly**
   - Go to your github-practice-clone repository on GitHub
   - Click on README.md
   - Click the pencil icon to edit
   - Add a line: "## Updates from GitHub Web Interface"
   - Commit directly on GitHub

2. **Fetch Remote Changes**
   ```bash
   git fetch origin
   git status          # Should show: "Your branch is behind..."
   ```

3. **View Incoming Changes**
   ```bash
   git log --oneline -n 3
   git log origin/main --oneline -n 3  # View remote commits
   git diff main origin/main            # See what changed
   ```

4. **Pull Changes**
   ```bash
   git pull origin main
   cat README.md       # Should contain the GitHub web edit
   ```

5. **Create Conflict Scenario**
   - Edit README.md locally
   ```bash
   echo "## Local Updates" >> README.md
   git add README.md
   git commit -m "docs: Add local updates"
   ```
   - Edit same file on GitHub web interface
   - Add different content to README.md

6. **Attempt Pull and Resolve**
   ```bash
   git fetch origin
   git pull origin main
   # May show merge conflict
   ```

7. **If Conflict Occurs, Resolve It**
   ```bash
   # Edit README.md manually to resolve
   git add README.md
   git commit -m "fix: Resolve README conflict"
   git push origin main
   ```

**Verification Checklist:**
- [ ] Remote changes fetched successfully
- [ ] Local and remote commits can be compared
- [ ] Changes pulled and integrated
- [ ] Conflicts can be resolved
- [ ] Final state pushed to GitHub

**Key Concepts:**
- `git fetch` gets updates without merging
- `git pull` is fetch + merge
- Conflicts occur when same files change differently
- Always pull before pushing in shared repos

---

## Exercise 6: Work with Multiple Remotes

**Objective:** Understand and manage multiple remote repositories

**Instructions:**

1. **Create Fork (on GitHub)**
   - Find a public repository (e.g., a friend's project)
   - Click "Fork" button
   - This creates a copy under your account

2. **Set Up Upstream Remote**
   ```bash
   cd github-practice-clone
   git remote list
   ```

3. **Add Upstream Remote**
   ```bash
   # The original repository URL
   git remote add upstream git@github.com:original-owner/repo.git
   ```

4. **Verify Multiple Remotes**
   ```bash
   git remote -v
   # Should show both origin (your fork) and upstream
   ```

5. **Fetch from Upstream**
   ```bash
   git fetch upstream
   ```

6. **Create Feature Branch from Upstream**
   ```bash
   git checkout -b sync-with-upstream
   git merge upstream/main
   ```

7. **Push to Your Fork**
   ```bash
   git push origin sync-with-upstream
   ```

8. **Create Pull Request** (covered in Chapter 2)

**Verification Checklist:**
- [ ] Repository forked successfully on GitHub
- [ ] Both origin and upstream remotes configured
- [ ] Can fetch from upstream
- [ ] Can merge upstream changes into local branch
- [ ] Changes can be pushed to origin (your fork)

**Key Concepts:**
- "origin" = your repository copy
- "upstream" = original source repository
- Fork workflow enables contributing to others' projects

---

## Exercise 7: GitHub Repository Settings

**Objective:** Configure repository settings and options

**Instructions:**

1. **Access Repository Settings**
   - Go to your github-practice repository
   - Click "Settings" tab

2. **Explore General Settings**
   - View repository name and description
   - Note visibility (Public/Private)
   - Check "Dangerous Zone" options

3. **Configure Branch Protection** (if available)
   - Go to "Branches" in Settings
   - Add rule for "main" branch
   - Require pull request reviews
   - Require status checks before merging

4. **Add Collaborators**
   - Go to "Collaborators & teams"
   - Click "Add people"
   - Search for a GitHub user
   - (Skip actual addition to avoid real commitments)

5. **Explore Webhooks & Integrations**
   - Go to "Webhooks"
   - See available integration options
   - (Don't configure unless you have a specific service)

6. **View Repository Insights**
   - Click "Insights" tab
   - Explore "Network" view
   - Check "Contributors"

**Verification Checklist:**
- [ ] Accessed Settings successfully
- [ ] Reviewed General configuration options
- [ ] Understood Branch Protection settings
- [ ] Explored Collaborators section
- [ ] Reviewed Webhooks and Integrations
- [ ] Viewed repository Insights

**Key Concepts:**
- Settings control repository behavior
- Branch protection enforces workflow standards
- Webhooks enable external integrations

---

## Exercise 8: Create and Track a .gitignore File

**Objective:** Configure Git to ignore specific files and directories

**Instructions:**

1. **Navigate to Repository**
   ```bash
   cd ~/github-practice
   ```

2. **Create .gitignore File**
   ```bash
   cat > .gitignore << EOF
   # Dependencies
   node_modules/
   venv/
   __pycache__/
   
   # Build outputs
   dist/
   build/
   *.o
   
   # Environment variables
   .env
   .env.local
   
   # IDE
   .vscode/
   .idea/
   *.swp
   *.swo
   
   # OS
   .DS_Store
   Thumbs.db
   
   # Logs
   *.log
   logs/
   EOF
   ```

3. **Create Files to Ignore**
   ```bash
   mkdir node_modules
   mkdir __pycache__
   echo "API_KEY=secret123" > .env
   echo "This should be ignored" > node_modules/package.json
   ```

4. **Check Status**
   ```bash
   git status
   # Should NOT show ignored files
   ```

5. **Commit .gitignore**
   ```bash
   git add .gitignore
   git commit -m "config: Add .gitignore file"
   ```

6. **Verify Ignored Files**
   ```bash
   git status
   # node_modules/, __pycache__, .env should not appear
   ```

7. **Push to GitHub**
   ```bash
   git push origin main
   ```

**Verification Checklist:**
- [ ] .gitignore file created
- [ ] Ignored directories and files don't appear in `git status`
- [ ] .gitignore itself is committed
- [ ] Ignored files are not tracked after push
- [ ] Can view .gitignore on GitHub

**Key Concepts:**
- .gitignore prevents tracking unnecessary files
- Common patterns: dependencies, build outputs, secrets
- .gitignore should be committed to repository

---

## Exercise 9: README and Documentation

**Objective:** Create comprehensive repository documentation

**Instructions:**

1. **Create Enhanced README**
   ```bash
   cat > README.md << EOF
   # My Project Name
   
   ## Description
   This is a project for learning GitHub fundamentals.
   
   ## Installation
   \`\`\`bash
   git clone git@github.com:username/repo.git
   cd repo
   npm install
   \`\`\`
   
   ## Usage
   \`\`\`bash
   npm start
   \`\`\`
   
   ## Contributing
   See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
   
   ## License
   MIT License - see [LICENSE](LICENSE) file
   
   ## Contact
   - Email: your.email@example.com
   - GitHub: [@yourusername](https://github.com/yourusername)
   EOF
   ```

2. **Create CONTRIBUTING.md**
   ```bash
   cat > CONTRIBUTING.md << EOF
   # Contributing Guidelines
   
   ## Steps to Contribute
   1. Fork the repository
   2. Create a feature branch
   3. Make your changes
   4. Commit with clear messages
   5. Push to your fork
   6. Create a Pull Request
   
   ## Code Guidelines
   - Write clear commit messages
   - Include comments for complex code
   - Test your changes
   EOF
   ```

3. **Create CODE_OF_CONDUCT.md**
   ```bash
   cat > CODE_OF_CONDUCT.md << EOF
   # Code of Conduct
   
   ## Our Pledge
   We are committed to providing a welcoming environment.
   
   ## Our Standards
   - Be respectful
   - Be inclusive
   - Provide constructive feedback
   EOF
   ```

4. **Commit Documentation**
   ```bash
   git add README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
   git commit -m "docs: Add comprehensive project documentation"
   ```

5. **Push to GitHub**
   ```bash
   git push origin main
   ```

6. **Verify on GitHub**
   - README.md should display on repository home
   - Other docs should be viewable as files

**Verification Checklist:**
- [ ] README.md created with proper sections
- [ ] CONTRIBUTING.md provides contribution guidelines
- [ ] CODE_OF_CONDUCT.md establishes community standards
- [ ] All documentation files committed
- [ ] Files visible and formatted correctly on GitHub

**Key Concepts:**
- Documentation is crucial for project usability
- README is the first thing visitors see
- CONTRIBUTING.md sets contribution expectations
- Good documentation increases project adoption

---

## Exercise 10: Template and Automation

**Objective:** Use GitHub templates for consistency

**Instructions:**

1. **Create Issues Template**
   ```bash
   mkdir -p .github/ISSUE_TEMPLATE
   cat > .github/ISSUE_TEMPLATE/bug_report.md << EOF
   ---
   name: Bug Report
   about: Report a bug
   ---
   
   ## Description
   Describe the bug clearly.
   
   ## Steps to Reproduce
   1. Step 1
   2. Step 2
   
   ## Expected Behavior
   What should happen.
   
   ## Actual Behavior
   What actually happens.
   EOF
   ```

2. **Create Pull Request Template**
   ```bash
   cat > .github/pull_request_template.md << EOF
   ## Description
   Describe your changes here.
   
   ## Related Issue
   Fixes #(issue number)
   
   ## Changes
   - Change 1
   - Change 2
   
   ## Checklist
   - [ ] Code reviewed
   - [ ] Tests passed
   - [ ] Documentation updated
   EOF
   ```

3. **Commit Templates**
   ```bash
   git add .github/
   git commit -m "config: Add issue and PR templates"
   git push origin main
   ```

4. **Verify on GitHub**
   - Create a new issue
   - Bug report template should appear
   - Create a new pull request
   - PR template should appear

**Verification Checklist:**
- [ ] .github directory created
- [ ] Issue template created and committed
- [ ] PR template created and committed
- [ ] Templates appear when creating issues/PRs on GitHub
- [ ] Templates guide users through proper information

**Key Concepts:**
- Templates ensure consistent issue/PR information
- .github is special directory for GitHub specific files
- Templates improve quality of contributions

---

## Chapter 1 Challenge Project

**Objective:** Apply all GitHub fundamentals in one project

**Project:** Create a Community Project Repository

**Requirements:**

1. Create new repository on GitHub: `community-project`
2. Set up SSH authentication
3. Clone repository locally
4. Create comprehensive README.md with:
   - Project description
   - Installation instructions
   - Usage examples
   - Contributing guidelines
5. Create .gitignore for multiple languages/frameworks
6. Create CONTRIBUTING.md and CODE_OF_CONDUCT.md
7. Make commits with semantic messages
8. Create and push at least 3 feature branches
9. Merge one branch back to main on GitHub
10. Add branch protection rules

**Success Criteria:**
- [ ] Repository created on GitHub
- [ ] SSH authentication working
- [ ] All documentation files present
- [ ] Meaningful commit history
- [ ] Multiple branches created and tracked
- [ ] Branch protection configured

---

## Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| SSH connection fails | Verify public key on GitHub, check SSH agent |
| Push is rejected | Run `git pull origin main` first |
| Can't clone repository | Check SSH key setup, verify repository is public or you have access |
| Merge conflict from GitHub | Run `git pull origin main`, resolve manually, commit and push |
| Branch not showing on GitHub | Use `git push -u origin branch-name` |
| .gitignore not working | Commit .gitignore before creating ignored files |
| Can't add collaborators | Ensure you have admin access to repository |

---

## Next Steps

You've completed Chapter 1 exercises! You now understand:
- ✅ GitHub account and SSH setup
- ✅ Creating and cloning repositories
- ✅ Remote operations (push, pull, fetch)
- ✅ Branch management on GitHub
- ✅ Repository documentation and configuration

**Proceed to Chapter 2: Collaboration Workflows** to learn about pull requests and team collaboration.

---

**[← Back to Chapter 1 Overview](./README.md)** | **[Next: Chapter 2 →](../Chapter-2-Collaboration-Workflows/README.md)**
