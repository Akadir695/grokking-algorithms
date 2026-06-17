# Hash tables is function where you put in string- meaning any data and you get back a number 
"""it needs to constant meaning if you put apple you get 3 you should 3 all should get 3
hash function maps different strings to diffrent indexes
if we put hash function and array we get hash table , but in the realiy we use the same for diffrent items
one -to-one mapping is called injective function
python has hash tables which is called dictionaries
to make hash table in python we use empty braces
book = {}
it has keys and values  book["apple" ]= 0.67 apples is keys and value is 0.67 
"""
book = {}
book["apple" ]= 0.67
book["milk" ]= 1.49
book["avocado" ]= 1.49
print(book) # {'apple': 0.67, 'milk': 1.49, 'avocado': 1.49}
print(book["avocado"]) # 1.49
# use cases
"hash tables are great when you want to create one-to-one mapping and looking up things"
phone_book = {}
phone_book['jenny'] = '723894332'
phone_book['ahmed'] = '732439222'
print(phone_book["jenny"])
# preventing duplicates we can filter duplicates
voted = {}

def check_voter(name):
  if name in voted:
    print(f'{name} has voted')
  else:
    voted[name] = True
    print("let them vote")
check_voter('akadir')
check_voter('akadir')
# we use hash tables as cache(it is common way to make things faster like like serving webpages to users)
"collision happens when two keys are assigned to the same slot"
"it does not matter if the hash table has one element or billion elements it always takes the same amount of time "
"to avoid the the worst-case performance you need a load factor and good hash functio(one has has no collions)"


