---
name: workout-program-evaluation
description: 'Evaluate and build the resistance band workout program using all repo context, gitignored local training preferences, git history, and parallel specialist subagent reviews. Use for full program builds, full reviews, time-aware recommendations, progression stalls, git-history stagnation analysis, rep-range audits, band-specific exercise evaluation, recovery or pain constraints, and reconciling multiple viewpoints into one final recommendation.'
argument-hint: 'Optional focus: full build from preferences, full review, time budget, progression stalls, history review, elbow-friendly changes, rep ranges, volume balance, exercise swaps'
user-invocable: true
disable-model-invocation: false
---

# Workout Program Evaluation

## Purpose

Run a full, constraint-aware evaluation of this repo's workout program. Treat review as a multi-specialist process: read every relevant source of truth in the repo, launch focused subagent analyses in parallel, then reconcile them into one final recommendation set.

This skill can also build or rebuild a full individualized program from the user's gitignored local answers in `.training-preferences.local.md`, then evaluate and refine that plan over time.

This skill is evaluation-first and decision-first. It can lead to edits later, but it must not edit the program until the user approves specific changes.

## When To Use

- Build a full individualized program from `.training-preferences.local.md`
- Full review of the current program
- Time-budget-aware rep or set recommendations
- Progression bottlenecks or stalled exercises
- Improvement and stagnation review from git history
- Volume balance, frequency, and muscle coverage checks
- Band-specific exercise or rep-range fit questions
- Recovery, joint irritation, or durability concerns
- Cases where several plausible changes need reconciliation instead of one quick opinion

## Hard Rules

- Read the current workout files before making judgments.
- Treat `.training-preferences.local.md` as the canonical gitignored personal questionnaire and constraint file if it exists.
- Respect the fixed weekly schedule from `.github/copilot-instructions.md`.
- Keep recommendations evidence-first, and clearly label band-practical reasoning when direct evidence is limited.
- Do not claim multi-model diversity unless the platform actually exposes distinct models. If it does not, run multiple specialist subagent passes with distinct briefs instead.
- Do not edit `program.md` or `reference.md` until the user approves specific changes.
- If recommending rep changes, present a current-vs-recommended table and ask for the user's thoughts before editing.
- Treat session length as a first-class constraint when the local preferences file says time is tight.
- Avoid global rep inflation. If higher reps materially increase time cost, prefer tighter ranges or consider offsetting with accessory set reductions.
- If the user asks for a full program build and `.training-preferences.local.md` is missing or incomplete, ask targeted follow-up questions before proposing the structure.
- When the user asks about improvement over time, inspect git history and explicitly separate what the current plan looks like from what the history suggests is improving, regressing, or stagnating.

## Required Context

Read these sources every time before forming conclusions:

- `program.md`
- `reference.md`
- `README.md`
- `.github/copilot-instructions.md`
- `.training-preferences.local.md` if present

When the request is a full build or major rewrite, treat `.training-preferences.local.md` as the user-specific answer sheet for goals, priority muscles, pain issues, recovery constraints, session length, equipment, and non-negotiables.

Use git history when the request is about progression over time, stalls, improvement tracking, or a full review where past changes may matter:

```bash
git -C /home/jb/python/workout log --oneline -- program.md
git -C /home/jb/python/workout log -p --follow -- program.md
```

If history is shallow, say so and evaluate the current design on its own merits.

## Workflow

1. Read the required context files and write down the active constraints before judging the program.
2. If the user wants a full build, summarize the personal answers from `.training-preferences.local.md`, call out any missing inputs, and translate those answers into program constraints before proposing structure.
3. Summarize the user's actual objectives, priority muscles, pain issues, recovery or time constraints, fixed schedule, progression rule, and non-negotiables.
4. Build a quick baseline: rough weekly set totals by muscle group, obvious overlap, likely progression bottlenecks, and any exercises that look mismatched to bands or rep targets.
5. If the user wants improvement-over-time feedback, inspect `git log -p -- program.md` and note what seems to have improved, what has churned, and what appears stalled.
6. Launch the specialist reviews defined in [the subagent framework](./references/subagent-framework.md). Run them in parallel when tools allow.
7. Reconcile the specialist outputs into one recommendation set. Favor consensus, simplicity, constraint fit, and time efficiency over novelty.
8. Produce a concise final review with a short list of high-impact changes only.
9. If changes involve reps, sets, or exercise swaps, ask the user for sign-off before editing files.

## Output Standard

Your final review should be decision-ready, not sprawling.

- Start with the main conclusion and the limiting factor.
- Separate high-confidence recommendations from lower-confidence ideas.
- Keep the main change list to 3 to 7 items unless the user explicitly asks for a full rewrite.
- For each proposed change, state whether the basis is `Evidence`, `Band-practical`, or `Mixed`.
- If time is a constraint, explicitly note the expected time effect: `lower`, `neutral`, or `higher`.
- When rep changes are proposed, use a current-vs-recommended table before any edit is made.
- For git-history reviews, distinguish current-state problems from trends seen across commits and call out stagnating areas explicitly.

## Editing Guardrails

- Preserve the fixed Friday, Saturday, Sunday, and midweek structure.
- Preserve existing formatting, table structure, and emoji band notation.
- Keep Saturday Skull Crushers and the midweek biceps curl unless the user explicitly requests otherwise.
- Make the smallest set of changes needed.
- Update `reference.md` when an approved exercise or prescription change should also alter the exercise catalog.

## Related Artifacts

- Specialist briefs and scoring: [subagent framework](./references/subagent-framework.md)