# Chapter 1 - Module 2: Repository Management

**Duration:** 30 minutes | **Difficulty:** Beginner

---

## Learning Objectives

By the end of this module, you will be able to:

1. Create and manage README files
2. Use .gitignore to exclude files
3. Configure repository settings
4. Clone repositories
5. Fork repositories
6. Understand repository permissions

---

## The README.md File

The README is the first thing people see when visiting your repository.

### Purpose

- **Description:** What does this project do?
- **Getting Started:** How to run it locally?
- **Installation:** Dependencies and setup
- **Usage:** Examples of how to use
- **Contributing:** How others can help
- **License:** Usage rights

### Markdown Format

README uses Markdown syntax:

```markdown
# Project Title
Main heading

## Section Title
Subheading

- Bullet point 1
- Bullet point 2

### Subsection
More details

```bash
# Code block
python main.py
```

[Link text](https://example.com)
```

### Create a Good README

```markdown
# My Project

Brief one-liner description.

## Getting Started

### Prerequisites
- Python 3.9+
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/username/project.git
cd project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script:
```bash
python main.py --help
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your fork
5. Create a pull request

## License

This project is licensed under the MIT License.
```

---

## The .gitignore File

**.gitignore** tells Git which files to ignore (not track).

### Why Ignore Files?

- **Dependencies:** `node_modules/`, `venv/` (can be reinstalled)
- **Secrets:** API keys, passwords (security risk)
- **Build Files:** Compiled code, temporary files
- **IDE Files:** `.vscode/`, `.idea/` (developer preference)
- **OS Files:** `.DS_Store`, `Thumbs.db`

### Create .gitignore

```bash
# In your repository root
touch .gitignore
```

### Common .gitignore Patterns

```
# Python
__pycache__/
*.py[cod]
*$py.class
venv/
*.egg-info/

# Node.js
node_modules/
npm-debug.log

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local

# Build
build/
dist/
```

### Gitignore Syntax

```
# Comments start with #
*.log              # Ignore all .log files
temp/              # Ignore entire directory
!important.log     # Exception: don't ignore this file
**/*.tmp           # Ignore .tmp in any directory
```

---

## Repository Settings on GitHub

### Access Settings

Go to **Settings** tab:

- **General:** Name, description, visibility
- **Collaborators:** Add team members
- **Branch protection:** Enforce requirements before merging
- **Webhooks:** Triggers for external services

### Important Settings

**Branch Protection Rules:**
- Require pull request reviews
- Require status checks
- Restrict who can force push

---

## Cloning Repositories

### `git clone`

Download entire repository.

```bash
git clone https://github.com/username/project.git
# or
git clone git@github.com:username/project.git

cd project
```

What `clone` does:
1. Creates local directory
2. Initializes `.git` folder
3. Downloads entire history
4. Sets up origin remote
5. Checks out main branch

---

## Forking Repositories

### What is a Fork?

A **fork** is your own copy of someone else's repository.

```
Original Repo (upstream)
    ↑ (pull request)
    |
Your Fork (origin)
    ↑
Your Local Clone
```

### When to Fork

- Contributing to open source
- Building upon someone's project
- Experimenting with someone's code

### How to Fork

1. Visit the repository on GitHub
2. Click "Fork" button (top right)
3. GitHub creates your copy
4. Clone your fork locally
5. Make changes and push
6. Create pull request to original

---

## File Permissions and Collaboration

### Permission Levels

| Level | Capabilities |
|-------|--------------|
| **Pull** | Clone, read, open issues |
| **Triage** | Manage issues, pull requests |
| **Push** | Create branches, merge |
| **Maintain** | Settings, team management |
| **Admin** | Full access |

### Adding Collaborators

Settings → Collaborators → Add by username/email

---

## Repository Organization

### Standard Structure

```
my-project/
├── README.md              # Project documentation
├── .gitignore            # Ignore patterns
├── LICENSE               # License file
├── requirements.txt      # Python dependencies
├── package.json          # Node dependencies
├── src/                  # Source code
│   └── main.py
├── tests/                # Test files
│   └── test_main.py
└── docs/                 # Documentation
    └── guide.md
```

---

## Exercises

### Exercise 1: Create README.md

**Objective:** Write a comprehensive README

**Instructions:**

1. **Edit existing README** (if starting from scratch)
   ```bash
   cd your-repo
   ```

2. **Create content**
   Create a file called `README.md` with:

   ```markdown
   # My Awesome Project

   A brief description of what this project does.

   ## Features

   - Feature 1
   - Feature 2
   - Feature 3

   ## Installation

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
   cd YOUR-REPO
   python main.py
   ```

   ## Usage

   ```bash
   python main.py --help
   ```

   ## Contributing

   Feel free to submit issues and pull requests.

   ## License

   MIT License
   ```

3. **Stage and commit**
   ```bash
   git add README.md
   git commit -m "Add comprehensive README"
   git push
   ```

4. **View on GitHub**
   - Visit your repository
   - README should display on main page

**Verification Checklist:**
- [ ] README.md created
- [ ] Content is descriptive and well-formatted
- [ ] Pushed to GitHub
- [ ] Displays on repository home page

---

### Exercise 2: Create .gitignore

**Objective:** Exclude unnecessary files from tracking

**Instructions:**

1. **Create .gitignore file**
   ```bash
   # In your repository directory
   cat > .gitignore << 'EOF'
   # Python
   __pycache__/
   *.pyc
   venv/
   .env

   # IDE
   .vscode/
   .idea/

   # OS
   .DS_Store
   Thumbs.db

   # Project specific
   temp/
   *.log
   EOF
   ```

2. **Test with temporary files**
   ```bash
   # Create files that should be ignored
   mkdir __pycache__
   touch temp_file.log
   touch temp/file.txt

   # Check git status
   git status
   ```

   These files should NOT appear in status.

3. **Commit .gitignore**
   ```bash
   git add .gitignore
   git commit -m "Add .gitignore"
   git push
   ```

4. **Verify on GitHub**
   - Visit repository
   - Confirm __pycache__ and temp/ don't appear in file list

**Verification Checklist:**
- [ ] .gitignore file created
- [ ] Temporary files are properly ignored
- [ ] .gitignore pushed to GitHub
- [ ] Repository doesn't track ignored files

---

### Exercise 3: Clone and Explore a Repository

**Objective:** Practice cloning an open source repository

**Instructions:**

1. **Find a repository to clone**
   Go to github.com and find an interesting project

2. **Clone it**
   ```bash
   # Create a learning directory
   mkdir ~/learning
   cd ~/learning

   git clone https://github.com/[owner]/[repo].git
   cd [repo]
   ```

3. **Explore the structure**
   ```bash
   ls -la          # View files
   cat README.md   # Read README
   git log --stat  # View history
   ```

4. **Understand the project**
   - What does it do?
   - What files does it have?
   - How many commits?
   - Who contributes?

**Verification Checklist:**
- [ ] Repository cloned successfully
- [ ] All files present locally
- [ ] Can view README and commit history
- [ ] Understand project purpose

---

### Exercise 4: Understand File Ignoring in Practice

**Objective:** See how .gitignore prevents tracking

**Instructions:**

1. **Create a test scenario**
   ```bash
   cd your-repo
   
   # Create files
   echo "secret_key=12345" > .env
   pip install -r requirements.txt  # Creates venv/
   touch debug.log
   ```

2. **No .gitignore - see what would be tracked**
   ```bash
   git status
   # You'd see .env, venv/, debug.log listed
   ```

3. **With .gitignore - they're ignored**
   ```bash
   # View your .gitignore from previous exercise
   cat .gitignore
   
   # Check status again
   git status
   # .env, venv/, debug.log should NOT appear
   ```

4. **Understanding the benefit**
   - Security: `.env` not in version control
   - Size: `venv/` not stored in history
   - Clarity: Only important files tracked

**Verification Checklist:**
- [ ] Can create and manage ignored files
- [ ] Understand why certain files are important to ignore
- [ ] Repository only tracks necessary files

---

## Command Reference

| Command | Purpose |
|---------|---------|
| `git clone <url>` | Download repository |
| `git status` | Check tracked files |
| `git add .` | Stage all (respecting .gitignore) |
| `git log --stat` | View commit details |

---

## Best Practices

✅ Always include a comprehensive README
✅ Use .gitignore to exclude dependencies and secrets
✅ Keep repository structure organized
✅ Add meaningful commit messages
✅ Set branch protection rules

❌ Don't commit API keys or passwords
❌ Don't ignore files you should track
❌ Don't mix unrelated changes in one commit

---

## Key Takeaways

✅ README is crucial for project documentation
✅ .gitignore prevents tracking unwanted files
✅ Repository settings control access and workflows
✅ Cloning allows you to work with others' projects
✅ Proper structure makes projects maintainable

---

## Next Steps

You've mastered local Git and GitHub basics! 

**Chapter 2** covers **Collaboration Workflows** including:
- Pull Requests
- Code Reviews
- Working in teams

These represent real-world development practices.

---

**[← Back to Module 1](./Module-1-Remote-Operations.md)** | **[Next: Chapter 2 →](../Chapter-2-Collaboration-Workflows/README.md)**
