"""  fine the unique number 1 1 2 3 3 """


""""2"""
def find_unique(arr):
    result = 0
    
    for num in arr:
        result ^= num
    
    return result


# INPUT
n = int(input())
arr = list(map(int, input().split()))

print(find_unique(arr))



"""find_missing the number from o to n 

def find_missing(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    
    return expected_sum - actual_sum


# INPUT
n = int(input())
arr = list(map(int, input().split()))

print(find_missing(arr))

"""