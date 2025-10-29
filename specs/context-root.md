# Context Root and Session Management

## Overview

This document summarizes key insights about context window management and why starting new LLM sessions is important, based on Steve Yegge's article "Beads for Blobfish" and related work on the Beads project.

## The Context Window Problem

### Effective Context Window Usage

Even with large context windows (e.g., 1 million tokens), coding agents can only effectively utilize **10-15%** of the available context before experiencing degradation in:
- **Performance**: Response quality and accuracy decline
- **Cost**: Token processing costs increase exponentially
- **Speed**: Response generation slows down

Most agents implement hard cutoffs at around **20%** context usage to prevent these issues.

### Session Duration Reality

When working at full productivity, typical coding agent sessions last only:
- **5-10 minutes** of effective work time
- Before requiring a restart or context compaction

This creates a workflow similar to "the movie Memento in real life, or Fifty First Dates" - constant short-term memory resets.

## Why Start New Sessions?

### 1. Performance Degradation
As the context window fills, LLM performance degrades:
- Slower response times
- Reduced accuracy
- Higher error rates
- Increased hallucinations

### 2. Cost Management
Token costs scale with context size:
- Every message processes all previous context
- Costs increase proportionally with context usage
- 80-90% context usage becomes economically unsustainable

### 3. Attention Dilution
Large contexts reduce the model's ability to focus:
- Important information gets "lost in the noise"
- Model attention spreads across too many tokens
- Critical details may be overlooked

### 4. Inter-Session Amnesia
The fundamental challenge:
- Agents have **no memory between sessions**
- Each restart is a complete cognitive reset
- Work continuity requires external memory systems

## Best Practices

### When to Start a New Session

Start a new session when you reach:
- **20%** context usage (hard limit for most agents)
- **15%** context usage (recommended for optimal performance)
- Noticeable degradation in response quality
- Completion of a discrete work unit

### Context Root Concept

A "context root" is the minimal set of information needed to bootstrap a new session:
- Current task and goals
- Key decisions made
- Critical file locations and patterns
- Dependencies and relationships
- Outstanding issues and blockers

### Session Handoff Strategy

1. **Document current state** before hitting limits
2. **Create a context root** with essential information
3. **Start fresh session** with context root
4. **Reference previous work** via external memory (e.g., git commits, issue trackers)

## The Beads Solution

Steve Yegge's Beads project addresses this by providing:
- **External memory** for coding agents
- **Dependency tracking** across sessions
- **Query capabilities** to retrieve relevant context
- **Git-backed storage** for persistence
- **Graph-based organization** for relationships

This enables agents to maintain continuity across the inevitable session restarts without losing critical context.

## References

- [Beads for Blobfish](https://steve-yegge.medium.com/beads-for-blobfish-80c7a2977ffa) by Steve Yegge
- [Introducing Beads: A coding agent memory system](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a)
- [Beads GitHub Repository](https://github.com/steveyegge/beads)

## Key Takeaway

> "Even with a 1M context window, coding agents can only get a usable 10-15% out of that before their cost and performance both go the wrong direction."

Monitor your context window usage and restart sessions proactively to maintain optimal performance and cost-efficiency.
