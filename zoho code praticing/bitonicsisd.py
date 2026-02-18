def bitonic_point(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # if mid is not first or last element
        if 0 < mid < len(arr) - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            elif arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            return arr[mid]


# ----------- INPUT PART -------------- o(log n )

n = int(input())                 # size of array
arr = list(map(int, input().split()))  # elements

print(bitonic_point(arr))

