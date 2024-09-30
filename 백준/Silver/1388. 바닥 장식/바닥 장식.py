# 입력 처리
n, m = map(int, input().split())
floor = [input().strip() for _ in range(n)]

# 방문 체크 배열
visited = [[False] * m for _ in range(n)]

# 나무 판자 개수를 저장할 변수
plank_count = 0

# 탐색 함수
def dfs(x, y, symbol):
    visited[x][y] = True  # 현재 위치 방문 처리
    
    # 행 방향으로 탐색 (가로 나무판 '-')
    if symbol == '-':
        for ny in range(y + 1, m):
            if floor[x][ny] == '-' and not visited[x][ny]:
                visited[x][ny] = True
            else:
                break

    # 열 방향으로 탐색 (세로 나무판 '|')
    elif symbol == '|':
        for nx in range(x + 1, n):
            if floor[nx][y] == '|' and not visited[nx][y]:
                visited[nx][y] = True
            else:
                break

# 바닥 전체 탐색
for i in range(n):
    for j in range(m):
        if not visited[i][j]:  # 아직 방문하지 않은 칸일 때
            if floor[i][j] == '-':
                dfs(i, j, '-')
                plank_count += 1
            elif floor[i][j] == '|':
                dfs(i, j, '|')
                plank_count += 1

# 결과 출력
print(plank_count)
