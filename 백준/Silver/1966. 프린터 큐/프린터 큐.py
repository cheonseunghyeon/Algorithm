import sys
from collections import deque

def text(s):
    return [False, int(s)]

for _ in range(int(sys.stdin.readline())):
    count = 0
    N, M = map(int, sys.stdin.readline().split())
    
    # 문서의 중요도와 관심 여부를 deque로 저장
    test = deque(map(text, sys.stdin.readline().split()))
    test[M][0] = True  # 관심 문서 위치를 True로 설정
    
    while test:
        # 현재 문서의 중요도를 확인하여 가장 높은지 비교
        if test[0][1] == max(test, key=lambda x: x[1])[1]:
            count += 1
            # 관심 문서가 인쇄되면 출력 후 종료
            if test[0][0] == True:
                print(count)
                break
            else:
                test.popleft()  # 중요도가 맞으면 문서를 인쇄
        else:
            # 중요도가 낮으면 문서를 뒤로 보냄
            test.append(test.popleft())
