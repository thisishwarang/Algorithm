N = int(input())
words = []

for i in range(N):
    words.append(input().strip())

words = list(set(words))

words.sort(key=lambda x: (len(x), x))

for w in words:
    print(w)