n = int(input())
num_list = list(map(int, input().split()))

num_dict = dict.fromkeys(num_list, 0)
num = 0
j = 0
for i in range(n):
    num_dict[num_list[i]] += 1
    while num_dict[num_list[i]] > 1:
        num_dict[num_list[j]] -= 1
        j += 1
    num = max(num, i - j + 1)
print(num)