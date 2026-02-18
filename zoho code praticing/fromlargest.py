arr = list(map(str, input().split()))

n = len(arr)

# Bubble sort based on x+y and y+x
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] + arr[j+1] < arr[j+1] + arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

result = ''.join(arr)

# handle case like 0 0
if result[0] == '0':
    print('0')
else:
    print(result)