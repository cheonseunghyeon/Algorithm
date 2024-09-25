# 3986번 문제
# 32684KB	 100ms

import sys
count = 0

for i in range(int(input())):

    check_list = []
    line = list(sys.stdin.readline().strip()) 

    # 현재 값과 스택 마지막 값 비교
    for item in line:
        if check_list and check_list[-1] == item: 
            check_list.pop()
        else:
            check_list.append(item)
            
    if not check_list:
        count += 1
   
print(count)
