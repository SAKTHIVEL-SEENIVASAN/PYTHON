def spiral_matrix(matrix):
    result = []
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        
        # Left → Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Top → Bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Right → Left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # Bottom → Top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result


# INPUT
n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

print(*spiral_matrix(matrix))



"""
3
10 20 30
40 50 60
70 80 90



🧠 Core Idea

Use 4 boundaries:

top
bottom
left
right

Move:

→ right
↓ down
← left
↑ up

Then shrink boundaries.

⏱ Complexity

Every element visited once.

👉 O(n²)
"""


