from random import randint
list1 = []
i = 0
while i < 21:
  list1.append(randint(0,99))
  i += 1
print(f"List is {list1}")

newlist = list1 [:]
newlist.sort()
print(f"Sorted list is {newlist}")

