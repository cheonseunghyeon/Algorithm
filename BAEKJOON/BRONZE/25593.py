# 25593번 문제
# 31120KB 32MS

# 딕셔너리 값 비교 문제

import sys

number = int(sys.stdin.readline().strip())

time = [4,6,4,10]

user = {}

for i in range(number):
    for n in range(4): # 시간 기준으로 4개로 나눔
        user_list = sys.stdin.readline().split()
        count_list = list(filter(lambda x: x != "-",user_list)) # - 는 모두 제거
        
        for count in count_list:
            if count in user:
                user[count] += time[n] 
            else:
                user[count] = time[n]


if not user: # 직원이 없다면 YES
    print("Yes")
else: # 각 직원의 시간을 비교
    max_time = max(user.values())
    min_time = min(user.values())
    
    if max_time - min_time <= 12:
        print("Yes")
    else:
        print("No")