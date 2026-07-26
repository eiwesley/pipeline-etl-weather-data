#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

paths = ["src"]
if Path("tests").exists():
    paths.append("tests")

cmd = ["ruff", "check", "--fix"] + paths
print("Running:", " ".join(cmd))
rc = subprocess.call(cmd)
if rc != 0:
    print(f"ruff check --fix failed with exit code {rc}")
    sys.exit(rc)
print("ruff check --fix OK")
