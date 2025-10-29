# Context Window Skill Specification

## Overview
A Claude Code skill that provides real-time information about the current context window usage, including the total size and percentage utilized.

## User Story
As a user of Claude Code, I want to know how much of my context window is being used so that I can make informed decisions about when to start a new conversation or optimize my current session.

## Functional Requirements

### FR-1: Context Window Information Display
The skill MUST display the following information when invoked:
- Total context window size (in tokens)
- Current tokens used (in tokens)
- Percentage of context window used (as a percentage)

### FR-2: Skill Invocation
The skill MUST be invokable via the `/context-window` command in Claude Code.

### FR-3: Real-Time Information
The skill MUST provide information that reflects the current state of the conversation at the time of invocation.

### FR-4: Clear Output Format
The output MUST be human-readable and clearly formatted for CLI display.

## Technical Requirements

### TR-1: Implementation
- The skill SHALL be implemented as a Claude Code skill in the `.claude/skills/` directory
- The skill file SHALL be named `context-window.md`

### TR-2: Token Information Access
- The skill MUST access token usage information from the environment or system
- Token counts SHALL include all messages, tool calls, and responses in the current session

### TR-3: Calculation Accuracy
- Percentage calculation SHALL be rounded to 2 decimal places
- Token counts SHALL be accurate as of the moment of invocation

## Expected Output Format

```
Context Window Status
━━━━━━━━━━━━━━━━━━━━━
Total Size:     200,000 tokens
Used:            45,230 tokens
Available:      154,770 tokens
Usage:           22.62%
```

## Usage Examples

### Example 1: Low Usage
```
User: /context-window

Output:
Context Window Status
━━━━━━━━━━━━━━━━━━━━━
Total Size:     200,000 tokens
Used:            15,420 tokens
Available:      184,580 tokens
Usage:            7.71%
```

### Example 2: High Usage
```
User: /context-window

Output:
Context Window Status
━━━━━━━━━━━━━━━━━━━━━
Total Size:     200,000 tokens
Used:           178,950 tokens
Available:       21,050 tokens
Usage:           89.48%
```

## Non-Functional Requirements

### NFR-1: Performance
The skill SHALL execute and return results in under 1 second.

### NFR-2: Clarity
Output SHALL be immediately understandable without additional explanation.

### NFR-3: Consistency
Token counts and percentages SHALL be consistent and verifiable.

## Success Criteria
- [ ] Skill can be invoked with `/context-window` command
- [ ] Displays total context window size correctly
- [ ] Displays current token usage accurately
- [ ] Calculates and displays percentage used correctly
- [ ] Output is formatted clearly and readably
- [ ] Works across different conversation lengths

## Future Enhancements (Out of Scope for v1)
- Visual progress bar representation of usage
- Warning thresholds (e.g., alert when >80% used)
- Historical usage tracking across sessions
- Breakdown by message type (user vs assistant vs tool)
