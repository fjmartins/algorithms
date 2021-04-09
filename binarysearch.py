# find the index of a random number inside a sorted list

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 7 -> return 6

def binarySearch(numbers, target):
    start = 0
    end = len(numbers) - 1    
    
    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] < target:
          start = mid + 1
        elif numbers[mid] > target:
          end = mid - 1
        else:
          return mid
        
    return -1


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))