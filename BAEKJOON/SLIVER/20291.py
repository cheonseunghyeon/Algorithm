# 20291번 문제
# 125276KB	280MS

# 2번과 같이 리스트로 만들면 시간 초과가 걸림
import sys

count = int(sys.stdin.readline().strip())

list = {}

for _ in range(count):
  string = sys.stdin.readline().strip()

  if string.find("."): # .을 기준으로 확장자만 저장
    string = string[string.find(".") + 1:]

  if string in list:
    list[string] += 1 # 딕셔너리 key : 확장자, value : 횟수

  else:
    list[string] = 1 # key가 없다면 추가

sort_list = sorted(list.items()) # 사전 정렬

for key,value in sort_list:
  print('{} {}'.format(key,value))
