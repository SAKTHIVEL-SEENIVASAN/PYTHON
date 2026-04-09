# ENCODE
a = input("Enter string: ")

encoded = ""

for ch in a:
    encoded += str(1) + "#" + ch

print("Encoded:", encoded)


# DECODE
s = encoded
i = 0
decoded = []

while i < len(s):
    
    # find #
    j = s.find("#", i)
    
    # length before #
    length = int(s[i:j])
    
    # get character
    decoded.append(s[j+1 : j+1+length])
    
    # move pointer
    i = j + 1 + length

print("Decoded:", "".join(decoded))