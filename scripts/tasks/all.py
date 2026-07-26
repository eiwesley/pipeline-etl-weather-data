#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

script_dir = Path(__file__).parent
tasks_dir = script_dir

commands = [
    [sys.executable, str(tasks_dir / "format.py")],
    [sys.executable, str(tasks_dir / "check_fix.py")],
    [sys.executable, str(tasks_dir / "lint.py")],
    [sys.executable, str(tasks_dir / "typecheck.py")],
    [sys.executable, str(tasks_dir / "test.py")],
]


def run(cmd):
    print("Running:", " ".join(cmd))
    rc = subprocess.call(cmd)
    if rc != 0:
        print(f"Command failed with exit code {rc}: {' '.join(cmd)}")
        sys.exit(rc)


def main():
    for c in commands:
        run(c)
    print("All checks passed")


if __name__ == "__main__":
    main()
