import sys
from pathlib import Path
import os

from app.helpers import utils


class BuiltinCommands:
    def type(self, args) -> None:
        self.validate_args(args, required_args=1)
        cmd = args[0] or ""
        try:
            getattr(self, cmd)
            utils.print_to_stdout(f"{cmd} is a shell builtin")
        except AttributeError:
            utils.check_if_exec_found(cmd)

    def echo(self, args: list[str]) -> None:
        self.validate_args(args, required_args=1)
        message = " ".join(str(arg) for arg in args)
        utils.print_to_stdout(message)

    def pwd(self) -> None:
        path = Path.cwd()
        utils.print_to_stdout(path)

    def cd(self, args: list[str]) -> None:
        self.validate_args(args, 1)
        if args[0].startswith("/"):
            try:
                os.chdir(args[0])
            except FileNotFoundError:
                utils.print_to_stderr(f"cd: {args[0]}: No such file or directory")

    def exit(self) -> None:
        sys.exit(0)

    def validate_args(self, args: list[str], required_args: int):
        if len(args) < required_args:
            raise RuntimeError("Not enough arguments passed!")
