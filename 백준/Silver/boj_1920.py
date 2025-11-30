N = int(input())
n_list = set(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

for m in m_list:
    if m in n_list:
        print(1)
    else :
        print(0)