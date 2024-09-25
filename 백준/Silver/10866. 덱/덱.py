import sys
from collections import deque


number = int(sys.stdin.readline().strip())
result = deque() 

for _ in range(number):
    inputs = sys.stdin.readline().strip().split()
    command = inputs[0]  
  
    if command == "push_front":
        result.appendleft(inputs[1])
    elif command == "push_back":
        result.append(inputs[1])
    elif command == "pop_front":
        print(result.popleft() if result else -1) 
    elif command == "pop_back":
        print(result.pop() if result else -1) 
    elif command == "size":
        print(len(result))
    elif command == "empty":
        print(0 if result else 1) 
    elif command == "front":
        print(result[0] if result else -1)  
    elif command == "back":
        print(result[-1] if result else -1) 
