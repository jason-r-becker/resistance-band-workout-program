# Workout

Resistance band workout program — generates a printable PDF from Markdown.

## Usage

```
workout
```

Builds `workout.pdf` from `program.md` + `reference.md` and copies it to `~/Dropbox/`.

## Setup

```
ln -s "$(pwd)/workout" ~/bin/workout
```

## Files

- `program.md` — weekly training schedule (Pull / Push / Legs + micro sessions)
- `reference.md` — full exercise catalog and band reference
- `md2pdf` — Markdown → PDF converter (Pandoc + WeasyPrint)
- `workout` — build script (calls `md2pdf`, syncs to Dropbox)
