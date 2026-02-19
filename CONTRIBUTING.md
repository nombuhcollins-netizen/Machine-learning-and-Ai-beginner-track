# 🤝 Contributing Guide

Thank you for your interest in contributing to the **1-Month ML Internship Program**! This guide explains how to improve the curriculum, add resources, fix errors, or contribute in other ways.

---

## 📋 Table of Contents

1. [How to Contribute](#how-to-contribute)
2. [Types of Contributions](#types-of-contributions)
3. [Getting Started](#getting-started)
4. [Contribution Process](#contribution-process)
5. [Style Guides](#style-guides)
6. [Code of Conduct](#code-of-conduct)

---

## 🎯 How to Contribute

### For Students
- **Find errors or typos** - Report or fix them
- **Resource suggestions** - Recommend great learning links
- **Exercise improvements** - Suggest better exercises or solutions
- **Real-world projects** - Share completed projects for portfolio
- **Documentation** - Improve chapter explanations

### For Instructors/Mentors
- **Chapter content** - Expand with new sections or depth
- **Example datasets** - Add realistic data sources
- **Assessment rubrics** - Create grading guidelines
- **Solutions** - Develop answer keys for exercises
- **Visual aids** - Add diagrams, flowcharts, infographics

### For Developers
- **Automation** - Create testing/validation scripts
- **Tools** - Build helper tools for students
- **Deployment** - Improve CI/CD and GitHub workflows
- **Documentation** - Enhance setup guides and troubleshooting

---

## 🌟 Types of Contributions

### 1️⃣ Bug Reports
**Found something broken?**

- **Title:** `[BUG] Brief description`
- **Description:** Include:
  - What you expected vs what happened
  - Steps to reproduce
  - Your system info (OS, Python version)
  - Error messages/logs

### 2️⃣ Feature Requests
**Have an idea to improve content?**

- **Title:** `[FEATURE] What you want to add`
- **Description:**
  - Detailed explanation of the feature
  - Why it would be valuable
  - How students would use it
  - Rough outline/examples

### 3️⃣ Resource Recommendations
**Found an excellent tutorial or paper?**

- **Title:** `[RESOURCE] Topic area - Resource name`
- **Description:**
  - Link to resource
  - Brief description (1-2 sentences)
  - Why it's valuable (connects to which concept)
  - Difficulty level (Beginner/Intermediate/Advanced)

Example:
```markdown
[RESOURCE] NLP - Hugging Face NLP Course
https://huggingface.co/course

Free comprehensive NLP course covering transformers, fine-tuning, and production deployment.
Perfect companion to Chapter 1, Part 5 - "NLP Integration". Rated intermediate-advanced.
```

### 4️⃣ Content Improvements
**Can reword a concept more clearly?**

- **Title:** `[IMPROVE] Chapter X - What's being improved`
- **Description:**
  - Current text (if short) or location
  - Proposed improvement
  - Why it's clearer/better
  - For grammar fixes, be specific about changes

### 5️⃣ Exercise Problems & Solutions
**Want to improve or add exercises?**

For **new exercises:**
```markdown
[EXERCISE] Chapter X, Part Y - Topic name

**Difficulty:** Beginner/Intermediate/Advanced
**Time:** Estimated minutes

**Problem:**
[Clear problem statement]

**Starter Code (optional):**
[If helpful]

**Learning Objectives:**
- Objective 1
- Objective 2

**Hints (optional):**
- Hint 1
- Hint 2
```

For **contributions to SOLUTIONS:**
- Must work correctly
- Include comments explaining approach
- Show multiple solutions if applicable
- Follow code style (see below)

### 6️⃣ Code Contributions
**Improving scripts or adding examples?**

- **What:** Script/example/utility
- **Why:** What problem does it solve
- **Tests:** How to verify it works
- **Documentation:** Comments and docstrings
- **License:** Confirm it's compatible with MIT

---

## 🚀 Getting Started

### Step 1: Fork & Clone

```bash
# Fork on GitHub (via web interface)
git clone https://github.com/YOUR_USERNAME/seedai.git
cd seedai
git remote add upstream https://github.com/ORIGINAL_OWNER/seedai.git
```

### Step 2: Create a Branch

```bash
# Update from original repo
git fetch upstream
git checkout -b feature/your-feature-name upstream/main

# Branch naming:
# feature/add-rl-resources - For new features
# bugfix/fix-typo-chapter-2 - For bug fixes
# improve/clarify-linear-regression - For improvements
# docs/add-glossary - For documentation
```

### Step 3: Make Your Changes

```bash
# Edit files
# Test your changes
# Commit with clear messages
git add .
git commit -m "feat: Add new resources to Chapter 2 - Data Visualization"
```

### Step 4: Push & Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub:
- **Title:** Same as your commit message style
- **Description:** Explain what and why
- **Link issues:** If fixing a bug or addressing a request
- **Check:** Tests/linting/formatting pass

### Step 5: Respond to Review

- Be responsive to feedback
- Make requested changes in new commits
- Ask clarifying questions if needed
- Celebrate when merged! 🎉

---

## 📝 Contribution Process

### Small Contributions (Typos, Minor Fixes)

1. Fork repository
2. Create feature branch
3. Make changes
4. Commit with meaningful message
5. Push to your fork
6. Create PR with description
7. Wait for review (~24-48 hours)
8. Merge! ✅

### Medium Contributions (New Exercises, Resource Sections)

1. **Check existing issues** - Don't duplicate work
2. **Open discussion issue** - Propose your contribution
3. **Get feedback** - Wait for approval
4. **Create branch & code**
5. **Document thoroughly** - More content = more documentation needed
6. **Test completely** - Exercises should be solvable, resources should work
7. **Create PR** - Link to the discussion issue
8. **Iterate on feedback** - Usually 1-3 review rounds
9. **Merge!** ✅

### Large Contributions (New Chapters, Major Rewrites)

1. **Open issue FIRST** - Discuss scope and approach
2. **Get maintainer buy-in** - Don't write a whole chapter in isolation!
3. **Create design doc** - Outline the chapter/feature
4. **Get feedback** - Iterate on outline
5. **Develop incrementally** - Create PR for each section
6. **Cross-reference content** - Link to other chapters
7. **Complete testing** - All exercises should be fully functional
8. **Write documentation** - This is critical for large additions
9. **Final review** - Merge once approved

---

## 🎨 Style Guides

### Markdown Style

```markdown
# Chapter Title (Single #)

## Major Section (Double ##)

### Subsection (Triple ###)

**Bold for emphasis** or key terms
*Italic for references* or light emphasis

- Bullet lists for items
- With clear structure
- Easy to scan

1. Numbered lists for sequences
2. Step-by-step instructions
3. Priority-ordered items

> Blockquotes for important notes or tips

`inline code` for commands/variables
```

For code blocks:
````markdown
```python
# Always include language for syntax highlighting
def hello_world():
    print("Hello, ML students!")
```
````

### File Naming

- **Chapters:** `Chapter-0-Name-Here/`
- **Parts:** `Part-1-Name-Here.md` (with hyphens, not underscores)
- **Exercises:** `Day-X-Exercises.md`
- **Resources:** `RESOURCE_FILENAME.md` (all caps)

### Content Style

✅ **Do:**
- Write clearly for intermediate students (assuming Chapter 0 completion)
- Use real-world examples and datasets
- Include code examples that run (and test them!)
- Link to resources frequently
- Encourage practice and projects
- Include tips and warnings where relevant

❌ **Don't:**
- Assume deep domain knowledge
- Write overly theoretical without examples
- Create broken code examples
- Leave exercises without solutions available
- Copy directly from other resources without attribution

### Code Style

**Python:**
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints for clarity
- Include docstrings for functions
- Keep functions small and focused
- Add comments for non-obvious logic

```python
def calculate_similarity(vector1: List[float], vector2: List[float]) -> float:
    """
    Calculate cosine similarity between two vectors.
    
    Args:
        vector1: First vector
        vector2: Second vector
    
    Returns:
        Cosine similarity score between -1 and 1
    
    Raises:
        ValueError: If vectors have different lengths
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have same length")
    
    # Your code here
```

**Jupyter Notebooks:**
- Create meaningful cell titles with markdown
- Separate concerns (imports, config, code, visualization)
- Include outputs for readability
- Add markdown explanations
- Keep cells focused (not 100 lines per cell)

---

## 📋 Pull Request Checklist

Before submitting, ensure:

- [ ] **Small, focused PR** - Not changing 10 different things
- [ ] **Meaningful commits** - Each commit does one thing
- [ ] **Clear PR title & description** - Others can understand intent
- [ ] **No breaking changes** - Or clearly documented
- [ ] **Tests pass** - Run any existing tests/checks
- [ ] **Documentation updated** - Explain what changed
- [ ] **Follows style guides** - Formatting consistent with repo
- [ ] **Links issues** - References related issues with `Fixes #123`
- [ ] **Self-review** - Read your changes before submitting
- [ ] **No merge conflicts** - Keep up with main branch

---

## 💬 Code of Conduct

We're committed to providing a welcoming, inclusive environment.

**Be respectful:**
- Treat all contributors with respect
- Use welcoming language
- Be patient with errors/confusion

**Be collaborative:**
- Help other contributors succeed
- Provide constructive feedback
- Share knowledge generously

**Be honest:**
- Give credit to others' work
- Link to original sources
- Admit when you don't know something

**Report issues:**
- If you witness disrespect, report it
- Contact [maintainer email] with details
- All reports handled with care and confidentiality

---

## 🏆 Recognition

We celebrate our contributors!

- **Contributors listed in README.md**
- **Highlighted in release notes for major contributions**
- **Certificate of contribution** (upon request)
- **Testimonial option** - Your story in case studies

---

## ❓ Questions?

- **How do I get started?** → Fork repo + create first branch
- **Should I open an issue first?** → For large changes, yes!
- **How long until my PR is reviewed?** → Usually 24-48 hours
- **What if my PR gets rejected?** → That's okay! Feedback helps improve
- **Can I contribute if I'm just learning?** → Absolutely! Typos are great first steps

---

## 📚 Additional Resources

- [GitHub's Contributing Guide](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [First Contributions](https://github.com/firstcontributions/first-contributions)
- [Open Source Guide](https://opensource.guide/)
- [How to Write Good Git Commit Messages](https://chris.beams.io/posts/git-commit/)

---

**Thank you for contributing!** 🙏

Your improvements help the next generation of ML practitioners learn better.

Every contribution counts - whether it's fixing a typo or writing a whole chapter.

Let's build the best ML learning resource together! 🚀

---

**Last Updated:** February 19, 2026  
**Maintained by:** The SEEDAI Team
