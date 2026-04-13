---
name: workout-program-evaluation
description: 'Evaluate the resistance band workout program using all repo context, local training preferences, git history, and parallel specialist subagent reviews. Use for full program review, time-aware recommendations, progression stalls, rep-range audits, band-specific exercise evaluation, recovery or pain constraints, and reconciling multiple viewpoints into one final recommendation.'
argument-hint: 'Optional focus: full review, time budget, progression stalls, elbow-friendly changes, rep ranges, volume balance, exercise swaps'
user-invocable: true
disable-model-invocation: false
---

# Workout Program Evaluation

## Purpose

Run a full, constraint-aware evaluation of this repo's workout program. Treat review as a multi-specialist process: read every relevant source of truth in the repo, launch focused subagent analyses in parallel, then reconcile them into one final recommendation set.

This skill is for evaluation first. It can lead to edits later, but it must not edit the program until the user approves specific changes.

## When To Use

- Full review of the current program
- Time-budget-aware rep or set recommendations
- Progression bottlenecks or stalled exercises
- Volume balance, frequency, and muscle coverage checks
- Band-specific exercise or rep-range fit questions
- Recovery, joint irritation, or durability concerns
- Cases where several plausible changes need reconciliation instead of one quick opinion

## Hard Rules

- Read the current workout files before making judgments.
- Treat `.training-preferences.local.md` as a real constraint file if it exists.
- Respect the fixed weekly schedule from `.github/copilot-instructions.md`.
- Keep recommendations evidence-first, and clearly label band-practical reasoning when direct evidence is limited.
- Do not claim multi-model diversity unless the platform actually exposes distinct models. If it does not, run multiple specialist subagent passes with distinct briefs instead.
- Do not edit `program.md` or `reference.md` until the user approves specific changes.
- If recommending rep changes, present a current-vs-recommended table and ask for the user's thoughts before editing.
- Treat session length as a first-class constraint when the local preferences file says time is tight.
- Avoid global rep inflation. If higher reps materially increase time cost, prefer tighter ranges or consider offsetting with accessory set reductions.

## Required Context

Read these sources every time before forming conclusions:

- `program.md`
- `reference.md`
- `README.md`
- `.github/copilot-instructions.md`
- `.training-preferences.local.md` if present

Use git history when the request is about progression over time, stalls, or a full review where past changes may matter:

```bash
git -C /home/jb/python/workout log --oneline -- program.md
git -C /home/jb/python/workout log -p --follow -- program.md
```

If history is shallow, say so and evaluate the current design on its own merits.

## Workflow

1. Read the required context files and write down the active constraints before judging the program.
2. Summarize the user's actual objectives, priority muscles, pain issues, recovery or time constraints, fixed schedule, progression rule, and non-negotiables.
3. Build a quick baseline: rough weekly set totals by muscle group, obvious overlap, likely progression bottlenecks, and any exercises that look mismatched to bands or rep targets.
4. Launch the specialist reviews defined in [the subagent framework](./references/subagent-framework.md). Run them in parallel when tools allow.
5. Reconcile the specialist outputs into one recommendation set. Favor consensus, simplicity, constraint fit, and time efficiency over novelty.
6. Produce a concise final review with a short list of high-impact changes only.
7. If changes involve reps, sets, or exercise swaps, ask the user for sign-off before editing files.

## Output Standard

Your final review should be decision-ready, not sprawling.

- Start with the main conclusion and the limiting factor.
- Separate high-confidence recommendations from lower-confidence ideas.
- Keep the main change list to 3 to 7 items unless the user explicitly asks for a full rewrite.
- For each proposed change, state whether the basis is `Evidence`, `Band-practical`, or `Mixed`.
- If time is a constraint, explicitly note the expected time effect: `lower`, `neutral`, or `higher`.
- When rep changes are proposed, use a current-vs-recommended table before any edit is made.

## Editing Guardrails

- Preserve the fixed Friday, Saturday, Sunday, and midweek structure.
- Preserve existing formatting, table structure, and emoji band notation.
- Keep Saturday Skull Crushers and the midweek biceps curl unless the user explicitly requests otherwise.
- Make the smallest set of changes needed.
- Update `reference.md` when an approved exercise or prescription change should also alter the exercise catalog.

## Related Artifacts

- Specialist briefs and scoring: [subagent framework](./references/subagent-framework.md)