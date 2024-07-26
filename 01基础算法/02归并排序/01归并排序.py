

n = int(input())
num_list = list(map(int, input().split()))

def fen(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = fen(arr[:mid])
    right = fen(arr[mid:])
    return merge(left, right)

def merge(left, right):
    res =[]
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res += left
    res += right
    return res

ans = fen(num_list)
print(' '.join(map(str, ans)))