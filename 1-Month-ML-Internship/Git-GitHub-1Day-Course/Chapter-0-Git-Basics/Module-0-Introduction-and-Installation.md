# Chapter 0 - Module 0: Introduction & Installation

**Duration:** 30 minutes | **Difficulty:** Beginner

---

## Learning Objectives

By the end of this module, you will be able to:

1. Understand what Git is and why it's important
2. Install Git on your system
3. Configure Git with your credentials
4. Verify your installation

---

## What is Git?

Git is a **distributed version control system (VCS)** that allows you to:
- Track changes in your code
- Collaborate with other developers
- Maintain a complete history of your project
- Revert to previous versions if needed
- Work on multiple features simultaneously

### Why Git?

- **Distributed:** Every developer has a full copy of the repository
- **Fast:** Local operations are rapid
- **Reliable:** Built-in data integrity
- **Industry Standard:** Used by 90%+ of development teams

---

## Installation Guide

### Windows

1. Download from [git-scm.com](https://git-scm.com/download/win)
2. Run the installer
3. Accept defaults or customize as needed
4. Complete installation

### macOS

```bash
# Using Homebrew
brew install git

# Or download from git-scm.com/download/mac
```

### Linux

```bash
# Ubuntu/Debian
sudo apt-get install git

# Fedora
sudo dnf install git
```

---

## Initial Configuration

After installation, configure your identity:

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list
```

---

## Exercises

### Exercise 1: Install & Configure Git

**Objective:** Install Git and set up your credentials

**Steps:**
1. Download and install Git for your operating system
2. Open your terminal/command prompt
3. Run: `git --version` (should show version 2.30+)
4. Configure your name and email as shown above
5. Verify configuration with `git config --list`

**Expected Output:**
```
git version 2.40.0 (or similar)
user.name=Your Name
user.email=your.email@example.com
```

**Verification Checklist:**
- [ ] Git is installed
- [ ] Git version is 2.30 or higher
- [ ] Your name is configured
- [ ] Your email is configured
- [ ] `git config --list` shows your settings

---

### Exercise 2: Understand Git Concepts

**Objective:** Familiarize yourself with Git terminology

**Read and explain the following terms:**

1. **Repository (Repo)** - A folder containing version history
2. **Commit** - A snapshot of changes
3. **Branch** - An independent line of development
4. **Remote** - A hosted version of your repository
5. **Pull** - Fetch and integrate remote changes
6. **Push** - Send local changes to remote

Write a 2-3 sentence explanation for each term in your own words.

---

## Key Takeaways

✅ Git is a version control system essential for modern development
✅ Installation is straightforward on all platforms
✅ Configuration with your identity is the first step
✅ Verification ensures everything is set up correctly

---

## Next Steps

Once you've completed these exercises, move on to **Module 1: Core Concepts** to understand the fundamental principles of Git.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Command not found | Git may not be installed. Reinstall or check PATH |
| Wrong user info | Run `git config --global user.name "New Name"` |
| Need to check settings | Run `git config --list` |

---

**[← Back to Chapter 0 Overview](./README.md)** | **[Next: Module 1 →](./Module-1-Core-Concepts.md)**
