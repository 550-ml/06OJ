(n, m , x) = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

j = m - 1
for i in range(n):
    while j>=0 and list1[i] + list2[j] > x:
        j -= 1
    if j >= 0 and list1[i] + list2[j] == x:
        print(i, j)
        break