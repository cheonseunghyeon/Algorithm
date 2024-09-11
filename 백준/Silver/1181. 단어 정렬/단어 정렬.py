# 입력 받기
N = int(input())
words = set()

# 중복 제거를 위해 set에 단어 저장
for _ in range(N):
    words.add(input().strip())

# 정렬: 먼저 단어의 길이로 정렬하고, 길이가 같으면 사전순으로 정렬
sorted_words = sorted(words, key=lambda x: (len(x), x))

# 결과 출력
for word in sorted_words:
    print(word)
