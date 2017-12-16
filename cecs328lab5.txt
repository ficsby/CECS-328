from random import *
import time
import statistics

def build_maxheap(a):
    for i in range(len(a), -1, -1):
        max_heapify(a, i)
    return a


def max_heapify(a, i):
    max_index = i
    left_index = 2*i+1
    right_index = 2*i+2

    if left_index < len(a) and a[left_index] > a[max_index]:
        max_index = left_index

    if right_index < len(a) and a[right_index] > a[max_index]:
        max_index = right_index

    if max_index != i:
        temp = a[max_index]
        a[max_index] = a[i]
        a[i] = temp
        max_heapify(a, max_index)


def heap_sort(a):
    temparray ={}
    build_maxheap(a)
    for i in range(len(a)-1, -1, -1):
        temp = a[0]
        a[0] = a[i]
        a[i] = temp
        temparray[i] = a.pop()
        max_heapify(a, 0)

    return temparray

def selection_sort(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j

        a[i], a[min] = a[min], a[i]

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

# User chooses array size n #####################################################
print("When n = user input: ------------------------------------------------------------------------------------------------")
n = int(input("Enter the size of the array: "))

conversion = 1000000000  # conversion unit from seconds to nanoseconds
reps = 1

avg_time_selection = 0
print("Selection Sort ----------------------------------------------------------------------------------")
for i in range(reps):
    a = [randint(-10000, 10000) for i in range(n)]
    print("Before Selection Sort: ", a)
    nano = int(round(time.time() * conversion))
    selection_sort(a)
    print("After Selection Sort: ", a)
    avg_time_selection += int(round(time.time() * conversion)) - nano
avg_time_selection /= reps

avg_time_quicksort = 0
print("\nQuick Sort ----------------------------------------------------------------------------------")
for i in range(reps):
    a = [randint(-10000, 10000) for i in range(n)]
    nano = int(round(time.time() * conversion))
    print("Before Quick Sort: ", a)
    selection_sort(a)
    print("After Quick Sort: ", a)
    avg_time_quicksort += int(round(time.time() * conversion)) - nano
avg_time_quicksort /= reps

avg_time_heap = 0
print("\nHeap Sort ----------------------------------------------------------------------------------")
for i in range(reps):
    a = [randint(-10000, 10000) for i in range(n)]
    nano = int(round(time.time() * conversion))
    print("Before heap Sort: ", a)
    temp = heap_sort(a)
    print("After heap Sort: ", temp)
    avg_time_heap += int(round(time.time() * conversion)) - nano
avg_time_heap /= reps
print("\nAverage Times ----------------------------------------------------------------------------------")
print("Average run-time of selection sort: ", avg_time_selection, "ns")
print("Average run-time of quick sort: ", avg_time_quicksort, "ns")
print("Average run-time of heap sort: ", avg_time_heap, "ns")