(n, k) = map(int, input().split())
num_list = list(map(int, input().split()))


# 快速排序
def choice_k(num_list, l, r, k):
    if l>=r:
        return
    point_i = l - 1
    point_j = r + 1
    point = num_list[(l+r)//2]
    while point_i< point_j:
        while True:
            point_i += 1
            if num_list[point_i] >= point:
                break
        while True:
            point_j -=1
            if num_list[point_j] <= point:
                break

        if point_i<point_j:
            num_list[point_i], num_list[point_j] = num_list[point_j], num_list[point_i]
        
    if point_j < k-1:
        choice_k(num_list, point_j+1, r, k)
    else:
        choice_k(num_list, l, point_j, k)

choice_k(num_list, 0, n-1, k)
print(num_list[k-1])
