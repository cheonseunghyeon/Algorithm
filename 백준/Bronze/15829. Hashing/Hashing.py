import sys

# 아스키 코드로 a ~ z를 키로 등록
alp_dict = {chr(97 + i): i + 1 for i in range(26)}  # a=1, b=2, ..., z=26
total = 0

# 상수 정의
r = 31
M = 1234567891

# 입력 받기
N = int(sys.stdin.readline().strip())
input_data = list(sys.stdin.readline().strip())

# 해시 값 계산
for i in range(N):
    # 각 알파벳의 값에 31의 i승을 곱하고 M으로 나눠서 나머지를 구함
    total += (alp_dict[input_data[i]] * (r ** i)) % M
    total %= M  # 계속해서 M으로 나누어 나머지를 유지

print(total)
