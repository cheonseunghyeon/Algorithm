import sys
from collections import deque

left = list(sys.stdin.readline().strip())
right = deque()

for _ in range(int(sys.stdin.readline())):
    input_data = sys.stdin.readline().split()
    
    if input_data[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif input_data[0] == 'D':
        if right:
            left.append(right.popleft())
    elif input_data[0] == 'B':
        if left:
            left.pop()
    elif input_data[0] == 'P':
        test = input_data[1]
        left.append(test)
        
print("".join(left) + "".join(right))