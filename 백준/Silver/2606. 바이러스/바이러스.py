from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    count = 0  # 감염된 컴퓨터 수

    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1  # 감염된 컴퓨터 수 증가

    return count

n = int(input()) 
m = int(input())  

graph = [[] for _ in range(n + 1)]  # 인덱스 0은 사용하지 않음
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)  # 방문 여부 초기화
infected_count = bfs(1, graph, visited)

print(infected_count)
