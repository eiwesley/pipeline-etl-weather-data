#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

paths = ["src"]
if Path("tests").exists():
    paths.append("tests")

cmd = ["ruff", "check"] + paths
print("Running:", " ".join(cmd))
rc = subprocess.call(cmd)
if rc != 0:
    print(f"ruff failed with exit code {rc}")
    sys.exit(rc)
print("ruff OK")
