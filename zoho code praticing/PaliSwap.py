def can_be_palindrome_by_one_swap(s):
    if s == s[::-1]:
        return True
    
    n = len(s)
    s = list(s)
    
    for i in range(n):
        for j in range(i+1, n):
            s[i], s[j] = s[j], s[i]
            
            if s == s[::-1]:
                return True
            
            s[i], s[j] = s[j], s[i]  # swap back
    
    return False


# INPUT
s = input().strip()

if can_be_palindrome_by_one_swap(s):
    print("Yes")
else:
    print("No")\
        
        
        
        
'''🧠 Core Idea

Check if string == reverse

If not → try swapping every pair

If any swap makes palindrome → YES

⏱ Complexity

Two loops → O(n²)

Palindrome check → O(n)

Total → O(n³) (worst case)

But string size usually small.'''        