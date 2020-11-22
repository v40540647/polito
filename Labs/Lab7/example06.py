from random import randint

def main ():
  list1 = []
  i = 0
  while i < 10:
    list1.append(randint(0,99))
    i += 1
  print(list1)
  print(reversem(list1))

def reversem(incoming_list):
  list2 = incoming_list [:]
  return list2[::-1]

main()