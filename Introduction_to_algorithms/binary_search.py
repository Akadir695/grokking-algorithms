"""Algorithms is set of instructions for accomplishing a task"""
# Binary search if the element that you are looking for is that list, it returns the position where it is located otherswise is null
# binary search is only works if the if your list is sorted
# low = 0, high = len(arr)-1
def binary_search(arr, item):
  low = 0
  high = len(arr)-1
  while low <= high:
    mid = (low + high) // 2
    guess = arr[mid] 
    if guess == item:
      return mid
    elif guess > item:
      high = mid -1
    else: 
      low = mid + 1
  return None

# in simple is we have 100items it takes 100 while binary search takes 7 times 
# BIG O notation tells how fast is an algorithms is: it counts the number of operation
"""algorithms is measured in number operations, 
a run of algorithms is expressed in big O operations
# Simple search — O(n)
# worst case you check every single element
# 100 elements = 100 operations

# Binary search — O(log n)
# worst case you check log2(n) elements
# 100 elements = 7 operations
Big O is how every programmer answers the question "will this still be fast when the data gets huge?
"""