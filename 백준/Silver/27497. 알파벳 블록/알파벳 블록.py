from collections import deque
import sys

list = deque()
list_count = []

Number = int(sys.stdin.readline().strip())

for _ in range(Number):
    input_data = sys.stdin.readline().strip().split()
    
    if input_data[0] == '1':
        list.append(input_data[1])
        list_count.append(input_data[0])
        
    elif input_data[0] == '2':
        list.appendleft(input_data[1])
        list_count.append(input_data[0])
        
    elif input_data[0] == '3':
        if list_count:
            order = list_count.pop()
            if order == '1':
                list.pop()
            elif order == '2':
                list.popleft()    

if list:
    print("".join(list))
else:
    print(0)
