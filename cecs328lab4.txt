from random import *
from math import *

# MSS O(nlogn) runtime ########################################################################################
def mss_nlogn(nums, beg, end):
    if beg == end:
        return nums[beg]
    mid = (beg + end) // 2
    mssLeft = mss_nlogn(nums, beg, mid)
    mssRight = mss_nlogn(nums, mid+1, end)
    mssIntersect = intersection(nums, beg, mid, end)
    return max(max(mssLeft, mssRight), mssIntersect)


def intersection(nums, beg, mid, end):
    i_sum = 0
    left_sum = -int(pow(2, 65))

    to_left = mid
    while to_left >= beg:
        i_sum += nums[to_left]
        if i_sum > left_sum:
            left_sum = i_sum
        to_left -= 1

    i_sum = 0
    right_sum = -int(pow(2, 65))
    to_right = mid+1
    while to_right <= end:
        i_sum += nums[to_right]
        if i_sum > right_sum:
            right_sum = i_sum
        to_right += 1

    return left_sum + right_sum

# MSS O(n) runtime ########################################################################################
def mss_n(nums):
    mss = 0
    n_sum = 0

    for i in nums:
        n_sum += i
        if n_sum > mss:
            mss = n_sum
        if n_sum < 0:
            n_sum = 0
    return mss


print("When n = user input: ------------------------------------------------------------------------------------------------")
n = int(input("Enter the size of the array: "))

randomNums = [randint(-100, 100) for i in range(n)]

print(randomNums)

print("O(nlogn): ", mss_nlogn(randomNums, 0, n-1))
print("O(n): ", mss_n(randomNums))
