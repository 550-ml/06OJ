(n, m) = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

point_a = 0
point_b = 0

while point_a < n and point_b < m:
    if list_a[point_a] == list_b[point_b]:
        point_a += 1
        point_b += 1
    else:
        point_b += 1

if point_a == n:
    print("Yes")
else:
    print("No")