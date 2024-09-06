# 1302번 문제
# 31120KB	28MS

# 딕셔너리의 값을 비교 후 최댓 값 호출
import sys

count = int(sys.stdin.readline().strip())

max = 0
max_key = ""
list = {}

for _ in range(count):
  string = sys.stdin.readline().strip()

  if string in list:
    list[string] += 1
  else:
    list[string] = 1

sort_list = sorted(list.items(), key=lambda x: (x[1], x[0]))
for key,value in sort_list:
  if value > max:
    max = value
    max_key = key

print(max_key)