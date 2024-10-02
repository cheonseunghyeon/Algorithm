from collections import deque
import sys
import heapq

dic = {}
def read():
    return sys.stdin.readline().strip()

def left(Input,root):
    return Input[0:root]

def right(Input,root):
    return Input[root +1:]  

def find(Input, count):
    if len(Input) == 1: # 한개만 있는 경우
        if count not in dic:
            dic[count] = [Input[0]]
        else:
            dic[count].append(Input[0])
        return
    
    root = len(Input)//2
    
    if count not in dic:
        dic[count] = [Input[root]]
    else:
        dic[count].append(Input[root])
    
    L = left(Input,root)
    R = right(Input,root)
    
    if L:
        find(L,count+1)
    if R:
        find(R,count+1)

N = read()

Input = read().split()
find(Input, 1)

for level in sorted(dic.keys()):
    print(" ".join(dic[level]))