---
name: "Workout Full Review"
description: "Evaluate the full workout program with parallel specialist sub-agents, reconcile suggested changes, and surface only high-impact edits."
argument-hint: "Optional focus: full review, progression stalls, arm balance, chest, legs, shoulders"
agent: "agent"
---

# Workout Full Review

Evaluate the full workout program in [program.md](../../program.md) using [reference.md](../../reference.md), [README.md](../../README.md), [.github/copilot-instructions.md](../copilot-instructions.md), and [../../.training-preferences.local.md](../../.training-preferences.local.md) if it exists.

Your goal is to produce the best possible feedback with minimal noise, no contradictory recommendations, and a short list of high-impact edits.

## Hard Rules

- The weekly schedule is fixed. Do **not** suggest changing Friday, Saturday, Sunday, or the existence of the midweek micro sessions.
- Start by reading the current workout files before making any judgments.
- If [../../.training-preferences.local.md](../../.training-preferences.local.md) exists, read it and treat it as a real constraint set for exercise selection, volume, session length, recovery tradeoffs, and recommendation priority. If it does not exist, state that clearly and proceed without it.
- Use git history to look for progression context, but do **not** invent a trend if the history is shallow.
- Use exact current exercise names, bands, sets, and reps from [program.md](../../program.md).
- Do **not** give circular advice. If one suggestion removes or swaps an exercise, do not later reintroduce the same idea in a different form unless there is a clearly stated reason.
- Prefer the smallest number of changes that unlock the biggest improvement. Target **3 to 7** changes, not a giant rewrite.
- Every suggested change must clearly improve at least one of these: progression potential, hypertrophy stimulus, recovery, durability, balance, or simplicity.
- Every suggested change must also respect the repo's recommendation standard: evidence first, with band-specific practical bias only where necessary.
- Ignore low-value nitpicks. The goal is not to maximize comments, it is to maximize useful signal.
- Do **not** edit [program.md](../../program.md) until the user approves specific changes.

## Step 1 — Gather Context

Read the current workout files:

- [program.md](../../program.md)
- [reference.md](../../reference.md)
- [README.md](../../README.md)
- [.github/copilot-instructions.md](../copilot-instructions.md)
- [../../.training-preferences.local.md](../../.training-preferences.local.md) if it exists

Then inspect history in the terminal:

```bash
git -C /home/jb/python/workout log --oneline -- program.md
git -C /home/jb/python/workout log -p --follow -- program.md
```

If `program.md` only has one relevant commit or the history is otherwise too shallow, state that clearly and evaluate progression based on the **current design only**.

Before spawning sub-agents, write down:

1. Rough weekly set totals for chest, back, side delts, rear delts, biceps, triceps, quads, glutes/hamstrings, calves, and core
2. Any obvious exercise duplication or redundancy
3. Any obvious likely progression bottlenecks
4. Which local user preferences are most relevant to the current decision

## Step 2 — Spawn Specialist Sub-Agents In Parallel

Launch these four specialist reviews in parallel. Each one should read the current program and return a short, concrete report.

All specialists must respect [../../.training-preferences.local.md](../../.training-preferences.local.md) if it exists, and must avoid recommendations that conflict with it unless they explicitly justify why the conflict is worth it.

### Agent 1: Hypertrophy Analyst

Focus on:

- Weekly volume per muscle group
- Frequency distribution
- Exercise angle coverage
- Rep-range variety
- Whether the plan is likely to build muscle efficiently with bands

Return:

1. Overall letter grade
2. Top 3 high-impact changes only
3. Short rationale for each change
4. Any changes you explicitly would **not** make

### Agent 2: Strength And Durability Analyst

Focus on:

- Joint stress and recovery within the fixed schedule
- Push/pull and upper/lower balance
- Exercise redundancy
- Likely weak links or injury risks
- Whether the structure is sustainable for months, not just weeks

Return:

1. Overall letter grade
2. Top 3 high-impact changes only
3. Short rationale for each change
4. Any changes you explicitly would **not** make

### Agent 3: Progression Analyst

Focus on:

- Which exercises are most likely to stall first
- Whether current band choices and rep ranges make progression realistic
- Whether exercise order supports progression
- Where the progression logic is ambiguous or too subjective
- Whether the plan has a clear path for continued advancement

Return:

1. Overall letter grade
2. Top 3 high-impact changes only
3. Short rationale for each change
4. Any changes you explicitly would **not** make

### Agent 4: Skeptic / Constraint Checker

Focus on:

- Reject weak, low-ROI, or contradictory suggestions from the other agents
- Enforce the fixed-schedule rule
- Flag suggestions that add complexity without enough upside
- Flag cases where adjusting an existing exercise would be better than adding a new one

Return:

1. A short list of suggestions that should be rejected
2. The reason each should be rejected
3. A short list of the strongest surviving ideas

## Step 3 — Reconcile The Suggestions

After the four sub-agents finish, reconcile their outputs into a single decision.

### Reconciliation Rules

Use these tie-breakers in order:

1. User constraints win first
2. Consensus beats novelty
3. Simpler changes beat more invasive changes when impact is similar
4. Adjusting an existing movement beats adding another exercise when both solve the problem
5. Avoid changing multiple variables at once unless the problem clearly requires it

For each surviving change, score:

- **Impact:** 1 to 5
- **Confidence:** 1 to 5
- **Support:** which agents endorsed it
- **Basis:** `Evidence`, `Band-practical`, or `Mixed`

Only keep suggestions that clear a high bar. If an idea is interesting but low-confidence, put it in a lower-priority section instead of the main list.

## Step 4 — Produce The Final Review

Your final answer should be concise, concrete, and decision-ready.

Use this structure:

```markdown
## Workout Review

### Overall Grade
Short paragraph with the grade and the main reason.

### Specialist Summary
| Specialist | Grade | Main concern | Best suggestion |
|------------|-------|--------------|-----------------|

### Consensus High-Impact Changes
| # | Exact edit | Why it matters | Basis | Support | Impact | Confidence |
|---|------------|----------------|-------|---------|--------|------------|

### Rejected Ideas
- Suggestion: why it was rejected

### Notes On Progression History
Brief note on what git history does or does not show.

### Preference Fit
Brief note on which user preferences most shaped the final recommendations.

### Ready To Apply
Ask which of the consensus changes should be applied to [program.md](../../program.md).
```

## Editing Rules If The User Approves Changes

- Edit [program.md](../../program.md) only after approval
- Preserve existing formatting, table structure, and emoji band notation
- Make the smallest set of edits needed
- Do not silently change the fixed schedule
- If a suggested exercise is not already in [reference.md](../../reference.md), call that out before adding it