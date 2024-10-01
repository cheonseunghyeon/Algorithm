from collections import deque
import sys

def read():
    return sys.stdin.readline().strip()

L = deque()
dic = {}
count = 0
student = 0
for _ in range(int(read())):
    Input = list(map(int,read().split()))
    
    if Input[0] == 1:
        L.append(Input[1])
        if count < len(L):
            count = len(L)
            student = L[-1]
            
        elif count == len(L):
            student = min(student, L[-1])
            
    elif Input[0] == 2:
        if L:
            L.popleft()
    
print(f'{count} {student}')
