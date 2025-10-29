#!/usr/bin/env python3
"""
Context Window Status Formatter

This script formats and displays context window usage information
in a clear, readable format for Claude Code users.
"""

import sys


def format_number(num):
    """Format number with thousand separators."""
    return f"{num:,}"


def calculate_percentage(used, total):
    """Calculate percentage used, rounded to 2 decimal places."""
    if total == 0:
        return 0.0
    return round((used / total) * 100, 2)


def display_context_window(total_tokens, used_tokens):
    """
    Display context window status in formatted output.

    Args:
        total_tokens: Total context window size in tokens
        used_tokens: Current tokens used in the conversation
    """
    available_tokens = total_tokens - used_tokens
    usage_percentage = calculate_percentage(used_tokens, total_tokens)

    # Format the output
    output = f"""Context Window Status
━━━━━━━━━━━━━━━━━━━━━
Total Size:     {format_number(total_tokens):>10} tokens
Used:           {format_number(used_tokens):>10} tokens
Available:      {format_number(available_tokens):>10} tokens
Usage:          {usage_percentage:>10.2f}%"""

    print(output)


def main():
    """Main entry point for the script."""
    if len(sys.argv) != 3:
        print("Usage: format_context_window.py <total_tokens> <used_tokens>", file=sys.stderr)
        print("\nExample: format_context_window.py 200000 28354", file=sys.stderr)
        sys.exit(1)

    try:
        total_tokens = int(sys.argv[1])
        used_tokens = int(sys.argv[2])

        if total_tokens < 0 or used_tokens < 0:
            print("Error: Token counts must be non-negative", file=sys.stderr)
            sys.exit(1)

        if used_tokens > total_tokens:
            print("Error: Used tokens cannot exceed total tokens", file=sys.stderr)
            sys.exit(1)

        display_context_window(total_tokens, used_tokens)

    except ValueError:
        print("Error: Arguments must be valid integers", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
