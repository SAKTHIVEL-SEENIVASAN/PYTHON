import heapq

def kth_smallest(arr, k):
    heap = arr.copy()        # copy to avoid modifying original
    heapq.heapify(heap)      # convert list into min heap
    
    for _ in range(k - 1):
        heapq.heappop(heap)  # remove smallest k-1 times
    
    return heapq.heappop(heap)  #kth smallest     heapify → O(n)  each pop → O(log n) total → O(n + k log n) 


# -------- INPUT PART --------
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

print(kth_smallest(arr, k))





"""    Kth Largest
import heapq

def kth_largest(arr, k):
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


# -------- INPUT PART --------
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

print(kth_largest(arr, k))"""