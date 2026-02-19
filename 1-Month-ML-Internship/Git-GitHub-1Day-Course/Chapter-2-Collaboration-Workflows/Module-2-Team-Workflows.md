# Chapter 2 - Module 2: Team Workflows

**Duration:** 40 minutes | **Difficulty:** Intermediate

---

## Learning Objectives

By the end of this module, you will be able to:

1. Understand common team workflows
2. Implement feature branch workflow
3. Use GitHub issues for planning
4. Handle parallel development
5. Manage conflicts in team settings
6. Communicate effectively with teams

---

## Common Team Workflows

### 1. GitHub Flow (Simple Teams)

Used by GitHub, Shopify, and many startups.

```
main (production)
       ↑ PR ← feature-1 ← developer 1
       ↑ PR ← feature-2 ← developer 2
       ↑ PR ← feature-3 ← developer 3
```

**Process:**
1. Create branch from main: `feature-login`
2. Commit and push
3. Create PR
4. Team reviews
5. Merge to main
6. Deploy from main

**Good for:** Small teams, continuous deployment

---

### 2. GitFlow (Complex Projects)

Used by larger teams with release planning.

```
main (production) ← hotfix-1
       ↑
       ← release-1
       ↑
develop (staging)
       ↑ PR ← feature-1
       ↑ PR ← feature-2
       ↑ PR ← bugfix-1
```

**Branches:**
- `main` - Production releases
- `develop` - Integration branch
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `release/*` - Release preparation
- `hotfix/*` - Emergency production fixes

**Process:**
1. Develop features on `feature/*` branches
2. Merge to `develop` when complete
3. Create `release/*` branch for testing
4. Merge to `main` at release
5. Patch with `hotfix/*` if needed

**Good for:** Large teams, scheduled releases

---

### 3. Trunk-Based Development

Used by Microsoft, Google, Facebook.

```
main
       ← small-feature-1 (1-2 days)
       ← small-feature-2 (1-2 days)
       ← small-PR (hours)
       ← small-PR (hours)
```

**Process:**
1. Very short-lived branches (hours/days, not weeks)
2. Frequent small commits to main
3. Feature flags for incomplete features
4. Heavy continuous integration (CI)

**Good for:** High-performing teams, microservices

---

## Using GitHub Issues for Planning

### Create Issues

**Example Issue:**

```markdown
# Add user authentication

## Description
Users need to log in to access their personalized content.

## Requirements
- [ ] Login form UI
- [ ] Password hashing
- [ ] Session management
- [ ] Email verification

## Acceptance Criteria
- User can register with email and password
- User can reset forgotten password
- Session expires after 24 hours
- Passwords are securely hashed

## Resources
- Design mockup: [link]
- API documentation: [link]

## Labels
feature, backend, authentication

## Assigned
@john-developer

## Milestone
v1.0 Release
```

### Link PRs to Issues

When creating PR:
```markdown
Fixes #42
Closes #43
Resolves #44
```

### Track Progress with Projects

GitHub Projects (Kanban Board):

```
To Do          In Progress       In Review       Done
├─ Issue #1    ├─ Issue #5       ├─ PR #12      ├─ Issue #2
├─ Issue #3    ├─ Issue #7       ├─ PR #15      ├─ Issue #4
└─ Issue #6    └─ Issue #8                      └─ PR #20
```

---

## Handling Parallel Development

### Scenario: Multiple Features

```
Developer A: feature-search
Developer B: feature-filters  
Developer C: feature-share

All start from main, work independently
```

**Ensuring no conflicts:**

1. **Different files** - Easiest, rarely conflict
2. **Same file, different sections** - Can be merged
3. **Same section** - Will conflict, needs discussion

### Preventing Conflicts

**Good:**
```
Developer A: src/search.py
Developer B: src/filter.py
Developer C: src/share.py
```

**Problematic:**
```
Developer A: main.py (edit line 50-100)
Developer B: main.py (edit line 50-100)
```

### Team Communication

Before starting feature:
```markdown
@team I'm starting work on search functionality in 
src/search.py. Planning to finish by Friday. Will 
need review then.

@john Don't modify src/search.py until I create the PR!
```

---

## Resolving Merge Conflicts in Team Setting

### Conflict Happens During PR Review

```
main has: main.py v1
Your PR has: main.py v2
But someone else merged v1.5!

Result: Conflict when merging PR
```

### Resolve Conflict

1. **Update your branch**
   ```bash
   git switch feature-X
   git pull  # Update main
   git merge main
   # Git shows conflicts
   ```

2. **Fix conflicts**
   ```
   main.py has conflict markers
   Edit to choose which version to keep
   ```

3. **Test thoroughly**
   ```bash
   # Ensure merged code still works
   python tests/test_main.py
   ```

4. **Commit the merge**
   ```bash
   git add main.py
   git commit -m "Merge main and resolve conflicts"
   git push
   ```

5. **PR updates automatically**
   PR now shows "No conflicts" and is mergeable

---

## Handling Large Scalability

### When Team is 5+ Developers

**Establish rules:**

1. **Code review requirements**
   - How many reviewers?
   - Who can approve merge?
   - Automatic checks required?

2. **Branch naming conventions**
   ```
   feature/user-auth
   bugfix/login-error
   hotfix/payment-crash
   docs/api-guide
   ```

3. **Commit message standards**
   ```
   feat: Add user authentication
   fix: Resolve login button styling
   docs: Update API documentation
   ```

4. **Release management**
   - When can we merge to main?
   - When do we deploy?
   - Who gives final approval?

---

## Team Communication Tools

### In Pull Request

```markdown
@john-lead Can you review when you get a chance?
@jane-qa Please verify the testing scenario in the description.
@team This touches the authentication system - review carefully!
```

### Use Labels and Milestones

**Labels:** `bug`, `feature`, `documentation`, `urgent`
**Milestones:** `v1.0`, `Q1 Release`, `Critical Path`

### Sync Regularly

- Daily standups: "What are you working on?"
- Weekly: Review open PRs
- Monthly: Retrospectives on workflow

---

## Exercises

### Exercise 1: Create GitHub Issues

**Objective:** Plan features using GitHub Issues

**Instructions:**

1. **Go to Issues tab** on your repository

2. **Create 3 issues:**

   **Issue 1: Feature**
   ```markdown
   # Add contact form
   
   Users should be able to submit contact requests.
   
   ## Requirements
   - [ ] Form with name, email, message
   - [ ] Email validation
   - [ ] Confirmation message
   
   ## Labels
   feature, frontend
   ```

   **Issue 2: Bug**
   ```markdown
   # Fix navigation menu on mobile
   
   Menu doesn't display correctly on small screens.
   
   ## Steps to Reproduce
   1. View site on mobile
   2. Menu appears broken
   
   ## Expected Behavior
   Menu should be responsive
   
   ## Labels
   bug, frontend
   ```

   **Issue 3: Documentation**
   ```markdown
   # Document API endpoints
   
   Developers need clear API documentation.
   
   ## Endpoints to Document
   - [ ] GET /api/users
   - [ ] POST /api/users
   - [ ] GET /api/posts
   
   ## Labels
   documentation, backend
   ```

3. **Navigate Issues**
   - Use labels to filter
   - Sort by priority
   - Assign to yourself

**Verification Checklist:**
- [ ] 3 issues created
- [ ] Each has clear description
- [ ] Labels applied
- [ ] Can filter by labels

---

### Exercise 2: Implement Feature Branch Workflow

**Objective:** Practice team workflow locally

**Instructions:**

1. **Create 3 feature branches**
   ```bash
   git switch main
   git switch -c feature-contact-form
   ```

2. **On feature-contact-form:**
   ```bash
   touch contact_form.py
   echo "# Contact Form Implementation" > contact_form.py
   git add contact_form.py
   git commit -m "feat: Add contact form"
   git push -u origin feature-contact-form
   ```

3. **Back to main, create another feature:**
   ```bash
   git switch main
   git switch -c feature-mobile-responsive
   
   touch mobile_responsive.css
   echo "/* Mobile styles */" > mobile_responsive.css
   git add mobile_responsive.css
   git commit -m "feat: Add mobile responsive styles"
   git push -u origin feature-mobile-responsive
   ```

4. **View branches on GitHub**
   - Go to Code tab
   - Click "Branches"
   - Should see 3 branches:
     - `main`
     - `feature-contact-form`
     - `feature-mobile-responsive`

5. **Create PRs for both features**
   For each branch:
   - Go to GitHub
   - Click "New pull request"
   - Fill in title and description
   - Link related issue
   - Create PR

**Verification Checklist:**
- [ ] Multiple feature branches created
- [ ] Each branch has commits
- [ ] PRs created for features
- [ ] PRs link to issues

---

### Exercise 3: Simulate Team Merge

**Objective:** Handle multiple PRs merging

**Instructions:**

1. **Have 2+ PRs open** (from Exercise 2)

2. **Merge first PR:**
   - Go to first PR
   - Click "Merge pull request"
   - Confirm merge
   - Delete branch

3. **Check second PR:**
   - Go to second PR
   - Click "Files changed"
   - Should say "No conflicts" (same files)
   - Merge this PR too

4. **Verify on main:**
   ```bash
   git switch main
   git pull
   git log --oneline -n 5
   # Should show 2 merge commits
   
   ls -la
   # Should show both new files
   ```

5. **Clean up local:**
   ```bash
   git branch -a
   # Should show remote branches deleted
   
   git branch -v
   # Delete stale local branches
   git branch -d feature-contact-form
   ```

**Verification Checklist:**
- [ ] Both PRs merged
- [ ] No conflicts (or resolved)
- [ ] Main has all changes
- [ ] Branches properly cleaned up

---

## Workflow Comparison

| Aspect | GitHub Flow | GitFlow |
|--------|-------------|---------|
| Complexity | Simple | Complex |
| Branch Types | Few | Many |
| Team Size | Small (2-5) | Large (5+) |
| Deployment | Continuous | Scheduled |
| Release Frequency | Frequent | Planned |
| Setup Time | Minutes | Hours |

---

## Key Takeaways

✅ Choose workflow matching team size and needs
✅ Use GitHub Issues to plan work
✅ Link PRs to issues for tracking
✅ Communicate with team before starting work
✅ Resolve conflicts in team setting carefully
✅ Establish team agreements (labels, branches, reviews)

---

## Team Agreements to Make

1. **Workflow:** Which pattern do we use?
2. **Branch names:** What's the convention?
3. **PR process:** How many reviewers? Automatic checks?
4. **Commit messages:** What should they look like?
5. **Deployment:** When and how?
6. **On-call:** Who handles production issues?

---

## Next Steps

You've learned the complete collaboration workflow! **Chapter 3** covers advanced topics:
- Rebasing and history management
- Stashing and tags
- GitHub advanced features

---

**[← Back to Module 1](./Module-1-Code-Reviews.md)** | **[Next: Chapter 3 →](../Chapter-3-Advanced-Topics/README.md)**
