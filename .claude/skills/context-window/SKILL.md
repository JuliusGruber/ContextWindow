---
name: context-window
description: Display real-time context window size and usage percentage information to help monitor token consumption
---

# Context Window Status

This skill displays the current context window usage statistics.

## Instructions

When invoked, you should:

1. Access the current token budget information from your environment
   - Look for `<budget:token_budget>` tags in your context
   - Look for `<system_warning>Token usage:` messages for current usage

2. Extract the following information:
   - Total token budget (context window size)
   - Current tokens used
   - Calculate tokens remaining
   - Calculate percentage used (used / total * 100, rounded to 2 decimal places)

3. Use the Python helper script `format_context_window.py` to format and display the output

4. Display the information in this exact format:

```
Context Window Status
━━━━━━━━━━━━━━━━━━━━━
Total Size:     [total with commas] tokens
Used:           [used with commas] tokens
Available:      [available with commas] tokens
Usage:          [percentage]%
```

## Example Output

```
Context Window Status
━━━━━━━━━━━━━━━━━━━━━
Total Size:     200,000 tokens
Used:            28,354 tokens
Available:      171,646 tokens
Usage:           14.18%
```

## Usage

Invoke this skill by typing `/context-window` or asking Claude about context window usage.

## Notes

- Token counts reflect the state at the moment of invocation
- Percentage is rounded to 2 decimal places
- Numbers are formatted with thousand separators for readability
