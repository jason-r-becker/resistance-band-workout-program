#!/usr/bin/env python3

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PDF_PATH = REPO_ROOT / "workout.pdf"
TARGET_FILES = {"program.md", "reference.md"}
MUTATING_TOOLS = {
    "apply_patch",
    "create_file",
    "editFiles",
    "replace_string_in_file",
    "writeFile",
    "createFile",
    "Edit",
    "Write",
}


def collect_targets(value, targets):
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in {"input", "patch"} and isinstance(nested, str):
                parse_patch_paths(nested, targets)
            elif key.lower().endswith("path"):
                collect_targets(nested, targets)
            elif key.lower().endswith("paths") or key in {"files", "file"}:
                collect_targets(nested, targets)
            else:
                collect_targets(nested, targets)
        return

    if isinstance(value, list):
        for nested in value:
            collect_targets(nested, targets)
        return

    if isinstance(value, str):
        cleaned = value.strip()
        if cleaned:
            targets.add(cleaned)


def parse_patch_paths(patch_text, targets):
    for line in patch_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("*** Update File: ") or stripped.startswith("*** Add File: "):
            targets.add(stripped.split(": ", 1)[1].strip())


def has_target_change(payload):
    if payload.get("hookEventName") != "PostToolUse":
        return False

    tool_name = payload.get("tool_name", "")
    if tool_name not in MUTATING_TOOLS:
        return False

    targets = set()
    collect_targets(payload.get("tool_input", {}), targets)

    for target in targets:
        if Path(target).name in TARGET_FILES:
            return True

    return False


def print_json(data):
    sys.stdout.write(json.dumps(data))
    sys.stdout.write("\n")


def main():
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print_json(
            {
                "decision": "block",
                "reason": "Workout PDF hook received invalid JSON input.",
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": str(exc),
                },
            }
        )
        return 0

    if not has_target_change(payload):
        print_json({"continue": True})
        return 0

    build = subprocess.run(
        ["./workout"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )

    if build.returncode != 0:
        details = (build.stdout + "\n" + build.stderr).strip()
        details = details[-4000:]
        print_json(
            {
                "decision": "block",
                "reason": "Rebuilding workout.pdf failed after editing program.md or reference.md.",
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": details,
                },
            }
        )
        return 0

    open_note = "Rebuilt workout.pdf and opened it with the default PDF viewer."
    try:
        subprocess.Popen(
            ["xdg-open", str(PDF_PATH)],
            cwd=REPO_ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except Exception as exc:  # noqa: BLE001
        open_note = f"Rebuilt workout.pdf, but opening it failed: {exc}"

    print_json(
        {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": open_note,
            }
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())