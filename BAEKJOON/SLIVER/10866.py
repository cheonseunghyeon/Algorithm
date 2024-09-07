# 10866번 문제
# 34088KB	64MS
# 데크 사용법 문제

import sys
from collections import deque

number = int(sys.stdin.readline().strip())

result = deque()

for i in range(number):

  inputs = sys.stdin.readline().strip().split()
  if len(inputs) == 2:
    command = inputs[0]
    count = int(inputs[1])

    if command == "push_front":
      result.appendleft(count)
    elif command == "push_back":
      result.append(count)

  else:
    command = inputs[0]
    if command == "front":
      if result:
        print(result[0])
      else:
        print(-1)
    elif command == "back":
      if result:
        print(result[len(result) - 1])
      else:
        print(-1)
    elif command == "pop_front":
      if result:
        print(result[0])
        result.popleft()
      else:
        print(-1)
    elif command == "pop_back":
      if result:
        print(result[len(result) - 1])
        result.pop()
      else:
        print(-1)
    elif command == "size":
      print(len(result))
    elif command == "empty":
      if len(result) == 0:
        print(1)
      else:
        print(0)