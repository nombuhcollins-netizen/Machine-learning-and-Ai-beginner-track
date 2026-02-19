# Final Project: Complete Git & GitHub Workflow

## Project Overview

This project brings together everything you've learned in the 1-day Git & GitHub course. You'll create a complete project using professional Git and GitHub practices.

**Duration:** 1-2 hours | **Difficulty:** Intermediate

---

## Project Goals

By completing this project, you will demonstrate:

✅ Local version control (commits, branches, history)
✅ Remote repository management (push, pull, sync)
✅ Collaborative workflow (PRs, reviews, merging)
✅ Professional practices (branch protection, issues, releases)

---

## Project Scenario

You're building a simple Python project called "Task Manager" - a command-line to-do list application.

### Features to Implement

**MVP (Minimum Viable Product):**
1. Add tasks to a list
2. View all tasks
3. Mark tasks as complete
4. Delete tasks
5. Save tasks to file

**Bonus features:**
- Task priorities
- Due dates
- Search/filter

---

## Part 1: Project Setup (30 minutes)

### 1.1 Create Local Repository

```bash
# Create directory
mkdir task-manager
cd task-manager

# Initialize Git
git init

# Create initial structure
mkdir src
touch README.md
touch .gitignore

# Configure Git
git config user.name "Your Name"
git config user.email "your@email.com"
```

### 1.2 Create README.md

```markdown
# Task Manager

A simple command-line task management application.

## Features

- ✅ Add tasks
- ✅ View tasks
- ✅ Mark tasks complete
- ✅ Delete tasks
- 💾 Persistent storage

## Installation

```bash
python task_manager.py
```

## Usage

```
$ python task_manager.py
1. Add Task
2. View Tasks
3. Mark Complete
4. Delete Task
5. Exit

Enter choice: 1
```

## Contributing

See CONTRIBUTING.md

## License

MIT License
```

### 1.3 Create .gitignore

```
# Python
__pycache__/
*.pyc
*.pyo
venv/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Project
tasks.json
```

### 1.4 Initial Commit

```bash
git add .
git commit -m "Initial project setup"

# Verify
git log --oneline
```

---

## Part 2: GitHub Setup (15 minutes)

### 2.1 Create GitHub Repository

1. Go to github.com
2. Click "+" → "New repository"
3. Name: `task-manager`
4. PUBLIC
5. Don't initialize with README (we have one)
6. Create

### 2.2 Connect Local to Remote

```bash
git remote add origin https://github.com/YOUR-USERNAME/task-manager.git
git branch -M main
git push -u origin main
```

### 2.3 Verify on GitHub

- Visit your repository
- Should see README displayed
- Verify all files present

---

## Part 3: Feature Development (45 minutes)

### 3.1 Create Feature Branch

```bash
git switch -c feature/core-functions
```

### 3.2 Implement Core Functions

Create `src/task_manager.py`:

```python
"""Task Manager Application"""

import json
import os
from datetime import datetime


class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_tasks(self):
        """Save tasks to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, title, description=""):
        """Add new task"""
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'completed': False,
            'created': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def list_tasks(self):
        """List all tasks"""
        return self.tasks
    
    def complete_task(self, task_id):
        """Mark task as complete"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                return task
        return None
    
    def delete_task(self, task_id):
        """Delete task"""
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        self.save_tasks()


if __name__ == '__main__':
    manager = TaskManager()
```

### 3.3 Stage and Commit

```bash
git add src/task_manager.py
git commit -m "Implement core task manager functions"

# Commit again if needed
echo "# Implementation notes" >> docs/DEVELOPMENT.md
git add docs/DEVELOPMENT.md
git commit -m "Add development documentation"
```

### 3.4 View Branch

```bash
git log --oneline
# Shows your commits on feature branch

git log --graph --all --oneline
# Shows feature branch separate from main
```

### 3.5 Push Feature Branch

```bash
git push -u origin feature/core-functions
```

---

## Part 4: Create Pull Request (30 minutes)

### 4.1 Create PR on GitHub

1. Go to github.com/YOUR-USERNAME/task-manager
2. See notification about feature branch
3. Click "Compare & pull request"

### 4.2 Fill PR Details

**Title:**
```
Add core task manager functionality
```

**Description:**
```markdown
## Description
Implements core task management features including 
adding, viewing, and managing tasks.

## Changes
- Implemented TaskManager class
- Added task persistence with JSON
- Created core functions:
  - add_task()
  - list_tasks()
  - complete_task()
  - delete_task()

## Testing
- Tested add/list/complete/delete operations
- Verified file persistence
- No breaking changes

## Closes
#1
```

### 4.3 Review Your Own PR

1. Go to "Files changed"
2. Add 2-3 comments:
   ```
   This function is well-designed and clear.
   ```

3. Request changes (simulate review):
   - Click "Review changes"
   - Select "Request changes"
   - Comment:
     ```
     Need to add error handling for file operations.
     ```

### 4.4 Address Feedback

```bash
# On feature branch
# Add error handling
echo "# Better error handling" >> src/task_manager.py

git add src/task_manager.py
git commit -m "Add error handling for file operations"
git push

# Go back to PR
# Change review from "Request changes" to "Approve"
```

### 4.5 Merge PR

1. After approving (or when satisfied)
2. Click "Merge pull request"
3. Check "Delete branch"
4. Confirm merge

### 4.6 Verify Merge

```bash
git switch main
git pull
git log --oneline
# Should show merge commit

ls src/
# Should see task_manager.py
```

---

## Part 5: Advanced Workflow (30 minutes)

### 5.1 Create Second Feature Branch

```bash
git switch -c feature/cli-interface

# Create CLI script
cat > src/cli.py << 'EOF'
"""Command-line interface for Task Manager"""

from task_manager import TaskManager


def main():
    manager = TaskManager()
    
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ")
        
        if choice == '1':
            title = input("Task title: ")
            manager.add_task(title)
            print("✓ Task added")
        
        elif choice == '2':
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks")
            else:
                for task in tasks:
                    status = "✓" if task['completed'] else "○"
                    print(f"{status} {task['id']}. {task['title']}")
        
        elif choice == '5':
            break


if __name__ == '__main__':
    main()
EOF

git add src/cli.py
git commit -m "Add command-line interface"
```

### 5.2 Interactive Rebase to Clean

```bash
# Let's say we made messy commits; clean them up
git rebase -i HEAD~2

# In editor, squash or reword commits
# For learning, just close and continue
```

### 5.3 Create Release

```bash
# Tag version
git tag -a v1.0.0 -m "First release - Core features"

# Push tag
git push origin v1.0.0
```

### 5.4 Create Release on GitHub

1. Go to "Releases" tab
2. Click "Draft a new release"
3. **Tag:** v1.0.0 (should be pre-selected)
4. **Title:** Version 1.0.0 - Task Manager MVP
5. **Description:**
   ```markdown
   ## Features
   - Add, view, complete, delete tasks
   - Persistent storage
   - Simple CLI interface
   
   ## Installation
   ```bash
   git clone https://github.com/YOUR-USERNAME/task-manager.git
   cd task-manager
   python src/cli.py
   ```
   ```
6. Publish Release

---

## Part 6: Documentation & Best Practices (15 minutes)

### 6.1 Create CONTRIBUTING.md

```markdown
# Contributing to Task Manager

Thank you for interest in contributing!

## How to Contribute

1. Fork the repository
2. Create feature branch: `git switch -c feature/your-feature`
3. Commit changes: `git commit -m "Add feature"`
4. Push branch: `git push origin feature/your-feature`
5. Create pull request

## Code Style

- Use Python PEP 8
- Write docstrings
- Add comments for complex logic

## Testing

Add tests for new features.

## Questions?

Create an issue to discuss ideas.
```

### 6.2 Set Up Branch Protection

(Only if repository is public and you want to demonstrate this)

1. Settings → Branches
2. Add rule for `main`
3. Require pull request before merging
4. Save

### 6.3 Create Issues

Create GitHub Issues for ideas:

1. **Issue #1:** Add task priority feature
2. **Issue #2:** Add due dates
3. **Issue #3:** Improve error messages

---

## Part 7: Documentation & Reflection (15 minutes)

### 7.1 Create LEARNING.md

Document your learning:

```markdown
# Learning Outcomes

## Completed Skills

- [x] Local version control (commits, branches)
- [x] Remote repositories (push, pull)
- [x] Pull requests and code review
- [x] Merging and rebasing
- [x] Tagging and releases
- [x] Best practices (branch protection, issues)

## Key Learnings

1. **Commits:** Clear messages help future you
2. **Branches:** One feature per branch keeps things clean
3. **Pull requests:** Code review catches issues early
4. **History:** Clean commits are easier to understand

## Challenges Faced

- ...

## Next Steps

- Add tests
- Implement bonus features
- Deploy to web
```

### 7.2 View Final Repository

```bash
# View all commits
git log --oneline -n 10

# View graph
git log --graph --all --oneline

# Count commits
git log --oneline | wc -l
```

---

## Verification Checklist

### Must Have

- [ ] Local Git repository initialized
- [ ] README.md created and committed
- [ ] .gitignore properly configured
- [ ] Code pushed to GitHub
- [ ] Feature branch created and merged via PR
- [ ] Commits have clear messages
- [ ] PR has descriptive title and description

### Should Have

- [ ] Performed code review on own PR
- [ ] Addressed review feedback
- [ ] Clean commit history
- [ ] Branch protection on main

### Nice to Have

- [ ] Created release with tag
- [ ] Created GitHub Issues
- [ ] Professional documentation
- [ ] Multiple features merged

---

## Completion Requirements

**Project is complete when you have:**

1. ✅ Repository on GitHub with meaningful commits
2. ✅ At least 2 merged pull requests
3. ✅ Clear README and documentation
4. ✅ At least 1 release/tag created
5. ✅ Demonstrated code review process
6. ✅ Clean git history

---

## What You've Demonstrated

By completing this project you've shown:

🎯 **Version Control Mastery**
- Creating and managing repositories
- Commit discipline
- Branch strategy

🎯 **Collaboration Skills**
- Pull requests
- Code review process
- Addressing feedback

🎯 **Professional Practices**
- Clear documentation
- Release management
- Git workflow

---

## Extending the Project

### Next Features

1. **Testing:** Add unit tests with pytest
2. **CI/CD:** GitHub Actions to run tests
3. **Deployment:** Deploy to web
4. **Database:** Upgrade from JSON to database
5. **API:** REST API instead of CLI

### Learning Paths

- **DevOps:** Docker, Kubernetes, deployment
- **Web:** Flask API, web interface  
- **Testing:** pytest, coverage, mocking
- **Open Source:** Publish and share

---

## Getting Help

If you get stuck:

1. **Review course materials** - Go back to relevant chapters
2. **Check Git documentation** - `git help <command>`
3. **Google the error** - Copy exact error message
4. **Ask for help** - Twitter, Reddit, Stack Overflow

---

## Celebrate Your Success! 🎉

You've completed a professional Git & GitHub workflow! This is a valuable skill that will serve you throughout your career.

### What You Can Do Now

✅ Manage code with Git
✅ Collaborate on teams via GitHub
✅ Follow professional workflows
✅ Review and be reviewed
✅ Manage releases

---

## Share Your Work

Consider:

1. **GitHub Profile** - Display your project
2. **Portfolio** - Link to project
3. **Resume** - Mention version control skills
4. **Open Source** - Contribute to projects
5. **Blog** - Write about what you learned

---

## Further Learning

### Immediate Next Steps

- Practice with different projects
- Contribute to open source
- Learn CI/CD (GitHub Actions)
- Master advanced Git techniques

### Resources

- [Pro Git Book](https://git-scm.com/book)
- [GitHub Learning Lab](https://lab.github.com)
- [Atlassian Tutorials](https://www.atlassian.com/git)
- [Real-world projects on GitHub](https://github.com/explore)

---

## Final Thoughts

Git and GitHub are powerful tools embraced by developers worldwide. The skills you've learned today are:

- **In Demand:** Every job needs version control
- **Timeless:** Git isn't going away
- **Valuable:** Separates professionals from hobbyists
- **Universal:** Works across all tech stacks

Keep practicing, contribute to open source, and level up your development skills.

---

## Thank You for Completing the Course! 🚀

You're now equipped to work professionally with code, collaborate with teams, and contribute to the global developer community.

**Next: Start a new project and apply what you've learned!**

---

**[← Back to Course Overview](./README.md)**
