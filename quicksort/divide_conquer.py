# divide and conquer 
def sum(arr):
  total = 0
  for x in arr:
    total += x
  return total
print(sum([1,2, 3, 4]))
# write recursive function to find the number items in the list
# we can do this with loop 
def count_items(arr):
  counter = 0
  for x in arr:
    counter = counter + 1
  return counter
print(count_items([1, 2, 3, 4]))  
# recurcive function
def recursive_items(arr):
  if arr == []:
    return 0
  return 1 + recursive_items(arr[1:])
print(recursive_items([10, 2, 3, 4])) 
def recursive_sum(list):
    # Base case: If the list is empty, the count is 0
    if list == []:
        return 0
    # Recursive case: 1 (for the current item) + the count of the rest of the list
    return list[0] + recursive_sum(list[1:])
print(recursive_sum([1, 2, 3, 4]))  
# write a function that finds the maximum number in the list
# let do this with a loop
def maximun_num(list):
    highest_num = list[0]
    for x in list:
        if x > highest_num:
            highest_num = x
    return highest_num
print(maximun_num([1, 2, 3, 4]))  
def recursive_maximun_num(list):
    # Base case: if the list has one element, return it
    if len(list) == 1:
        return list[0]
    # Recursive case: find the max of the rest
    max_rest = recursive_maximun_num(list[1:])
    # Compare first element with max of the rest
    if list[0] > max_rest:
        return list[0]
    else:
        return max_rest
print(recursive_maximun_num([1, 2, 3, 4]))  