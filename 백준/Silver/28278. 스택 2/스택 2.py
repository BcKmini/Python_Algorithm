import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    N = int(data[0])
    commands = data[1:]

    stack = []
    result = []

    for command in commands:
        if command[0] == '1':
            _, x = command.split()
            stack.append(int(x))
        elif command[0] == '2':
            if stack:
                result.append(stack.pop())
            else:
                result.append(-1)
        elif command[0] == '3':
            result.append(len(stack))
        elif command[0] == '4':

            result.append(1 if not stack else 0)
        elif command[0] == '5':
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)

    sys.stdout.write("\n".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()
