
def slidingWindow(numbers, k):
  biggestSum = 0
  currSum = 0  
  for i in range(len(numbers)):
    currSum += numbers[i]
    if i >= k:
      currSum -= numbers[i - k]
    biggestSum = max(biggestSum, currSum)
  return biggestSum

def slidingWindow2(numbers, k):    
    biggestSum = 0    
    currSum = 0
    left = 0
    for right in range(len(numbers)):
        # currSum = -3
        currSum += numbers[right]
        
        while (
            (right - left + 1 > k) or
            (left < right and numbers[left] < 0) or
            (right == len(numbers) - 1 and right - left + 1 > 1)
        ):
            currSum -= numbers[left] # -3 - (-3) = -3 + 3 = 0
            left += 1        
        
        biggestSum = max(biggestSum, currSum)

    return biggestSum
      
print(slidingWindow2([1, 2, 3, -4, 5, 5, 6, -22, 19], 3))