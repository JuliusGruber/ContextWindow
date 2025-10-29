# ContextWindow

A Claude Code skill that displays real-time context window usage information, helping you monitor token consumption and make informed decisions about conversation management.

## Features

- View total context window size
- Check current token usage
- See percentage of context window used
- Available tokens remaining

## Usage

Invoke the skill with:
```
/context-window
```

## Output

```
Context Window Status
━━━━━━━━━━━━━━━━━━━━━
Total Size:     200,000 tokens
Used:            45,230 tokens
Available:      154,770 tokens
Usage:           22.62%
```

## Documentation

See [specs/context-window-skill.md](specs/context-window-skill.md) for the complete specification.