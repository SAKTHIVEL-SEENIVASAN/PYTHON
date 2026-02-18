def count_and_say(n):
    result = "1"
    
    for _ in range(n - 1):
        new = ""
        i = 0
        
        while i < len(result):
            count = 1
            while i + 1 < len(result) and result[i] == result[i+1]:
                count += 1
                i += 1
            
            new += str(count) + result[i]
            i += 1
        
        result = new
    
    return result


# INPUT
n = int(input())
print(count_and_say(n))


"""⏱ Complexity

Outer loop runs n times
Inner loop reads full string

Total approx → O(n × length)

Length grows, but usually manageable."""