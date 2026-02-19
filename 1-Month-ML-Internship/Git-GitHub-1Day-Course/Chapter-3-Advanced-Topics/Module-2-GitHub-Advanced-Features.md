# Chapter 3 - Module 2: GitHub Advanced Features

**Duration:** 30 minutes | **Difficulty:** Intermediate

---

## Learning Objectives

By the end of this module, you will be able to:

1. Configure branch protection rules
2. Set up required status checks
3. Understand GitHub Actions basics
4. View advanced GitHub features
5. Use GitHub Issues effectively
6. Integrate tools with your repository

---

## Branch Protection Rules

### Why Protect Main?

Prevent accidents like:
- Direct pushes to main (bypass review)
- Merging untested code
- Deleting main branch
- Force-pushing changes

### Setting Up Protection

1. Go to repository **Settings** tab
2. Click **Branches** (left sidebar)
3. Click **Add rule** under "Branch protection rules"
4. **Branch name pattern:** `main` or `master`

### Protection Options

#### Require Pull Request Review

```
☑ Require a pull request before merging
  ☑ Require pull request reviews before merging
    Require 1 approvals
    ☑ Dismiss stale pull request approvals when new commits pushed
    ☑ Require review from code owners
```

**Effect:** Can't merge to main without at least 1 approval

#### Require Status Checks

```
☑ Require status checks to pass before merging
  ☑ Require branches to be up to date before merging
  
Select required status checks:
  ☑ continuous-integration/build
  ☑ continuous-integration/test
  ☑ Ensure code coverage doesn't decrease
```

**Effect:** All tests must pass before merging

#### Other Protection Options

```
☑ Include administrators
☑ Restrict who can push to matching branches
☑ Allow force pushes (only if truly needed)
☑ Allow deletions
```

### Example Setup

Safe production configuration:
1. Require 1 review
2. Require all tests passing
3. Require up-to-date with main
4. Include administrators

---

## GitHub Actions (CI/CD)

### What is CI/CD?

- **CI (Continuous Integration):** Automatically test code
- **CD (Continuous Deployment):** Automatically deploy code

### Basic Example

```yaml
name: Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
```

### How It Works

1. Code pushed or PR created
2. GitHub triggers workflow
3. Runs jobs (tests, linting, etc.)
4. Reports results to PR
5. Prevents merge if failing

### Status Checks in PR

```
✅ continuous-integration/pytest
✅ continuous-integration/linting
❌ coverage/codecov - Coverage decreased

Can't merge until all pass!
```

---

## Advanced Features

### 1. GitHub Mobile App

- Review PRs on phone
- Check build status
- Merge PRs
- Comment on issues

### 2. Code Owners

```
# .github/CODEOWNERS file

# API team reviews all API changes
/api/ @api-team

# Security team reviews security code
/security/ @security-team

# Documentation
*.md @documentation-team
```

When PR touches these files, code owners notified.

### 3. Pull Request Templates

```
# .github/pull_request_template.md

## Description
[What does this PR do?]

## Type of change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation

## Testing
[How was this tested?]

## Checklist
- [ ] Code reviewed
- [ ] Tests written
- [ ] Documentation updated
```

### 4. Issue Templates

Create consistent issue formats:
- Bug report template
- Feature request template
- General question template

### 5. Repository Settings

**Visibility:**
- Public (anyone can see)
- Private (only invited)

**Features:**
- Enable Discussions
- Enable Sponsorships
- Enable Projects

**Default Branch:**
- Usually `main`
- Can change for backward compatibility

**Archive Repository:**
- Mark as read-only
- When project is finished/deprecated

---

## GitHub Issues Advanced

### Issue Templates

Create `.github/ISSUE_TEMPLATE/` folder with:
- `bug_report.md`
- `feature_request.md`
- `blank.md`

### Linking Issues and PRs

In PR description:
```
Fixes #123
Closes #456
Resolves #789
```

When PR merges, linked issues auto-close.

### Issue Labels

Organize and categorize:
- `bug` - Something broken
- `feature` - New functionality
- `documentation` - Docs needed
- `good first issue` - For newcomers
- `help wanted` - Need community help

### Milestones

Group issues for releases:
- `v1.0.0` - Release 1.0
- `v2.0.0` - Release 2.0
- `Q1` - Quarter planning

### Project Boards

Kanban-style tracking:

```
To Do          In Progress       In Review       Done
├─ Issue #1    ├─ Issue #5       ├─ PR #12       ├─ Issue #2
├─ Issue #3    └─ Issue #7       └─ PR #15       └─ PR #20
└─ Issue #6                                      
```

### Automated Workflows

Card moves automatically based on:
- PR opened → moved to In Progress
- PR approved → moved to In Review
- PR merged → moved to Done

---

## GitHub Apps & Integrations

### Popular Integrations

1. **CodeClimate** - Code quality analysis
2. **Better Code Hub** - Code metrics
3. **Snyk** - Security scanning
4. **Codecov** - Coverage tracking
5. **Slack** - Notifications

### Adding Integration

1. Go to **Settings** > **Integrations & apps**
2. Search for app
3. Install
4. Authorize
5. Configure settings

### Webhook

Custom integration via webhooks:
```
When event happens (push, PR, etc.)
GitHub sends HTTP POST to your server
Your server processes the data
```

---

## Exercises

### Exercise 1: Set Up Branch Protection

**Objective:** Protect main branch

**Instructions:**

1. **Go to Settings**
   - Repository home → Settings tab

2. **Navigate to Branches**
   - Left sidebar → Branches

3. **Add protection rule**
   - Click "Add rule"
   - Pattern: `main`

4. **Configure protections**
   ```
   ☑ Require a pull request before merging
   ☑ Require approvals (set to 1)
   ☑ Dismiss stale reviews
   ☑ Require status checks (if using CI)
   ```

5. **Click "Create"**

6. **Test protection**
   - Try pushing to main directly
   - Should be rejected!
   - Must create PR instead

**Verification Checklist:**
- [ ] Branch protection rule created
- [ ] Visible in Settings > Branches
- [ ] Blocks direct pushes
- [ ] Requires PR to merge

---

### Exercise 2: Create GitHub Actions Workflow

**Objective:** Set up basic CI

**Instructions:**

1. **Create workflow file**
   ```
   .github/workflows/tests.yml
   ```

2. **Add basic workflow**
   ```yaml
   name: Tests
   
   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]
   
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v2
       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.9'
       - name: Install dependencies
         run: |
           pip install pytest
       - name: Run tests
         run: |
           pytest
   ```

3. **Commit and push**
   ```bash
   git add .github/workflows/tests.yml
   git commit -m "Add CI workflow"
   git push
   ```

4. **View on GitHub**
   - Go to "Actions" tab
   - See workflow running
   - Check results

**Verification Checklist:**
- [ ] Workflow file created
- [ ] File in .github/workflows/
- [ ] Committed and pushed
- [ ] Workflow visible in Actions tab

---

### Exercise 3: Create PR with Status Checks

**Objective:** See status checks in action

**Instructions:**

If you have GitHub Actions set up:

1. **Create feature branch**
   ```bash
   git switch -c feature-test
   ```

2. **Make code change**
   ```bash
   echo "test code" > test_file.py
   git add test_file.py
   git commit -m "Add test file"
   git push -u origin feature-test
   ```

3. **Create PR**
   - Go to GitHub
   - Click "Compare & pull request"
   - Create PR

4. **Observe checks**
   - PR shows status checks running
   - See "Checks" tab
   - Checks show pass/fail

5. **Merge when all pass**
   - If all checks pass
   - Can merge safely
   - Click "Merge pull request"

**Verification Checklist:**
- [ ] PR created
- [ ] Checks visible in PR
- [ ] Can see check results
- [ ] Merge possible when passing

---

## Essential Advanced Features

### Must Have

- ✅ Branch protection on main
- ✅ Require PR reviews
- ✅ Require status checks passing

### Very Useful

- ✅ GitHub Actions CI/CD
- ✅ Issue templates
- ✅ CODEOWNERS file
- ✅ PR templates

### Nice to Have

- ✅ GitHub Projects
- ✅ Issue labels
- ✅ Milestone tracking
- ✅ Third-party integrations

---

## Workflow with Protections

```
1. Developer creates feature branch
   ↓
2. Pushes commits
   ↓
3. Creates PR
   ↓
4. GitHub Actions runs tests
   ├─ Tests pass → ✅ Shows green check
   └─ Tests fail → ❌ Shows red X
   ↓
5. Code review happens
   ├─ Reviewer approves → ✅
   └─ OR requests changes → 🔄
   ↓
6. Once approved + tests pass
   → Merge button enabled
   ↓
7. Click merge
   → PR to main merged
   ↓
8. Tests run on main
   → Deploy automatically (if configured)
```

---

## Key Takeaways

✅ Branch protection prevents accidents
✅ Status checks ensure code quality
✅ GitHub Actions automate testing
✅ PR/Issue templates improve consistency
✅ Code owners ensure proper review
✅ Integrations extend functionality

---

## Best Practices

1. **Always protect main branch**
2. **Require reviews from humans**
3. **Run automated tests on all PRs**
4. **Use issue templates for consistency**
5. **Document with CODEOWNERS**
6. **Track progress with milestones**

---

## Next Steps

You've now learned advanced GitHub features! Review the course and practice.

---

## Course Completion

**Congratulations!** You've completed the entire Git & GitHub 1-Day course:

✅ Chapter 0: Git Basics
✅ Chapter 1: GitHub Fundamentals
✅ Chapter 2: Collaboration Workflows
✅ Chapter 3: Advanced Topics

---

## Where to Go From Here

### Deepen Your Knowledge

- **Git Cherry-pick:** Move specific commits
- **Git Bisect:** Find bugs in history
- **Submodules:** Include other repos
- **Hooks:** Automate tasks

### Level Up Your Skills

- **DevOps:** Learn deployment pipelines
- **Cloud:** Deploy to AWS, Azure, GCP
- **Containers:** Docker + Kubernetes

### Contribute

- **Open Source:** Find projects on GitHub
- **Communities:** Join developer groups
- **Mentorship:** Learn from experienced developers

---

## Resources

- [Pro Git Book](https://git-scm.com/book) - Free, comprehensive
- [GitHub Learning Lab](https://lab.github.com) - Interactive tutorials
- [Atlassian Tutorials](https://www.atlassian.com/git) - Excellent guides
- [GitHub Docs](https://docs.github.com) - Official documentation

---

## Final Advice

🚀 **Keep Practicing**
- Every project is learning
- Mistakes are learning opportunities
- Repetition builds mastery

💡 **Stay Curious**
- Explore open source
- Read others' code
- Learn from the community

🤝 **Help Others**
- Answer questions
- Mentor junior developers
- Contribute to projects

---

## Thank You!

You're now equipped to:
- Version control professionally
- Collaborate effectively
- Automate workflows
- Contribute to open source
- Lead development teams

Good luck on your coding journey! 🎉

---

**[← Back to Module 1](./Module-1-Stashing-and-Tags.md)** | **[← Course Overview](../README.md)**
