import sys
import heapq
def read():
    return sys.stdin.readline().strip()

N = int(read())
for _ in range(N):
    Num = int(read())
    Input = [list(map(int,read().split())) for _ in range(Num)]
    
    # O(N^2) 이라 시간초과
    # for i in range(1,Num):
    #     for j in range(i,0,-1):
    #         if Input[j][0] < Input[j-1][0]:
    #             Input[j],Input[j-1] = Input[j-1], Input[j]
    Input.sort()
    count = 1
    min = Input[0][1] 
    

    for i in range(1, Num):
        if Input[i][1] < min:
            count += 1
            min = Input[i][1] 
    
    print(count)