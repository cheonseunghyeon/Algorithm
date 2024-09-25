# 22867번 문제
# 53208KB	 732ms
import heapq
import sys

total_heap = []

def total_col(hh, mm, ss, sss):
    return (int(hh) * 1000 * 60 * 60) + (int(mm) * 1000 * 60) + (int(ss) * 1000) + int(sss)

for _ in range(int(input())):
    input_data = sys.stdin.readline().strip().split()
    
    in_hh, in_mm, in_ss = input_data[0].split(":")
    in_ss, in_sss = in_ss.split(".")
    in_time = total_col(in_hh, in_mm, in_ss, in_sss)
    
    out_hh, out_mm, out_ss = input_data[1].split(":")
    out_ss, out_sss = out_ss.split(".")
    out_time = total_col(out_hh, out_mm, out_ss, out_sss)
    
    heapq.heappush(total_heap, (in_time, 1)) # 들어오는 시간 +1
    heapq.heappush(total_heap, (out_time, -1)) # 나가는 시간 -1

max_count = 0
current_count = 0

# 힙에서 우선 순위 큐로 이벤트를 시간 순으로 처리 
while total_heap:
    time, change = heapq.heappop(total_heap)
    current_count += change
    max_count = max(max_count, current_count)

print(max_count)
