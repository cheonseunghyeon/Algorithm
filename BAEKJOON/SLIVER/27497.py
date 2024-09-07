# 20291번 문제
#56972KB	668MS

import sys
from collections import deque

number = int(sys.stdin.readline().strip())

# 값, 순서를 저장할 데크
que = deque()
rule = deque()

for i in range(number):
  inputs = sys.stdin.readline().strip().split()

  if(len(inputs) == 2):
      count = int(inputs[0])
      
      # 규칙에 따라 값과 순서 적재
      if count == 1:
        que.append(inputs[1])
        rule.append(True)
      elif count == 2:
        que.appendleft(inputs[1])
        rule.append(False)

# 3의 경우 입력 값이 1개          
  else:
    if inputs[0] == '3':
        if rule:   
            current_rule = rule.pop() # 넣은 순서대로 빼내서 실행
            if current_rule:
                que.pop()
            else:
                que.popleft()

if que:
    print("".join(que))
else:
    print(0)
    