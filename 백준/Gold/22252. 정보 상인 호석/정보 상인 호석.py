import heapq
import sys

# 고릴라별로 정보를 저장할 딕셔너리와 호석이가 구매한 정보를 저장할 총합 변수
dic = {}
total_value = 0  # 호석이가 구매한 정보들의 총 가치를 저장할 변수

# 쿼리 개수 입력받기
Q = int(input())

# 쿼리 처리
for _ in range(Q):
    input_data = sys.stdin.readline().strip().split()
    command = input_data[0]  # '1' 또는 '2'
    name = input_data[1]  # 고릴라의 이름

    # 고릴라가 새로운 정보를 얻는 경우
    if command == '1':
        k = int(input_data[2])  # 얻은 정보의 개수
        values = list(map(int, input_data[3:3 + k]))  # k개의 정보를 읽어서 리스트로 만듦

        if name not in dic:
            dic[name] = []  # 새로운 고릴라일 경우 리스트 초기화
        for value in values:
            heapq.heappush(dic[name], -value)  # 최대 힙처럼 사용하기 위해 음수로 저장

    # 호석이가 정보를 구매하는 경우
    elif command == '2':
        b = int(input_data[2])  # 구매할 정보의 개수

        # 고릴라가 가진 정보가 있는 경우에만 처리
        if name in dic:
            for _ in range(min(b, len(dic[name]))):  # 구매할 수 있는 최대 개수만큼 추출
                total_value += -heapq.heappop(dic[name])  # 음수로 저장된 값을 다시 양수로 변환하여 합산

# 결과 출력
print(total_value)
