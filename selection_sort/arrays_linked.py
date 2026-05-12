"""Arrays: elements are numbered, it starts from 0
the position of arrays is called index
Start at address 00
Item     →  1st  2nd  3rd  4th  5th
Index    →   0    1    2    3    4
Lots of inserts → lean towards linked list
Lots of reads → lean towards array
You were close in your thinking, you just applied it the wrong way around! Does that make sense?
the 4 is index of 4
Fifth item is at address 04
You can jump straight to it — no searching needed
Arrays are good at reads
arrays are good at for sequential and random access 
Exactly right! Each node in a linked list carries extra overhead for storing the pointer(s), unlike an array which stores just the raw data.
Array of 4 integers:
[ 10 | 20 | 30 | 40 ]
 4B    4B   4B   4B   = 16 bytes total

Linked list of 4 integers:
[ 10 | ptr ] → [ 20 | ptr ] → [ 30 | ptr ] → [ 40 | null ]
  4B + 8B       4B + 8B        4B + 8B         4B + 8B     = 48 bytes total
"""
items = [10, 20, 30, 40]

# Random access — O(1)
print(items[2])  # 30

# Sequential access — O(n)
for item in items:
    print(item)
    
#Example of selection sort
def findSmallest(arr):
    smallest = arr[0]       
    smallestIndex = 0
    for i in range(1, len(arr)):   
        if arr[i] < smallest:      
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

def selectSort(arr):
    new_arr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        new_arr.append(copiedArr.pop(smallest))
    return new_arr


