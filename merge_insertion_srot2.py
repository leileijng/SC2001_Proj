import time
import random
import matplotlib.pyplot as plt



def hybrid_sort(arr, s):
    if len(arr) <= s:
        return insertion_sort(arr)
    else:
        mid = len(arr) // 2
        left = hybrid_sort(arr[:mid], s)
        right = hybrid_sort(arr[mid:], s)
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Ask user for input
arr= input("Enter a list of numbers, separated by spaces: ").split()
arr = [int(num) for num in arr]

# Set the threshold
threshold = 4

# Sort the arrayay using the hybrid algorithm
a=hybrid_sort(arr, threshold)

# Print the sorted arrayay
print("Sorted array:", a)






# #Part 2 and 3

# sizes = [1000, 10000, 100000, 1000000, 10000000]
# x = 1000000
# s = 10

# comparisons = []

# for size in sizes:
#     arr = [random.randint(1, x) for _ in range(size)]
#     start = time.time()
#     hybrid_sort(arr, s)
#     end = time.time()
#     comparisons.append(end - start)

# print(comparisons)
# plt.plot(sizes, comparisons)
# plt.title('Number of Key Comparisons vs Input Size')
# plt.xlabel('Input Size')
# plt.ylabel('Number of Key Comparisons')
# plt.show()