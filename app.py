import random

def quicksort(arr):
    if (len(arr) == 1 or len(arr) == 0):
        return arr
    pivot = random.choice(arr)

    low = [num for num in arr if num < pivot]
    equal = [num for num in arr if num == pivot]
    high = [num for num in arr if num > pivot]

    return quicksort(low) + equal + quicksort(high)

print(quicksort([7, 6, 1, 15, 4, 2, 3, 3, 4, 7, 8, 2, 11, 11, 9, 6, 11, 12, 24, 65, 23, 43, 12, 5, 6, 7, 4]))