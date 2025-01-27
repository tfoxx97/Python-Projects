import time

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return f"{item} found at index: {mid}"
        elif arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return f"Could not find {item} in list"

my_list = [x for x in range(5, 1001)]
print(binary_search(my_list, 66))

def binary_search_recursive(arr, low, high, item):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return f"{item} found at index: {mid}"
        elif arr[mid] > item:
            return binary_search_recursive(arr, low, mid - 1, item)
        else:
            return binary_search_recursive(arr, mid + 1, high, item)
    return f"Could not find {item} in list"

print(binary_search_recursive(my_list, min(my_list), max(my_list), 66))

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

start = time.time()
print(selectionSort([3, 7, 9, 5, 1, 6, 4]))
ellapsed_time = time.time() - start
print(f"Selection sort: {ellapsed_time:.4f} seconds")

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

start = time.time()
print(quickSort([3, 7, 9, 5, 1, 6, 4]))
ellapsed_time = time.time() - start
print(f"Quick sort: {ellapsed_time:.4f} seconds")

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # recursion occuring until down to base case
        mergeSort(left)
        mergeSort(right)

        # temp values: i iterates through left, j iterates through right, k through arr
        # compare left and right and accordingly append lesser item to arr
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                # compare next index to j (until j index is moved)
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # in the case of left or right being completely emptied, the remaining elements
        # will be added to arr
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr

start = time.time()
print(mergeSort([3, 7, 9, 5, 1, 6, 4]))
ellapsed_time = time.time() - start
print(f"Merge sort: {ellapsed_time:.4f} seconds")
    
    
