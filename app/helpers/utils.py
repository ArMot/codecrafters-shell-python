import sys
import os
from pathlib import Path


def not_found(cmd: str):
    print_to_stderr(f"{cmd}: not found")


def print_to_stdout(message: str):
    sys.stdout.write(f"{message}\n")


def print_to_stderr(message: str):
    sys.stderr.write(f"{message}\n")


def check_if_exec_found(cmd):
    path = get_exec_if_exist(cmd)
    if path:
        print_to_stdout(f"{cmd} is {path}")
    else:
        not_found(cmd)


def get_exec_if_exist(cmd: str) -> str | None:
    PATH = os.environ.get("PATH", "/usr/bin:/usr/local/bin")
    for p in PATH.split(":"):
        exec_path = f"{p}/{cmd}"
        if Path(exec_path).is_file():
            return exec_path
