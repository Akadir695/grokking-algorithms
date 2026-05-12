# very recursion function has two case  the recursive base and the base case 
def countdown(i):
  print(i)
  if i <= 1:
    return
  else:
    countdown(i-1)
countdown(3)
"""countdown(3)
  → prints 3
  → calls countdown(2)
      → prints 2
      → calls countdown(1)
          → prints 1
          → i <= 1, so STOP (return)
"""
# the stack 
def greet(name):
  print("How are you," + name)
  greet2(name)
  print("greeting ready to say bye....")
  by()
# this func greets then calls another functions
def greet2(name):
  print("how are you, " + name +  '?')
def by():
  print("Ok by!  ")
greet("Alice")
"""|
|  greet2  |  ← runs first (on top)
|  greet   |  ← paused, waiting for greet2 to finish
"""
# the call stack with recursion 
def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)
print(fact(3))
