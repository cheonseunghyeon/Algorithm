import sys
import heapq
count_list = []
user = 0
count = 0
for n in range(int(sys.stdin.readline().strip())):
    if n == 0:    
        user = (int(sys.stdin.readline().strip()))
    else:
        heapq.heappush(count_list, - int(sys.stdin.readline().strip()))


while count_list and user <= -count_list[0]:
    max_num = heapq.heappop(count_list)
    
    user += 1
    heapq.heappush(count_list,max_num + 1)
    
    count += 1
    
print(count)
