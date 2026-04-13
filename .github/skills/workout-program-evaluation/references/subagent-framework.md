# Subagent Framework

## Constraint Hierarchy

Use this order when specialist opinions conflict:

1. Explicit non-negotiables from `.github/copilot-instructions.md` and `.training-preferences.local.md`
2. Pain and durability constraints
3. Session length and simplicity constraints
4. Stated goals and priority muscles
5. Progression clarity and band practicality
6. Variety or novelty

## Required Baseline Before Spawning Specialists

Write down:

1. The active goals
2. Priority muscles
3. Injury or irritation issues
4. Session length constraint
5. Fixed schedule and exercise non-negotiables
6. Rough weekly set totals for chest, back, side delts, rear delts, biceps, triceps, quads, glutes-hamstrings, calves, and core
7. The 2 to 4 biggest apparent bottlenecks before specialist review

## Specialist Roles

Launch these reviews in parallel. If only one named subagent is available, launch multiple instances with different prompts. If no separate agent type is available, run multiple internal specialist passes and keep them explicitly distinct.

### 1. Hypertrophy And Coverage Specialist

Focus on:

- Weekly volume by muscle group
- Frequency distribution
- Angle coverage and overlap
- Whether the plan is efficient for muscle gain with bands

Return:

1. Letter grade
2. Top 3 changes only
3. Why each change matters
4. Which current choices should stay in place

### 2. Progression And Band Mechanics Specialist

Focus on:

- Whether current band choices and rep targets create a realistic progression path
- Exercises likely to stall first
- Where band jumps are too coarse for the current rep scheme
- Which exercises are poor fits for very low reps because of resistance curve or setup

Return:

1. Letter grade
2. Top 3 changes only
3. Whether each change is evidence-driven, band-practical, or mixed
4. Which progressions are most likely to work without adding complexity

### 3. Recovery, Pain, And Durability Specialist

Focus on:

- Joint stress, especially around any stated pain issues
- Exercise sequencing and cumulative fatigue
- Whether the structure looks sustainable for months, not just one good week
- Redundancy that may create irritation without much upside

Return:

1. Letter grade
2. Top 3 changes only
3. Why each change matters for durability or recovery
4. What should not be changed because it is low-risk and productive

### 4. Time Budget And Simplicity Specialist

Focus on:

- Whether the plan fits the stated session-length limit
- Whether rep suggestions are realistic without bloating sessions
- Where set reductions would buy more value than adding reps
- Whether the plan is simpler than it needs to be

Return:

1. Letter grade
2. Top 3 changes only
3. Estimated time effect for each change: lower, neutral, or higher
4. Which recommendations should be rejected because they cost too much time

### 5. Skeptic And Constraint Arbiter

Focus on:

- Reject weak, low-ROI, or contradictory suggestions from the other specialists
- Enforce the fixed schedule and other non-negotiables
- Reject ideas that add complexity without enough upside
- Prefer adjusting an existing movement over adding another one when both solve the same problem

Return:

1. Suggestions to reject
2. Reason for each rejection
3. Strongest surviving ideas

## Reconciliation Rules

After all specialist passes finish, reconcile their outputs using these tie-breakers:

1. Constraints beat preferences
2. Consensus beats novelty
3. Simpler changes beat more invasive changes when impact is similar
4. Time-neutral changes beat time-costly changes when impact is similar
5. Adjusting an existing exercise beats adding another exercise when impact is similar

For every surviving recommendation, score:

- Impact: 1 to 5
- Confidence: 1 to 5
- Time effect: lower, neutral, or higher
- Basis: Evidence, Band-practical, or Mixed
- Support: which specialists endorsed it

Keep the main list short. Default to 3 to 7 changes.

## Rep-Change Rule

When any recommendation changes sets or reps:

1. Show a current-vs-recommended table first
2. Include the expected time effect
3. Ask for the user's thoughts before editing
4. If higher reps are being proposed on a time-limited program, consider whether a 3-set accessory should instead become 2 sets

## Final Output Template

Use this structure:

```markdown
## Workout Review

### Overall Verdict
Short paragraph with the biggest limiting factor.

### Constraint Summary
| Constraint | Active value | Why it matters |
|------------|--------------|----------------|

### Specialist Summary
| Specialist | Grade | Main concern | Best suggestion |
|------------|-------|--------------|-----------------|

### Consensus High-Impact Changes
| # | Exact edit | Why it matters | Basis | Time effect | Support | Impact | Confidence |
|---|------------|----------------|-------|-------------|---------|--------|------------|

### Rejected Ideas
- Suggestion: why it was rejected

### Current Vs Recommended
Only include this section if sets or reps are being changed.

| Exercise | Current | Recommended | Time effect | Reason |
|----------|---------|-------------|-------------|--------|

### Ready To Apply
Ask which approved changes should be applied to `program.md` and `reference.md`.
```