# 11478번 문제
# 240712KB	476MS

# 문자열을 모든 경우의 수로 분할 후 중복 제거
import sys

list = set() # 중복 제거
string = sys.stdin.readline().strip()

for i in range(len(string)):
  for s in range(i,len(string)):
    list.add(string[i:s+1]) # 자릿수를 한 자리씩 늘리며 set에 적재

print(len(list))
