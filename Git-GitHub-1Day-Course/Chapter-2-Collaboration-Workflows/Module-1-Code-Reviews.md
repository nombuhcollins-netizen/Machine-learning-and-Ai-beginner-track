# Chapter 2 - Module 1: Code Reviews & Feedback

**Duration:** 40 minutes | **Difficulty:** Intermediate

---

## Learning Objectives

By the end of this module, you will be able to:

1. Understand the code review process
2. Review pull requests effectively
3. Provide constructive feedback
4. Request changes when needed
5. Approve high-quality code
6. Handle review conversations professionally

---

## Code Review Purpose

### Goals of Code Review

✅ **Quality Assurance** - Catch bugs before production
✅ **Knowledge Sharing** - Learn different approaches
✅ **Standards** - Maintain consistent style
✅ **Mentoring** - Help junior developers improve
✅ **Accountability** - Shared responsibility

### Code Review Mindset

**Reviewer Perspective:**
- Reviewer is here to help, not criticize
- Reviewer wants the code to succeed

**Author Perspective:**
- Feedback is about code, not the person
- Goal is to learn and improve

---

## Reviewing a Pull Request

### Step 1: Understand the Change

1. Read PR title and description
2. Check linked issues
3. Understand the purpose
4. Note any context

### Step 2: Examine Files Changed

1. Go to "Files changed" tab
2. Review each file
3. Look for:
   - Logic errors
   - Style issues
   - Incomplete tests
   - Documentation gaps

### Step 3: Check Specific Lines

Click "+" to comment on specific lines:

```python
# Line 15: This variable could be named more clearly
message = result.msg  # What is 'msg'?
# Consider: error_message = result.error_message
```

### Step 4: Leave Review

**Three types of reviews:**

1. **Comment** - General feedback, not blocking
2. **Approve** - Code is good, ready to merge
3. **Request Changes** - Issues must be fixed

---

## Commenting Best Practices

### Constructive Comments

**❌ Bad:**
```
This is wrong.
Why would you do it this way?
This code is terrible.
```

**✅ Good:**
```
I noticed this could be simplified. Consider using a list 
comprehension instead of the loop:
[x * 2 for x in numbers]
This would be more Pythonic and readable.
```

### Compliment Good Code

**❌:**
```
Nothing - only comment on problems
```

**✅:**
```
I really like how you structured this error handling.
It's clear and maintainable.
```

### Ask Questions

**❌:**
```
This is wrong.
```

**✅:**
```
I'm curious about this logic. Is there a reason you're 
checking for None here instead of using a try-except block?
I want to understand your approach.
```

### Suggest, Don't Demand

**❌:**
```
You have to change this.
```

**✅:**
```
What if we extracted this into a separate function?
I think it might improve readability. What do you think?
```

---

## Common Code Review Issues

### Logic Errors

```python
❌ if user_age > 18:  # Should be >= 18
    allow_access()
```

```
Suggestion: I think this should check if age >= 18 to 
include 18-year-olds. Is that intentional?
```

### Missing Error Handling

```python
❌ user = users[username]  # KeyError if not found
```

```
This could raise KeyError if username doesn't exist.
Consider adding a check or using .get():
user = users.get(username)
```

### Style/Convention

```python
❌ myVar = 5  # camelCase in Python
```

```
Python convention is snake_case for variables:
my_var = 5
```

### Performance

```python
❌ for user in users:        # O(n)
    if user.id == target:
        return user
```

```
For large datasets, consider indexing:
users_by_id[target_id]  # O(1)
```

### Security

```python
❌ sql = f"SELECT * FROM users WHERE id={user_id}"  # SQL injection!
```

```
This is vulnerable to SQL injection. Use parameterized queries:
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

---

## Requesting Changes

When code needs significant fixes:

1. Click "Request changes" (instead of just commenting)
2. Add detailed explanation
3. Be specific about what needs improvement

```markdown
## Summary
This PR has good structure but needs fixes before merging.

## Required Changes

1. **Line 45:** The error handling needs improvement.
   Current code can raise KeyError. Please add:
   ```python
   try:
       result = process_data(data)
   except ValueError as e:
       logger.error(f"Processing failed: {e}")
       return None
   ```

2. **Missing tests:** Please add test cases for the error scenario.

3. **Documentation:** Update docstring to describe new parameters.

## Optional Improvements

- Consider caching results for performance
- Variable naming could be more descriptive

Once you address these points, I'll review again!
```

---

## Approving Changes

Only approve when:

✅ Code is correct
✅ Tests are adequate
✅ Style is consistent
✅ Performance is acceptable
✅ Security is not compromised

```markdown
## Looks good to me!

I've reviewed this thoroughly and everything looks solid:

✅ Logic is correct and handles edge cases
✅ Tests cover the main scenarios
✅ Code is well-documented
✅ No performance concerns
✅ Follows project conventions

Great work! Ready to merge.
```

---

## Managing the Conversation

### Author Responds to Feedback

```markdown
Good catch! I've addressed this by adding error handling.
Please see the new commit for the changes.
```

### Reviewer Re-reviews

After author makes changes:
1. Look at new commits pushed to PR
2. Review changes
3. Either approve or request more changes

### Multiple Reviewers

If multiple people review:
- All must approve to merge (usually)
- Check repository settings for requirements

---

## Review Etiquette

### Be Respectful

- Assume good intentions
- Treat as learning opportunity
- Build trust within team

### Be Timely

- Review PRs within 24 hours if possible
- Don't let PRs age - they become stale
- Communicate if you need more time

### Be Clear

- Explain your reasoning
- Provide examples
- Link to documentation

### Be Open-minded

- You might be wrong
- Learn from the author's approach
- Discuss trade-offs

---

## Exercises

### Exercise 1: Review a Sample PR

**Objective:** Practice reviewing code

**Instructions:**

Since we don't have actual PRs from team members, we'll simulate:

1. **Look at your own PR from Module 0**
   - Click on your PR
   - Go to "Files changed" tab
   - Read your own code as if you're another reviewer

2. **Leave specific comments:**
   - Click "+" on 2-3 lines
   - Add constructive feedback example:
     ```
     This logic looks good. Quick question: have you 
     considered edge case when the input is None?
     ```
   - Add a positive comment:
     ```
     I like how clear this variable name is!
     ```

3. **Review your own changes:**
   - Do they match the PR description?
   - Is there any obvious improvements?
   - Are tests adequate?

**Verification Checklist:**
- [ ] Review process understood
- [ ] Comments left on PR
- [ ] Mix of positive and constructive feedback
- [ ] Topics include logic, style, performance

---

### Exercise 2: Request Changes on Your PR

**Objective:** Understand change request process

**Instructions:**

1. **Go to your PR**
   - Files changed tab

2. **Click "Request changes"** button
   - (We're simulating a reviewer)
   - Add detailed feedback:
   
   ```markdown
   ## Summary
   Good work overall, but a few improvements needed.
   
   ## Required Changes
   1. Line 45: Add error handling for edge cases
   2. Missing test for null input scenario
   
   ## Optional Improvements
   - Consider refactoring repeated code into function
   
   Looking forward to seeing updates!
   ```

3. **Simulate addressing feedback:**
   - Make changes to your code locally
   - Push new commits
   - Go back to PR (should show new commits)

4. **Make the PR good:**
   - Address the feedback you gave
   - Push changes:
     ```bash
     git add .
     git commit -m "Address review feedback"
     git push
     ```

5. **Go back to PR:**
   - See new commits listed
   - Change review from "Changes requested" to "Approve"

**Verification Checklist:**
- [ ] Understand "Request changes" workflow
- [ ] Made updates to code
- [ ] Pushed new commits
- [ ] Changed review status

---

### Exercise 3: Approve PR

**Objective:** Complete review process

**Instructions:**

1. **Look at your PR**
   - Files changed tab
   - Verify all feedback addressed

2. **Add approval review:**
   - Click "Review changes" dropdown
   - Select "Approve"
   - Add comment:
   
   ```markdown
   Excellent work! All feedback has been addressed:
   
   ✅ Error handling improved
   ✅ Tests added for edge cases
   ✅ Code is clear and maintainable
   ✅ No performance concerns
   
   Ready to merge!
   ```
   
   - Click "Approve"

3. **Merge the PR:**
   - Scroll to bottom of PR
   - Click "Merge pull request"
   - Check "Delete branch"
   - Confirm merge

4. **Verify merge:**
   - Check "Code" tab on repository
   - Files should show your changes on main branch
   - View "Commits" to see merge commit

**Verification Checklist:**
- [ ] PR approved
- [ ] PR merged successfully
- [ ] Branch deleted
- [ ] Changes visible on main branch

---

## Review Checklist Template

Create your own review checklist:

```markdown
## Code Review Checklist

- [ ] PR description is clear
- [ ] Changes match the description
- [ ] Code is correct (no logic errors)
- [ ] Variable names are clear
- [ ] Error handling is present
- [ ] Tests are adequate
- [ ] Performance is acceptable
- [ ] Security is not compromised
- [ ] Follows code style guidelines
- [ ] Documentation is updated
```

---

## Key Takeaways

✅ Code review is about helping, not criticizing
✅ Written feedback should be constructive and specific
✅ Compliment good code, not just criticize bad code
✅ Ask questions to understand reasoning
✅ Only approve when truly ready to merge
✅ Be respectful and professional in all feedback

---

## Review Examples

### Good Review Comments

- "I like how you structured this!"
- "This could be simplified with a list comprehension"
- "Have you tested what happens if this is None?"
- "Great attention to error handling!"
- "This might have performance issues with large datasets"

### Bad Review Comments

- "This is dumb"
- "Why would you do it this way?"
- "This is obviously wrong"
- "You should know better"

---

## Next Steps

You understand code reviews! In **Module 2**, you'll apply these skills in actual team workflows.

---

**[← Back to Module 0](./Module-0-Pull-Requests.md)** | **[Next: Module 2 →](./Module-2-Team-Workflows.md)**
