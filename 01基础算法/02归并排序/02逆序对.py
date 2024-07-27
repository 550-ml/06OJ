n = int(input())
num_list = list(map(int, input().split()))


def fen(num_list):
    if len(num_list) == 1:
        return num_list, 0
    mid = len(num_list) // 2
    left, left_cont = fen(num_list[:mid])
    right, right_cont = fen(num_list[mid:])
    res, res_cont = merge(left, right)
    return res, left_cont + right_cont + res_cont


def merge(left, right):
    i = j = 0
    res = []
    cont = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            cont += len(left) - i
    res += left[i:]
    res += right[j:]
    return res, cont


res, res_cont = fen(num_list)
print(res_cont)
