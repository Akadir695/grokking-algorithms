# divide and conquer 
def sum(arr):
  total = 0
  for x in arr:
    total += x
  return total
print(sum([1,2, 3, 4]))
# How do we this recursion
# Exercises
def sum(list):
    # Base case: If the list is empty, the count is 0
    if list == []:
        return 0
    
    # Recursive case: 1 (for the current item) + the count of the rest of the list
    return list[0] + sum(list[1:])

print(sum([1, 2, 3, 4]))  
