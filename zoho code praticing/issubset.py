def is_subset(arr1, arr2):
    i = 0
    j = 0
    
    n = len(arr1)
    m = len(arr2)
    
    while i < n and j < m:
        
        if arr1[i] < arr2[j]:
            i += 1
            
        elif arr1[i] == arr2[j]:
            i += 1
            j += 1
            
        else:
            return False
    
    return j == m


# INPUT
n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

if is_subset(arr1, arr2):
    print("Yes")
else:
    print("No")
    
    
    
    
    
"""  

6
1 2 3 4 5 6
3
2 4 6


O(n + m)
"""    