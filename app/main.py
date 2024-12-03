import sys


def main():
    # Uncomment this block to pass the first stage
    #
    command = ""
    EXIT = "exit"

    while command != "exit":
        sys.stdout.write("$ ")
        # Wait for user input
        request = input()
        command = request.split()[0]

        if command == EXIT:
            continue

        sys.stderr.write(f"{command}: not found\n")


if __name__ == "__main__":
    main()
