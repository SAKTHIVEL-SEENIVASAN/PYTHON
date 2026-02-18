import heapq
def sl (a , k ):
    heapq.heapify(a)
    for i in range (k-1):
        heapq.heappop(a)
    return heapq.heappop(a)

a = list(map(int,input().split()))
n = len(a)

k = int(input())
print(sl(a ,n-k+1))     