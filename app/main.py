import sys


def main():
    # Uncomment this block to pass the first stage

    while True:
        sys.stdout.write("$ ")
        # Wait for user input
        request = input()
        command = request.split()[0]

        sys.stderr.write(f"{command}: not found\n")


if __name__ == "__main__":
    main()
