import sys

N, M = sys.stdin.readline().strip().split()

sing_list = {}
for _ in range(int(N)):
    input_data = sys.stdin.readline().strip().split()
    name = input_data[1]
    code = "".join(input_data[2:5])
    
    if code in sing_list:
        sing_list[code] = "?"
    else:
        sing_list[code] = name

for _ in range(int(M)):
    input_code = "".join(sys.stdin.readline().strip().split())
    
    if input_code in sing_list.keys():
        print(sing_list[input_code])
    else:
        print("!")
