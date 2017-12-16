import statistics
from random import *

def findkleast(nums, k):
    # if(len(nums) > 3):
    pivot = statistics.median([nums[0], nums[len(nums) // 2], nums[len(nums) - 1]])
    left = [i for i in nums if i < pivot]
    pivot_list = [k for k in nums if k == pivot]
    right = [j for j in nums if j > pivot]

    if len(left)+1 == k:
        return pivot
    else:
        if len(left)+1 > k:
            return findkleast(left, k)
        else:
            return findkleast(right, k - len(left)+1)
    # else:
    #     nums.sort()
    #     return nums[k-1]



n = int(input("Enter the size of the array n = "))

array = [randint(-100, 100) for i in range(n)]
print("Your array: ", array)

k = int(input("Enter a number between 1 to n: "))
print(findkleast(array, k))