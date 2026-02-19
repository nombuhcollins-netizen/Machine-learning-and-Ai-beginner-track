# Chapter 1: GitHub Fundamentals

**Total Duration:** 1.5 hours | **Difficulty:** Beginner to Intermediate

---

## Chapter Overview

This chapter moves from local Git to GitHub - the world's largest collaborative development platform. You'll learn how to create repositories on GitHub, connect them to your local Git, and work with remote repositories.

---

## Learning Outcomes

By the end of this chapter, you will be able to:

✅ Create GitHub repositories
✅ Connect local repositories to GitHub
✅ Push changes to remote
✅ Pull changes from remote
✅ Understand remote concepts
✅ Work with GitHub's interface

---

## Module Breakdown

### Module 0: GitHub Basics
**Duration:** 30 minutes | **Difficulty:** Beginner

Introduction to GitHub and setting up your account.

- What is GitHub?
- Creating a GitHub account
- Setting up SSH/HTTPS
- GitHub interface basics
- Creating your first repository

**Prerequisites:** Complete Chapter 0

[→ Open Module 0](./Module-0-GitHub-Basics.md)

---

### Module 1: Remote Repositories
**Duration:** 30 minutes | **Difficulty:** Beginner

Working with remote repositories and pushing/pulling.

- Understanding remotes
- `git remote` commands
- `git push` - Upload changes
- `git pull` - Download changes
- Tracking branches
- Synchronization

**Prerequisites:** Complete Module 0

[→ Open Module 1](./Module-1-Remote-Operations.md)

---

### Module 2: Repository Management
**Duration:** 30 minutes | **Difficulty:** Beginner

Managing GitHub repositories and collaborating.

- README files
- .gitignore files
- Repository settings
- Collaborators and permissions
- Forking repositories
- Cloning repositories

**Prerequisites:** Complete Module 1

[→ Open Module 2](./Module-2-Repository-Management.md)

---

## Time Allocation

```
Module 0: 30 minutes  [████░░████░░████░░████░░]
Module 1: 30 minutes  [████░░████░░████░░████░░]
Module 2: 30 minutes  [████░░████░░████░░████░░]
────────────────────────────────────────────
Total:   1.5 hours
```

---

## Prerequisites

- Completion of Chapter 0: Git Basics
- Your local Git installation and configuration
- A GitHub account (free) [Create here](https://github.com/signup)

---

## What You'll Need

- GitHub.com account
- SSH keys or HTTPS credentials setup
- Docker (not required, but useful)

---

## Key Concepts

| Concept | Definition |
|---------|-----------|
| **Remote** | A copy of your repository hosted elsewhere (GitHub) |
| **Origin** | Default name for your main remote repository |
| **Push** | Upload your local commits to remote |
| **Pull** | Download remote commits to local |
| **Clone** | Download entire repository from remote |
| **Fork** | Create your own copy of someone else's repository |
| **SSH/HTTPS** | Two ways to authenticate with GitHub |

---

## Exercise Overview

Each module includes practical exercises:

**Module 0 Exercises:**
- Create GitHub account
- Set up authentication
- Create first remote repository

**Module 1 Exercises:**
- Add GitHub as remote
- Push local code to GitHub
- Pull changes from GitHub
- Configure tracking branches

**Module 2 Exercises:**
- Create README.md
- Create .gitignore
- Configure repository settings
- Clone a repository
- Fork a repository

---

## Connected Workflow

```
Your Computer (Local)          GitHub (Remote)
┌──────────────────┐            ┌──────────────┐
│ my-first-repo    │  git push  │  my-first-repo
│                  │──────────→ │  (on GitHub)
│ Working Dir      │  git pull  │
│ Staging Area     │←─────────  │
│ Repository       │            │
└──────────────────┘            └──────────────┘
```

---

## Getting Started

Ready to connect to GitHub? Start with [Module 0: GitHub Basics](./Module-0-GitHub-Basics.md)

---

## Quick Links

- [GitHub Official Docs](https://docs.github.com)
- [GitHub Learning Lab](https://lab.github.com)
- [GitHub Skill Development](https://github.com/skills)

---

## Chapter Navigation

- [← Back to Course Overview](../README.md)
- [Chapter 0: Git Basics](../Chapter-0-Git-Basics/README.md)
- [Next: Chapter 2 →](../Chapter-2-Collaboration-Workflows/README.md)

---

## Tips for This Chapter

1. **Have your GitHub login ready** - You'll need to create an account
2. **Choose SSH or HTTPS** - Both work; SSH is more secure but requires setup
3. **Save your SSH key passphrase** - You'll need it for commits
4. **Test authentication** - Before moving forward, verify connectivity

---

## What Comes Next

After Chapter 1, you'll learn about:

- **Chapter 2:** Collaboration Workflows (Pull Requests, Code Reviews)
- **Chapter 3:** Advanced Topics (Rebasing, Stashing, Tags)

These chapters show real-world team collaboration patterns.

---

Let's proceed! [→ Module 0: GitHub Basics](./Module-0-GitHub-Basics.md)
