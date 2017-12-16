import statistics
import sys
from random import *
import time
import math

def quicksort(nums):
    if len(nums) <= 3:
        nums.sort()
        return nums
    else:
        pivot = statistics.median([nums[0], nums[len(nums) // 2], nums[len(nums) - 1]])
        left = [i for i in nums if i < pivot]
        pivot_list = [k for k in nums if k == pivot]
        right = [j for j in nums if j > pivot]

        return quicksort(left) + pivot_list + quicksort(right)


def insertionsort(nums):
    for i in range(len(nums)-1):
        ind = i
        while ind >= 0 and nums[ind] > nums[ind+1]:
            nums[ind], nums[ind+1] = nums[ind+1], nums[ind]
            ind -= 1
    return nums


convert = 1000000000  # conversion unit from seconds to nanoseconds
# User chooses array size n #####################################################
print("When n = user input: ------------------------------------------------------------------------------------------------")
n = int(input("Enter the size of the array: "))

randomNums = [randint(-7000, 7000) for i in range(n)]

nano = int(round(time.time() * convert))
quicksort(randomNums)
qs_time = int(round(time.time() * convert)) - nano

nano = int(round(time.time() * convert))
insertionsort(randomNums)
is_time = int(round(time.time() * convert)) - nano

print("Quicksort: ", qs_time, "ns")
print("Insertion sort: ", is_time, "ns")

# Array size n = 10000 #####################################################
print("\nWhen n = 10000: ------------------------------------------------------------------------------------------------")
n = 10000
rep = 100
qs_time = 0
is_time = 0
randomNums = [randint(-7000, 7000) for n in range(n)]
for i in range(rep):
    nano = int(round(time.time() * convert))
    quicksort(randomNums)
    qs_time += int(round(time.time() * convert)) - nano

randomNums = [randint(-7000, 7000) for n in range(n)]
for j in range(rep):
    nano = int(round(time.time() * convert))
    insertionsort(randomNums)
    is_time += int(round(time.time() * convert)) - nano

avg_qs_time = qs_time/rep
avg_is_time = is_time/rep
print("Quicksort: ", avg_qs_time, "ns")
print("Insertion sort: ", avg_is_time, "ns")

# Number of Instructions for 1 second: --> T(n) = inputsize * Avg. Runtime
avg_is_time_s = avg_is_time / (n*n*convert) #convert nano seconds to seconds
num_instructions = 1/avg_is_time_s
print("Number of instructions for 1 second: ", num_instructions)