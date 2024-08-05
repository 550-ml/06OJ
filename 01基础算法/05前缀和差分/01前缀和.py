(n, m) = map(int, input().split())
num_list = list(map(int, input().split()))
s = [0]*(n+1)

for i in range(n):
    if i == 0:
        s[i] = num_list[i]
    else:
        s[i] = s[i-1] + num_list[i]
for _ in range(m):
    l, r = map(int, input().split())
    print(s[r-1] - s[l-1] + num_list[l-1])