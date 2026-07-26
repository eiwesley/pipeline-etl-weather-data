#!/usr/bin/env python3
import subprocess
import sys

cmd = ["basedpyright"]
print("Running:", " ".join(cmd))
rc = subprocess.call(cmd)
# Treat basedpyright exit code 3 (no files found) as non-fatal
if rc != 0:
    if rc == 3:
        print("basedpyright returned code 3 (no files); continuing")
        sys.exit(0)
    print(f"basedpyright failed with exit code {rc}")
    sys.exit(rc)
print("basedpyright OK")
