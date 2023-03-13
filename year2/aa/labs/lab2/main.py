# ▒▄▀▄▒▄▀▄  c. AA | FAF | FCIM | UTM | Spring 2023
# ░█▀█░█▀█  FAF-212 Cristian Brinza lab2 

# Importing the required libraries for this script
import time  # Library for time-related functions
import matplotlib.pyplot as plt  # Library for data visualization
import random  # Library for generating random numbers



# Define empty lists for holding arrays with small and large ranges
'''
These lines define 10 empty lists which will be used later on in the code. The names of the lists indicate that they will be used to store different ranges of numbers.
These empty lists will be used to store values in the for loop that follows.
Each list is used to store values from a different range that will be generated later on.
'''
s_range = [] # Small range 1
s_range2 = [] # Small range 2
s_range3 = [] # Small range 3
s_range4 = [] # Small range 4
s_range5 = [] # Small range 5
l_range = [] # Large range 1
l_range2 = [] # Large range 2
l_range3 = [] # Large range 3
l_range4 = [] # Large range 4
l_range5 = [] # Large range 5

# Create 50000 random integers and append them to the arrays
# Append random integers to the arrays
for i in range(50000):
    s_range.append(random.randint(0, 100))
    s_range2.append(random.randint(0, 100))
    s_range3.append(random.randint(0, 100))
    s_range4.append(random.randint(0, 100))
    s_range5.append(random.randint(0, 100))
    l_range.append(random.randint(0, 1000000))
    l_range2.append(random.randint(0, 1000000))
    l_range3.append(random.randint(0, 1000000))
    l_range4.append(random.randint(0, 1000000))
    l_range5.append(random.randint(0, 1000000))


# Define the heap sort algorithm
'''
This code defines a heap_sort function that takes an array as an input and returns the sorted array. It sorts the array in place using the heap sort algorithm, which uses a max heap data structure.
The heap_sort function first finds the length of the input array and builds a max heap out of it using the build_max_heap function.
Then, the function loops through the array from the end to the beginning using a for loop. At each iteration, it swaps the first element (which is the largest element in the heap) with the ith element, where i is the current index of the loop. It then heapifies the array again using the heapify function.
Finally, the function returns the sorted array.
The build_max_heap and heapify functions are not defined in this code snippet and should be defined elsewhere in the code or imported from a library. These functions are common in heap sort implementations and are used to create and maintain the heap structure.
'''
# Define a function called heap_sort that takes an array as an argument
def heap_sort(arr):
    # Find the length of the array
    n = len(arr)
    # Build a max heap out of the array
    build_max_heap(arr, n)
    # Loop through the array from the end to the beginning
    for i in range(n - 1, 0, -1):
        # Swap the first element with the ith element
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the array again
        heapify(arr, i, 0)
    # Return the sorted array
    return arr


# Define the build_max_heap function, used in the heap sort algorithm
def build_max_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Define the heapify function, used in the build_max_heap function and the heap sort algorithm
'''
This is a function that implements the heapify operation on an array
It takes three arguments:
arr: the array to be heapified
n: the size of the array
i: the index of the current node being heapified
'''
def heapify(arr, n, i):
    largest = i # initialize the largest node as the current node
    left_child = 2 * i + 1 # calculate the index of the left child
    right_child = 2 * i + 2 # calculate the index of the right child

    # if left child is larger than largest, update largest
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # if right child is larger than largest, update largest
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # if largest is not the current node, swap the values of largest and current node
    # and recursively call heapify on the affected child node
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Define the merge sort algorithm
# This is a function called merge_sort that takes an array as input

def merge_sort(arr):
# The function takes an input array "arr".
# It first checks if the length of the array is greater than 1.
# If the array length is 1 or less, it is already sorted, so the function simply returns the array.
    if len(arr) > 1:
        # If the array length is greater than 1, the function recursively divides the array into two halves.
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        # After the array is divided, the function then merges the two halves back together in sorted order.
        # It does this by comparing the first elements of each half and putting the smaller element in the first position of a new array.
        # It then repeats this process for the second elements, third elements, etc. until the entire array is sorted.
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1
        # After comparing and merging all elements in both halves, the function checks if any elements remain in either half.
        # If elements remain in the left half, they are added to the new array.
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        # If elements remain in the right half, they are added to the new array.
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    # Finally, the function returns the sorted array.
    return arr

# Define the quick sort algorithm
'''
This function is an implementation of the quicksort algorithm, a divide and conquer sorting algorithm.
It takes an array (arr) to be sorted, as well as two indices (low and high) that determine the subarray of arr to be sorted by this recursive call.
'''
def quick_sort(arr, low, high):
# Check if there are at least two elements in the current subarray to sort. If there is only one or zero,
# then there is nothing to sort and we return.
    if low < high:
        
        # Use the partition function (not shown here) to find the pivot index that splits the subarray into
        # two subarrays, one containing elements smaller than the pivot and one containing elements larger than
        # the pivot. 
        partition_index = partition(arr, low, high)
        
        # Recursively call quicksort on the left and right subarrays of the pivot index.
        
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)


#This is a function named "partition" that takes three arguments: an array (arr), a low index (low), and a high index (high).
def partition(arr, low, high):
    # This line sets the pivot element as the last element of the array.
    pivot = arr[high]
    # This line initializes the variable i as low - 1.
    i = low - 1
    # This line starts a loop that iterates from low to high - 1.
    for j in range(low, high):
        # This line checks if the jth element of the array is less than the pivot element.
        if arr[j] < pivot:
            # This line increments i by 1.
            i += 1
            # This line swaps the ith and jth elements of the array.
            arr[i], arr[j] = arr[j], arr[i]
    # This line swaps the (i+1)th and high elements of the array.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # This line returns the index of the pivot element.
    return i + 1

# This function is called counting_sort and takes in an array as input.
def counting_sort(arr):
    # Find the maximum element in the input array and cast it to an integer.
    max_element = int(max(arr))

    # Create a list called count with length of the maximum element + 1, and fill it with zeros.
    count = [0 for _ in range(max_element + 1)]

    # Iterate through the input array, incrementing the count of the current element in the count list.
    for i in arr:
        count[i] += 1

    # Create a temporary variable and initialize it to zero.
    temp = 0

    # Iterate through each element in the count list and for each non-zero value, 
    # set the corresponding number of elements in the input array to the current element value.
    for i in range(max_element + 1):
        for j in range(count[i]):
            arr[temp] = i
            temp += 1

    # Return the sorted array.
    return arr



# An empty list to store results
results = []

# A temporary list to store sorted arrays
temp = []

# Quick sort
start = time.time()
temp = quick_sort(s_range.copy(), 0, len(s_range) - 1)
temp = quick_sort(s_range2.copy(), 0, len(s_range2) - 1)
temp = quick_sort(s_range3.copy(), 0, len(s_range3) - 1)
temp = quick_sort(s_range4.copy(), 0, len(s_range4) - 1)
temp = quick_sort(s_range5.copy(), 0, len(s_range5) - 1)
end = time.time()
results.append(round(end - start, 8) / 5)

# Merge sort
start = time.time()
temp = merge_sort(s_range.copy())
temp = merge_sort(s_range2.copy())
temp = merge_sort(s_range3.copy())
temp = merge_sort(s_range4.copy())
temp = merge_sort(s_range5.copy())
end = time.time()
results.append(round(end - start, 8)/5)

# Heap sort
start = time.time()
temp = heap_sort(s_range.copy())
temp = heap_sort(s_range2.copy())
temp = heap_sort(s_range3.copy())
temp = heap_sort(s_range4.copy())
temp = heap_sort(s_range5.copy())
end = time.time()
results.append(round(end - start, 8)/5)

# Counting sort
start = time.time()
temp = counting_sort(s_range.copy())
temp = counting_sort(s_range2.copy())
temp = counting_sort(s_range3.copy())
temp = counting_sort(s_range4.copy())
temp = counting_sort(s_range5.copy())
end = time.time()
results.append(round(end - start, 8))

# Plotting the results
plt.figure(1)
plt.bar(['Quick sort', 'Merge sort', 'Heap sort',
        'Counting sort'], results, color='red')
plt.title('Sorting array of 50000 elements with small range (values 0 to 100)')
plt.xlabel('Algorithms')
plt.ylabel('Time in seconds')

'''
 ^
/ \
 |
This script compares the execution time of four sorting algorithms (Quick sort, Merge sort, Heap sort, and Counting sort) on arrays of 50000 elements with small ranges (values 0 to 100).

- The time library is imported to measure the execution time of each sorting algorithm.
- The matplotlib.pyplot library is imported to visualize the results.
- An empty list results is initialized to store the execution time of each algorithm.
- A temporary list temp is initialized to store the sorted arrays.
- Five ranges of integers are defined to be sorted (s_range, s_range2, s_range3, s_range4, and s_range5).
- For each sorting algorithm, the script measures the execution time to sort all five ranges and calculates the average time per range. The sorted arrays are stored in temp.
- The execution time for each algorithm is appended to the results list.
- Finally, a bar plot is created using plt.bar() to visualize the results.
'''


# An empty list to store results
results = []

# A temporary list to store sorted arrays
temp = []

# Run quicksort on 5 different arrays, measuring time for each
start = time.time()
temp = quick_sort(l_range.copy(), 0, len(l_range) - 1)
temp = quick_sort(l_range2.copy(), 0, len(l_range2) - 1)
temp = quick_sort(l_range3.copy(), 0, len(l_range3) - 1)
temp = quick_sort(l_range4.copy(), 0, len(l_range4) - 1)
temp = quick_sort(l_range5.copy(), 0, len(l_range5) - 1)
end = time.time()
results.append(round(end - start, 8) / 5)

# Run mergesort on 5 different arrays, measuring time for each
start = time.time()
temp = merge_sort(l_range.copy())
temp = merge_sort(l_range2.copy())
temp = merge_sort(l_range3.copy())
temp = merge_sort(l_range4.copy())
temp = merge_sort(l_range5.copy())
end = time.time()
results.append(round(end - start, 8)/5)

# Run heapsort on 5 different arrays, measuring time for each
start = time.time()
temp = heap_sort(l_range.copy())
temp = heap_sort(l_range2.copy())
temp = heap_sort(l_range3.copy())
temp = heap_sort(l_range4.copy())
temp = heap_sort(l_range5.copy())
end = time.time()
results.append(round(end - start, 8)/5)

# Run countingsort on 5 different arrays, measuring time for each
start = time.time()
temp = counting_sort(l_range.copy())
temp = counting_sort(l_range2.copy())
temp = counting_sort(l_range3.copy())
temp = counting_sort(l_range4.copy())
temp = counting_sort(l_range5.copy())
end = time.time()
results.append(round(end - start, 8))

plt.figure(2) # This creates a new figure with figure number 2. A figure is a container for all the plot elements, such as axes, legends, and annotations.
plt.bar(['Quick sort', 'Merge sort', 'Heap sort',
        'Counting sort'], results, color='green') # These lines set the title, xlabel, and ylabel for the plot. The title describes the task being performed and the range of values being sorted, the xlabel describes the different algorithms being compared, and the ylabel describes the units of measurement for the results.

'''
Next lines set the title, xlabel, and ylabel for the plot. The title describes the task being performed and the range of values being sorted, the xlabel describes the different algorithms being compared, and the ylabel describes the units of measurement for the results.
'''
plt.title('Sorting array of 50000 elements with large range (values 0 to 100000)')
plt.xlabel('Algorithms')
plt.ylabel('Time in seconds') 

plt.show() # This displays the plot on the screen.