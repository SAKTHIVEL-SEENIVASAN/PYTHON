n = 5

# Step 1: Create 2D matrix
arr = [[0]*n for _ in range(n)]

num = 1

# Step 2: Fill column by column
for col in range(n):
    for row in range(col+1):
        arr[row][col-row] = num
        num += 1

# Step 3: Print pattern
for i in range(n):
    
    # print leading spaces
    for s in range(i):
        print("  ", end="")
    
    # print numbers
    for j in range(n-i):
        print(arr[i][j], end="  ")
    
    print()
    