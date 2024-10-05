from collections import deque

def find_kinship(n, person1, person2, relations):
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    
    # 부모 자식 관계 그래프에 저장
    for x, y in relations:
        graph[x].append(y)
        graph[y].append(x)
    
    # BFS 탐색
    def bfs(start):
        visited = [-1] * (n + 1)
        queue = deque([start])
        visited[start] = 0
        
        while queue:
            current = queue.popleft()
            
            for neighbor in graph[current]:
                if visited[neighbor] == -1:  
                    visited[neighbor] = visited[current] + 1
                    queue.append(neighbor)
                    
        return visited
    
    # 촌수 계산
    visited = bfs(person1)
    
    return visited[person2] if visited[person2] != -1 else -1

n = int(input())  # 사람의 수
person1, person2 = map(int, input().split())  # 촌수 계산할 두 사람
m = int(input())  # 부모 자식 간의 관계 수
relations = [tuple(map(int, input().split())) for _ in range(m)]

print(find_kinship(n, person1, person2, relations))
