import sys

def read():
    return sys.stdin.readline().strip()

N = int(read())

Input = set(map(int,read().split()))

ticket = 1

while ticket in Input:
    ticket += 1
    
print(ticket)
