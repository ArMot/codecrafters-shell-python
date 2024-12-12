import inspect
import sys
import os

import subprocess

from app.builtins.command import BuiltinCommands
from app.helpers import utils

BUILTINS = ["exit", "echo", "type"]

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def extract_command_and_params(user_input: str) -> tuple[str, list]:
    request = user_input.split()
    command = request[0]
    args = request[1:] if len(request) > 1 else []
    return command, args


def main():
    command = ""
    while True:
        sys.stdout.write("$ ")
        # Wait for user input
        request = input()
        command, args = extract_command_and_params(request)

        obj = BuiltinCommands()
        if hasattr(obj, command):
            run_builtin_command(obj, command, args)
        else:
            exec_path = utils.get_exec_if_exist(command)
            if exec_path:
                subprocess.call([command, *args])
            else:
                utils.not_found(command)


def run_builtin_command(obj: BuiltinCommands, command: str, args: list[str]) -> None:
    cmd = getattr(obj, command)
    if len(inspect.signature(cmd).parameters) == 0:
        cmd()
    else:
        cmd(args)


if __name__ == "__main__":
    main()
