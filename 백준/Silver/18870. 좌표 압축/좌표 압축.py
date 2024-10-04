import sys

def read():
    return sys.stdin.readline().strip()

N = int(read())
Input = list(map(int, read().split())) 

sort_Input = sorted(set(Input))  
dic = {value: idx for idx, value in enumerate(sort_Input)}

compressed_result = [str(dic[x]) for x in Input]
print(" ".join(compressed_result))
