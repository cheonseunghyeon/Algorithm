#25501번 문제

def recursion(s, l, r):
    global counter # 글로벌 변수 사용
    counter+= 1

    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

number = int(input())

if 1<= number <= 1000:
  for i in range(number):
    enter = input().strip()
    
    if 1<= len(enter) <= 1000:
      counter = 0  # 반복문이 실행될 때마다 초기화
      print(isPalindrome(enter),  counter) 