from collections import deque
import sys
input = sys.stdin.read
commands = input().splitlines()

queue = deque()
output = []

for command in commands[1:]:
    if command.startswith("push"):
        _, value = command.split()
        queue.append(value)
    elif command == "pop":
        if queue:
            output.append(queue.popleft())
        else:
            output.append("-1")
    elif command == "size":
        output.append(str(len(queue)))
    elif command == "empty":
        output.append("1" if not queue else "0")
    elif command == "front":
        if queue:
            output.append(queue[0])
        else:
            output.append("-1")
    elif command == "back":
        if queue:
            output.append(queue[-1])
        else:
            output.append("-1")

sys.stdout.write("\n".join(output) + "\n")
