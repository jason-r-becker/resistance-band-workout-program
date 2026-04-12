## Workout Repo Context

This is a resistance band workout program. The two core files are:

- `program.md` — the active weekly training schedule
- `reference.md` — full exercise catalog and band resistance reference

### Schedule (fixed, do not suggest changes)

- **Friday** — Pull + Micro Push
- **Saturday** — Push
- **Sunday** — Legs + Biceps
- **Midweek** — two light micro sessions (Arms/Chest and Legs/Back)

### Band Colors (lightest → heaviest)

| Band | Resistance |
|------|-----------|
| 🟡 Yellow | 5–15 lbs |
| 🔴 Red | 5–35 lbs |
| ⚫ Black | 20–60 lbs |
| 🟣 Purple | 30–80 lbs |
| 🟢 Green | 40–110 lbs |

### Progression Rule

When all sets hit the top of the prescribed rep range with good form, upgrade the band one tier and reset to the bottom of the rep range.

### Build Pipeline

`./workout` builds a PDF from `program.md` + `reference.md` via `md2pdf` (Pandoc + WeasyPrint) and syncs to `~/Dropbox/workout.pdf`.

### Conventions

- Program changes should be tracked with meaningful git commits so progression history is visible via `git log -p -- program.md`.
- Band stacking is shown with multiple emoji (e.g., 🟣🟡 = purple + yellow).
- Micro sessions use lighter bands and higher reps (12–20) for pump/recovery, not heavy work.
