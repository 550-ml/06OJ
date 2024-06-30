# get n
n = int(input())

# get the list of numbers
number = list(map(int, input().split()))

odd_number = sorted([num for num in number if num % 2 != 0])
even_number = sorted([num for num in number if num % 2 == 0])

sorted_number = odd_number + even_number
print(' '.join(map(str, sorted_number)))

