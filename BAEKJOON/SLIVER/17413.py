# 17413번 문제
# 31900KB	176MS

# 태그가 있는 경우와 없는 경우를 산정
# 태그가 없는 경우 공백 기준으로 뒤집기
# 태그가 있는 경우 <를 식별하고 태그 안은 정상, 밖은 뒤집기

import sys

string = sys.stdin.readline().strip()

tag = False
result = []
temp = ""

for char in string:
  if char == "<":

    if temp: # <를 식별시 지금까지 적재한 문자 뒤집기
      result.append(temp[::-1])
      temp = ""

    result.append(char)
    tag = True # 태그 내부 상태로 변환

  elif char == ">": 
    result.append(char)
    tag = False # 태그 내부 상태가 끝났으니 변환

  elif tag:
    result.append(char) # 태그 내부 상태라면 정상 적재

  elif char == " ": # 공백 기준으로 뒤집기 
    result.append(temp[::-1])
    result.append(char)
    temp = ""

  else:
    temp += char # 뒤집기 전 값들을 적재 후 한 번에 뒤집기

if temp: # 태그가 끝난 후 그 뒤에 값이 있어 temp이 남는 경우 뒤집기
  result.append(temp[::-1])

print("".join(result)) # 모든 결과 조합