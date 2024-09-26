import sys
from collections import deque

result = deque()
for _ in range(int(sys.stdin.readline())):
    input_data = sys.stdin.readline().split()
    
    command = input_data[0]
    if command == 'push':
        result.append(input_data[1])
    if command == 'pop':
        print(result.pop() if result else -1 )
    if command == 'size':
        print(len(result))
    if command == 'empty':
        print(0 if result else 1 )
    if command == 'top':
        print(result[-1] if result else -1 )