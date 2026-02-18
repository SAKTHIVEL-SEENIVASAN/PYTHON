def sathi(a, n):
    f ={}
    for i in a:
        f[i]=f.get(i, 0)+1
    max_freq= max(f.values())
    max_counter= list(f.values()).count(max_freq)
    time =(max_freq-1)*(n+1)+max_counter
    return max(len(a), time)    

a = input().split()
n = int(input())
print(sathi(a , n))