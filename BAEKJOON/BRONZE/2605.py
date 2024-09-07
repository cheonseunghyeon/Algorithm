# 2605번 문제
# 31120KB	32MS

# 배열의 리스트 관리 문제
import sys

number = int(sys.stdin.readline().strip())
list = list(map(int,sys.stdin.readline().split()))

result = []

for i in range(number):
    result.insert(len(result) - list[i] , i + 1) # insert를 사용하여 해당하는 인덱스에 삽입

print(" ".join(map(str,result)))
