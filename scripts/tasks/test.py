#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

if not Path("tests").exists():
    print("No 'tests' directory found; skipping tests")
    sys.exit(0)

cmd = ["pytest"]
print("Running:", " ".join(cmd))
rc = subprocess.call(cmd)
if rc != 0:
    print(f"pytest failed with exit code {rc}")
    sys.exit(rc)
print("pytest OK")
