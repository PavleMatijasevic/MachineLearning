def sum_arr(arr):
    total = 0
    for elem in arr:
        total += elem
    return total

def find_min(arr):
    if not arr:
        return "Array is empty"
    min_elem = arr[0]

    for elem in arr:
        if elem < min_elem:
            min_elem = elem
    return min_elem

def split_and_add(arr, k):
    if k <= 0 or k>= len(arr):
        return arr
    
    first_part = arr[:k]
    second_part = arr[k:]

    result = second_part + first_part

    return result

def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            decreasing = False
        elif arr[i] < arr[i-1]:
            increasing = False
    return increasing or decreasing

arr = [2,3,4,5,2,7,1,8]
arr1 = [1,2,3,4,5]
k = 3
print(arr)
print("Sum of array: ", sum_arr(arr))
print("Minimum of array: ", find_min(arr))
print("Array after spliting and adding: ", split_and_add(arr, k))
print("Is array monotonic? ", is_monotonic(arr))




