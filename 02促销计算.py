
def calculate_Sn(a, n):
    total_sum = 0  
    term = 0  
    
    for _ in range(n):
        term = term * 10 + a  
        total_sum += term  
    
    return total_sum


a, n = input().split()
a = int(a)
n = int(n)


result = calculate_Sn(a, n)
print(result)