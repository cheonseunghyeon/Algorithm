from collections import deque

def bfs(x, y, pasture, visit, directions):
    r, c = len(pasture), len(pasture[0])
    queue = deque([(x, y)])
    visit[x][y] = 1

    while queue:
        cur_x, cur_y = queue.popleft()
        
        for dx, dy in directions:
            new_x, new_y = cur_x + dx, cur_y + dy
            
            if 0 <= new_x < r and 0 <= new_y < c and not visit[new_x][new_y] and pasture[new_x][new_y] == '#':
                visit[new_x][new_y] = 1
                queue.append((new_x, new_y))

r, c = map(int, input().split())
pasture = [input().strip() for _ in range(r)]

visit = [[0] * c for _ in range(r)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

clump_count = 0

for i in range(r):
    for j in range(c):
        if pasture[i][j] == '#' and not visit[i][j]:
            bfs(i, j, pasture, visit, directions)
            clump_count += 1

# 결과 출력
print(clump_count)
