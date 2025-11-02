import os
import subprocess
import sys
from pathlib import Path

from extract_values import parse_log

WORKDIR = Path(__file__).resolve().parent
BIN = WORKDIR / "rev_vvm" / "vvm"
OVERRIDE = WORKDIR / "override.so"
LOG = WORKDIR / "handler_log.txt"


def run_with_input(s: str):
    if len(s) != 32:
        raise ValueError("Input must be 32 characters")
    if LOG.exists():
        LOG.unlink()
    env = os.environ.copy()
    env["OVERRIDE_INPUT"] = s
    cmd = ["timeout", "10s", "bash", "-lc", f'cd {WORKDIR} && LD_PRELOAD={OVERRIDE} {BIN} >/dev/null']
    subprocess.run(cmd, check=True, env=env)
    values = parse_log(LOG)
    return values


def main():
    if len(sys.argv) != 2:
        print("Usage: compute_outputs.py <32-char-string>")
        sys.exit(1)
    s = sys.argv[1]
    vals = run_with_input(s)
    for expected, computed in vals:
        print(f"expected={expected:#010x} computed={computed:#010x}")


if __name__ == "__main__":
    main()
