from typing import List


n = int(input())
num_list = list(map(int, input().split()))


# 快速排序
def quick_sort(num_list: List, left: int, right: int):
    # 递归结束条件
    if left >= right:
        return
    point_i = left - 1
    point_j = right + 1
    point  = num_list[(left + right) // 2]
    while point_i < point_j:
        while True:
            point_i += 1
            if num_list[point_i] >= point:
                break
        while True:
            point_j -= 1
            if num_list[point_j] <= point:
                break
        if point_i < point_j:
            num_list[point_i], num_list[point_j] = num_list[point_j], num_list[point_i]
    quick_sort(num_list, left, point_j)
    quick_sort(num_list, point_j + 1, right)

quick_sort(num_list, 0, n - 1)
for i in range(n):
    print(num_list[i], end=' ')