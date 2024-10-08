from collections import deque
import sys
input = sys.stdin.read

def bfs(start, target):
    # 시작과 목표가 동일하면 이동 횟수는 0
    if start == target:
        return 0
    
    
    queue = deque([(start,  0)])  # (x, y, 이동 횟수)
    visited = set()  # 방문한 위치
    visited.add(start)  # 시작 위치 방문 기록 
    
    while queue:
        x,time = queue.popleft() 
        
        if x == target:
            return time
        
        for dx in (x - 1, x + 1, 2 * x):
            if 0 <= dx <= 100000 and dx not in visited:
                visited.add(dx)
                queue.append([dx,time+1])
   
    return -1 


N,M = input().split()

print(bfs(int(N), int(M)))