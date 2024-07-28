def lower_bound(arr, target):
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

(n ,q) = map(int, input().split())
num_list = list(map(int, input().split()))

def get_low_and_high(num_list, target):
    low = lower_bound(num_list, target)
    high = lower_bound(num_list, target + 1) - 1
    return low, high
for i in range(q):
    target = int(input())
    low, high = get_low_and_high(num_list, target)
        
    if (high<low):
        print("-1 -1")
    else:
        print(low,end=" ")
        print(high)