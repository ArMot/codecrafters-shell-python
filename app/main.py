import sys

BUILTINS = ["exit", "echo", "type"]


def main():
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
        elif command == "type":
            if args[0] in BUILTINS:
                sys.stdout.write(f"{args[0]} is a shell builtin\n")
            else:
                not_found(args[0])

        else:
            not_found(command)


def echo(args: list):
    if not args:
        return
    args_str = " ".join(str(arg) for arg in args)
    sys.stdout.write(f"{args_str}\n")


def not_found(cmd: str):
    sys.stderr.write(f"{cmd}: not found\n")


if __name__ == "__main__":
    main()
