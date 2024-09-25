import sys
from collections import deque

number = int(sys.stdin.readline().strip())

que = deque()
rule = deque()

for i in range(number):
  inputs = sys.stdin.readline().strip().split()

  if(len(inputs) == 2):
      count = int(inputs[0])
      
      if count == 1:
        que.append(inputs[1])
        rule.append(True)
          
      elif count == 2:
        que.appendleft(inputs[1])
        rule.append(False)
          
  else:
    if inputs[0] == '3':
        if rule:   
            current_rule = rule.pop()
            if current_rule:
                que.pop()
            else:
                que.popleft()

if que:
    print("".join(que))
else:
    print(0)
    