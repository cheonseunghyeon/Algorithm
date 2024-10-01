from collections import deque
import sys

def read():
    return sys.stdin.readline().strip()

# 입력 받기
B = [int(read().split()[1]) for _ in range(int(read()))]

Test = []  # 스택
count = 0

# 각 빌딩의 높이를 처리하는 루프
for i in B:
    if i == 0:
        Test = []  # 0이 들어오면 스택 초기화 (모든 건물이 끝났다고 간주)
        continue
    
    while Test and Test[-1] > i:  # 현재 높이보다 높은 건물은 끝났다고 간주하고 스택에서 제거
        Test.pop()
    
    if not Test or Test[-1] < i:  # 스택이 비어 있거나 현재 높이가 마지막 건물보다 크면 새로운 건물 시작
        Test.append(i)
        count += 1  # 새로운 건물 시작이므로 카운트 증가

# 최소 건물 개수 출력
print(count)
