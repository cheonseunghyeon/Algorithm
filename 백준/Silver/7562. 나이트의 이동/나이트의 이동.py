from collections import deque

def bfs(start, target, l):
    # 시작과 목표가 동일하면 이동 횟수는 0
    if start == target:
        return 0
    
    # 나이트의 이동 방향
    directions = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    visited = set()  # 방문한 위치
    visited.add(tuple(start))  # 시작 위치 방문 기록 (리스트를 튜플로 변환)
    
    while queue:
        x, y, moves = queue.popleft()  # 현재 위치와 이동 횟수 가져오기
        
        # 나이트가 이동할 수 있는 위치 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # 새로운 위치 계산
            
            # 체스판 내에 있는지 확인
            if (0 <= nx < l) and (0 <= ny < l):
                # 목표 위치에 도착하면 이동 횟수 리턴
                if [nx, ny] == target:  # 리스트를 사용하여 비교
                    return moves + 1
                
                # 새로운 위치가 아직 방문하지 않은 경우
                if (nx, ny) not in visited:
                    visited.add((nx, ny))  # 방문 기록 추가 (튜플로 변환)
                    queue.append((nx, ny, moves + 1))  # 큐에 추가
    
    return -1  # 도달할 수 없는 경우 (실제 문제에서는 항상 도달 가능)

def knight_moves(test_cases):
    results = []
    for case in test_cases:
        l, start, target = case
        results.append(bfs(start, target, l))
    return results

import sys
input = sys.stdin.read

data = input().splitlines()
test_cases_count = int(data[0])
test_cases = []

line_idx = 1
for _ in range(test_cases_count):
    l = int(data[line_idx])
    start = list(map(int, data[line_idx + 1].split())) 
    target = list(map(int, data[line_idx + 2].split()))  
    test_cases.append((l, start, target))
    line_idx += 3

results = knight_moves(test_cases)
for result in results:
    print(result)
