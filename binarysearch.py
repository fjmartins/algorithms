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


# print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))


# [0, 0, 1, 1, 1, 1, 1, 3, 3, 4, 5, 6, 7] target=1 -1
# [0, 1, 1, 1, 2]

def findLastRepeatedNumberIndex(numbers, target): # O(n)
    start = 0
    end = len(numbers) - 1

    while(start <= end):
        mid = (start + end) // 2

        if target > numbers[mid]:
            start = mid + 1
        elif target < numbers[mid]:
            end = mid - 1
        else:
            if mid < len(numbers) - 1:
                for index in range(mid + 1, len(numbers)):
                    if numbers[index] != target:
                        return index - 1
            else:
                return mid

    return -1


def findLastRepeatedNumberIndex1(numbers, target): # O(log n)
    start = 0
    end = len(numbers) - 1
  
    while(start <= end):
        mid = (start + end) // 2
        
        if target > numbers[mid]:
            start = mid + 1
        elif target < numbers[mid]:
            end = mid - 1
        else:
            # se o teu mid ja eh o ultimo elemento do array
            if mid == len(numbers) - 1:
                return mid
            # quando ele n eh o ultimo elemento do array,
            # entao ele so vai ser a ultima ocorrencia se o proximo elemento
            # nao for o target
            if numbers[mid + 1] != numbers[mid]:
                return mid

            start = mid + 1
    
    return -1
        
print(findLastRepeatedNumberIndex1([0, 0, 1, 1, 1, 1, 1, 3, 3, 4, 5, 6, 7], 3))