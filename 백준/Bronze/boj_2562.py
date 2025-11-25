num_list = []

for i in range(9):
    N = int(input())
    num_list.append(N)

max_num = max(num_list)
i = num_list.index(max_num) + 1

print(max_num)
print(i)