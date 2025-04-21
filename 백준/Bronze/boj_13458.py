N = int(input())
tester = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0

for i in range(len(tester)):
    answer += 1
    if tester[i] - B > 0:
        answer += (tester[i] - B) // C
        if (tester[i] - B) % C != 0:
            answer += 1
    
print(answer)