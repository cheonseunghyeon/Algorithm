from collections import deque

def bfs(graph, start, end, weight_limit, n):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            return True
        
        for next_node, limit in graph[node]:
            if not visited[next_node] and limit >= weight_limit:
                visited[next_node] = True
                queue.append(next_node)
    
    return False

n, m = map(int, input().split())  # n: 섬의 개수, m: 다리의 개수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())  # a번 섬과 b번 섬 사이에 중량 제한이 c인 다리
    graph[a].append((b, c))
    graph[b].append((a, c))

start_factory, end_factory = map(int, input().split())

# 이분 탐색 범위 설정
low, high = 1, 1000000000
result = low

while low <= high:
    mid = (low + high) // 2
    
    # BFS로 중량 mid가 가능한지 확인
    if bfs(graph, start_factory, end_factory, mid, n):
        result = mid
        low = mid + 1  # 더 높은 중량을 시도
    else:
        high = mid - 1  # 중량을 낮춰야 함

print(result)
