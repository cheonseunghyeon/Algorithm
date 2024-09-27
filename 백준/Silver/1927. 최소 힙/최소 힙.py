import sys
import heapq

count_list = []
for _ in range(int(sys.stdin.readline().strip())):
    N = int(sys.stdin.readline().strip())
    if N != 0:
        heapq.heappush(count_list,N)   
    else:
        if count_list:
            print(heapq.heappop(count_list))
        else:
            print(0)
        