from random import randint

def main():
  list1 = []
  i = 0
  while i < 7:
    list1.append(randint(0,99))
    i += 1
  list1.sort()
  print(list1)
  j =sumWithoutSmallest(list1) - list1[0] 
  print(j)

def sumWithoutSmallest(incoming_list):
  a = 0
  for i in range(0,len(incoming_list)-1):
    a += incoming_list[i+1]
  return a


main()