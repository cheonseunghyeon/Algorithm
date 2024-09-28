import sys

def read():
    return sys.stdin.readline().strip()

# 테스트 케이스 수
for _ in range(int(read())):
    n = int(read())
    clothes = {}
    
    # 의상 정보를 입력받아 종류별로 분류
    for _ in range(n):
        item, category = read().split()
        if category not in clothes:
            clothes[category] = []
        clothes[category].append(item)
    
    # 모든 종류별 입지 않는 경우의 수를 포함해 조합 수 계산
    count = 1
    for category in clothes:
        count *= (len(clothes[category]) + 1) # +1은 해당 종류의 의상을 안 입는 경우
    
    # 알몸인 경우는 제외
    print(count - 1)
