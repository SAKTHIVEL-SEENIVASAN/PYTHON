n = 5
num = 1

for i in range(n):
    
    # If row is even → left to right
    if i % 2 == 0:
        for j in range(n):
            print(num, end=" ")
            num += 1
    
    # If row is odd → right to left
    else:
        temp = []
        for j in range(n):
            temp.append(num)
            num += 1
        
        for x in reversed(temp):
            print(x, end=" ")
    
    print()
    