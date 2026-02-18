def longest_unique(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):

        # If duplicate found, move left pointer
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # Add current character
        seen.add(s[right])

        # Update maximum length
        max_len = max(max_len, right - left + 1)

    return max_len


# Run
s = input()
print(longest_unique(s))






""" with charter means 
def longest_unique(s):
    seen = set()
    left = 0
    max_len = 0
    start = 0   # to remember where longest substring starts

    for right in range(len(s)):

        # If duplicate found → shrink window
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # Add current character
        seen.add(s[right])

        # Update max length and starting index
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    return max_len, s[start:start + max_len]


# Run
s = input()
length, substring = longest_unique(s)

print("Length:", length)
print("Substring:", substring)"""