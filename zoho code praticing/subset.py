def subset(a, b):
    f  ={}
    for i in a:
        f[i]=f.get(i , 0)+1
    for i in b:
        if f.get(i , 0)==0:
            return False
        f[i]-=1
    return True       




a= list(map(int, input().split()))
b=list(map(int, input().split()))
print(subset(a, b))