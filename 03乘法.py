n = input().split()
n = int(n[0])
def count_n(n):
    ans = n*(n+1)/2
    return ans
ans = count_n(n)
print(int(ans))
