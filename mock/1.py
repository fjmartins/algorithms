# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

# https://leetcode.com/problems/single-number/

# Example 1:
nums = [2,2,1]
nums1 = [2, 2, 3, 3, 4]
# Output: 1

def findUniqueNumber(arr):
    # space complexity is linear
    arr.sorted()
    
    length = len(arr) - 1
    for index in range(0, length, 2):
        if index + 1 <= length:
            if arr[index] != arr[index + 1]:
                return arr[index]
        else:
            return arr[index]

# [2, 2, 3, 3, 4] => 5 elementos
# { 2: 2, 3: 2, 4: 1 } => 3 elementos

from collections import defaultdict
def getUniqueNumberHash(nums): # len(nums) = n
    freq = defaultdict(int)
    for num in nums: # O(n)
        freq[num] += 1
    for num in freq: # time complexity O(n/2 + 1)
        # space: O(n/2 + 1) = O(n)
        if freq[num] == 1:
            return num
# O(n+n) = O(2n) = O(n)
# O(n)

# XOR => exclusive or
# 0 ^ 0 = 0
# 1 ^ 1 = 0
# 0 ^ 1 = 1

# a ^ 0 = a
# a ^ a = 0

# a ^ b ^ b
# a ^ (b ^ b)
# a ^ (0)
# a
# a ^ b ^ b ^ c ^ c ^ d ^ d...
def getUniqueNumberWithBitManipulation(nums):
    unique = 0
    for num in nums:
        unique ^= num
    return unique
# time = O(n), space = O(1)

print(getUniqueNumberHash(nums1))