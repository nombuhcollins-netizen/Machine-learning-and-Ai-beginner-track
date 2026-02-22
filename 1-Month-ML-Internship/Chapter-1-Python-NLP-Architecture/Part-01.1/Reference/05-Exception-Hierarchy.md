# Python Exception Hierarchy

## Built-in Exceptions
- Exception (base)
  - ValueError
  - TypeError
  - IndexError
  - KeyError
  - FileNotFoundError
  - RuntimeError

## Custom Exceptions
\`\`\`python
class CustomError(Exception):
    pass

class ValidationError(CustomError):
    pass

class DataError(CustomError):
    pass
\`\`\`

## Best Practices
- Create custom exceptions for clarity
- Inherit from appropriate base
- Document expected exceptions
- Handle specific before general
