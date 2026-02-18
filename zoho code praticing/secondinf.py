def second_largest(arr):
    first = float('-inf')
    second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        
        elif num > second and num != first:
            second = num
    
    if second == float('-inf'):
        return -1   # no second largest
    
    return second


# INPUT
n = int(input())
arr = list(map(int, input().split()))

print(second_largest(arr))