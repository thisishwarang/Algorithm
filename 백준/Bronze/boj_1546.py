N = int(input())
score_list = list(map(int, input().split()))

max_score = max(score_list)
new_score_list = []
new_sum = 0
new_avg = 0

for score in score_list:
    new_score = score / max_score * 100
    new_score_list.append(new_score)

for new_score in new_score_list:
    new_sum += new_score

new_avg = new_sum / len(new_score_list)

print(new_avg)