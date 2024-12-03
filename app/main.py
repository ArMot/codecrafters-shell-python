import sys
from typing import Optional


def main():
    # Uncomment this block to pass the first stage
    #
    command = ""
    EXIT = "exit"

    while command != "exit":
        sys.stdout.write("$ ")
        # Wait for user input
        request = input()
        request = request.split()
        command = request[0]
        args = request[1:] if len(request) > 1 else []

        if command == EXIT:
            continue
        elif command == "echo":
            echo(args)

        else:
            sys.stderr.write(f"{command}: not found\n")


def echo(args: list):
    if not args:
        return
    args_str = " ".join(str(arg) for arg in args)
    sys.stdout.write(f"{args_str}\n")


if __name__ == "__main__":
    main()
