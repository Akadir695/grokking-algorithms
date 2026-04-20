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
my_list = [1, 3, 5, 7, 9] 
print(binary_search(my_list, 3))
# in simple is we have 100items it takes 100 while binary search takes 7 times 