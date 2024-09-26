from collections import deque
import sys

total_list = deque()
count = 0
num = 0
N = int(sys.stdin.readline())
total_list = [int(sys.stdin.readline().strip()) for _ in range(N)]

S = len(total_list)-1
if total_list:
    for item in range(S, -1, -1):
        if num < total_list[item]:
            num = total_list[item]
            count += 1
            
print(count)       



