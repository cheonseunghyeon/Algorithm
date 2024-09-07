# 27160번 문제
# 과일 종류와 개수 배열 생성
# 총합 개수 비교 

count = int(input().strip())

list = []

for _ in range(count):
  string, number = input().strip().split()
  number = int(number)

  found = False  # 찾을 경우 값을 추가, 못 찾으면 리스트 추가

  for item in list:    # 과일 식별
    if item[0] == string:
      item[1] = item[1] + number
      found = True
      break

  if not found:
    list.append([string,int(number)]) # 과일 종류와 개수 적재

for total_item in list:
  found = False
  if int(total_item[1]) == 5:
    print("YES")
    found = True
    break

  if not found:
    print("NO")
  
