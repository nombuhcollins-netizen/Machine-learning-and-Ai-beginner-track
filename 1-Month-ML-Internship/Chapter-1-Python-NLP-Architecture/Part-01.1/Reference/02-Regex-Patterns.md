# Regular Expression Patterns

## Common Patterns
- `\d` - digit
- `\w` - word character
- `\s` - whitespace
- `[a-z]` - character class
- `^` - start, `$` - end
- `*` - zero or more
- `+` - one or more
- `?` - zero or one

## Email: `[a-z]+@[a-z]+\.[a-z]+`
## URL: `https?://[^\s]+`
## Phone: `\d{3}-\d{3}-\d{4}`

## Methods
- `re.search()` - find first match
- `re.findall()` - find all matches
- `re.sub()` - replace matches
- `re.match()` - match from start
