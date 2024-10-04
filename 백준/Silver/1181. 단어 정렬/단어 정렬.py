import sys

def read():
    return sys.stdin.readline().strip()

N = int(read())
Input = [read() for _ in range(N)]
Input = list(set(Input))

Input.sort()  
for i in range(1, len(Input)):
    for j in range(i, 0, -1):
        if len(Input[j]) < len(Input[j-1]):
            Input[j], Input[j-1] = Input[j-1], Input[j]


for item in Input:
    print(item)
