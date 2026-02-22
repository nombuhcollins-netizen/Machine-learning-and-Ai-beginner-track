# Debugging Guide

## Using pdb
\`\`\`python
import pdb
pdb.set_trace()  # breakpoint
# commands: n (next), s (step), c (continue), l (list)
\`\`\`

## Logging
\`\`\`python
logging.debug("Debug message")
logging.error("Error message")
\`\`\`

## Print Debugging
- Add strategic print statements
- Use f-strings for clarity
- Remove before production

## Common Issues
- Off-by-one errors in loops
- Type mismatches
- None values
- Mutation of shared data
