
def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif target > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

list_input = input("Enter the list of numbers: ")
list_a = [int(num) for num in list_input.split(",")]  
sorted_list = sorted(list_a)

target_element = int(input("Enter a target element: "))
result = binary_search(sorted_list, target_element)

if result != -1:
    print(f"{target_element} found at index {result}")
else:
    print(f"{target_element} not found in list")