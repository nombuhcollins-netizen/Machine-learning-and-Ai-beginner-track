# Chapter 3: Advanced Topics

**Total Duration:** 1.5 hours | **Difficulty:** Intermediate to Advanced

---

## Chapter Overview

This chapter covers advanced Git and GitHub features that power-users and senior developers rely on. You'll learn techniques for managing complex histories, organizing work, and using GitHub's advanced capabilities.

---

## Learning Outcomes

By the end of this chapter, you will be able to:

✅ Rebase branches and clean history
✅ Use stashing to save work temporarily
✅ Tag releases and versions
✅ Manage complex merge scenarios
✅ Use advanced GitHub features
✅ Optimize workflows for your team

---

## Module Breakdown

### Module 0: Rebasing & History Management
**Duration:** 30 minutes | **Difficulty:** Intermediate

Master interactive rebasing and maintaining clean commit history.

- Rebasing vs merging
- `git rebase` command
- Interactive rebasing
- Squashing commits
- Rewriting history safely

**Prerequisites:** Complete Chapter 2

[→ Open Module 0](./Module-0-Rebasing-and-History.md)

---

### Module 1: Stashing & Tags
**Duration:** 30 minutes | **Difficulty:** Intermediate

Learn temporary storage and version marking.

- What is stashing?
- `git stash` workflow
- Applying and popping stashes
- Tags and releases
- Semantic versioning
- Release management

**Prerequisites:** Complete Module 0

[→ Open Module 1](./Module-1-Stashing-and-Tags.md)

---

### Module 2: GitHub Advanced Features
**Duration:** 30 minutes | **Difficulty:** Intermediate

Leverage GitHub's powerful collaboration tools.

- GitHub Actions (CI/CD)
- GitHub Pages (hosting)
- Branch protection rules
- Status checks and required reviews
- GitHub Apps and integrations
- Advanced search

**Prerequisites:** Complete Module 1

[→ Open Module 2](./Module-2-GitHub-Advanced-Features.md)

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

## Key Concepts

| Concept | Definition |
|---------|-----------|
| **Rebase** | Replay commits on top of new base |
| **Interactive Rebase** | Edit commits during rebase |
| **Squash** | Combine multiple commits into one |
| **Stash** | Temporary storage for uncommitted changes |
| **Tag** | Named version mark in history |
| **Release** | Published version with notes |
| **CI/CD** | Automated testing and deployment |
| **Branch Protection** | Rules preventing direct main merges |

---

## When to Use Advanced Techniques

### Rebase/Clean History

- Cleaning up before merging to main
- Moving commits between branches
- Interactive rebasing for feature branches

### Stashing

- Switching branches with uncommitted changes
- Saving progress temporarily
- Cleaning working directory

### Tags

- Marking releases (v1.0, v1.1)
- Semantic versioning
- Creating release notes

### Branch Protection

- Protecting main branch
- Requiring reviews
- Running automated checks

---

## Exercise Overview

Each module includes practical exercises:

**Module 0 Exercises:**
- Rebase a feature branch
- Interactive rebase to clean commits
- Squash commits before merging

**Module 1 Exercises:**
- Stash changes and apply them
- Create version tags
- Create GitHub releases

**Module 2 Exercises:**
- Set up branch protection
- Configure required reviews
- Explore GitHub Actions

---

## Power User Workflow

```
Developer workflow with advanced techniques:

1. Create feature-login branch
2. Make messy commits (log is ugly)
3. Interactive rebase to clean it up
4. Rebase on latest main (if needed)
5. Push to GitHub
6. Create PR
7. Team reviews
8. Merge to main
9. Tag release: v1.2.0
10. GitHub Actions auto-deploys
```

---

## When You're Ready

These techniques are optional but powerful:

- **Beginners:** Chapters 0-2 are sufficient
- **Intermediate:** Add selective rebasing (Module 0)
- **Advanced:** Use all techniques fluently

You can use simpler workflows and still be productive!

---

## Getting Started

Ready for advanced techniques? Start with [Module 0: Rebasing & History Management](./Module-0-Rebasing-and-History.md)

---

## Quick Links

- [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Semantic Versioning](https://semver.org/)

---

## Chapter Navigation

- [← Back to Course Overview](../README.md)
- [Chapter 2: Collaboration](../Chapter-2-Collaboration-Workflows/README.md)
- [Final Project](./Final-Project.md)

---

## What Comes After

After completing this course:

- **Open Source:** Contribute to public projects
- **Team Development:** Join development teams
- **DevOps:** Learn CI/CD automation
- **Git Mastery:** Advanced techniques and workflows

---

Let's dive into advanced Git! [→ Module 0: Rebasing & History Management](./Module-0-Rebasing-and-History.md)
