import sys

#아스키 코드로 a ~ z를 키로 등록
alp_dict = {chr(97 + i): i for i in range(27)}
total = 0

N = int(sys.stdin.readline().strip())
input_data = list(sys.stdin.readline().strip())
    
for alp in range(0,len(input_data)):
    count = ((alp_dict[input_data[alp]]+ 1) * (31**(alp))) 
    total += count
    
print(total)
