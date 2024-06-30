# 100 到1000能被56整除
ans_list = []
for i in range(100,1001):
    if i % 30 == 0:
        ans_list.append(i)

# 每10个数输出一行
for i in range(len(ans_list)):
    if i % 10 == 9:
        print(ans_list[i])
    else:
        print(ans_list[i], end=' ',)