import inspect
import sys
import os
from pathlib import Path

from app.builtins.command import BuiltinCommands
from app.helpers import utils

BUILTINS = ["exit", "echo", "type"]


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

        try:
            obj = BuiltinCommands()
            cmd = getattr(obj, command)
            if len(inspect.signature(cmd).parameters) == 0:
                cmd()
            else:
                cmd(args)
        except AttributeError:
            utils.check_if_exec_found(command)


if __name__ == "__main__":
    main()
