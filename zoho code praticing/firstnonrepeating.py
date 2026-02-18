def first_non_repeating(s):
    freq = {}

    # Count frequency
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Find first non-repeating
    for ch in s:
        if freq[ch] == 1:
            return ch

    return -1


# Input
s = input()
print(first_non_repeating(s))\
    
    
    
    
    
    
    
    
    
    
    
    
    
"""def all_non_repeating(s):
    freq = {}

    # Step 1: Count frequency
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    result = ""

    # Step 2: Collect characters that appear once
    for ch in s:
        if freq[ch] == 1:
            result += ch

    if result == "":
        return -1

    return result


# Input
s = input()
print(all_non_repeating(s))"""    
    