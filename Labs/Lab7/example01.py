from random import randint

def main():
  list1 = []
  i = len(list1)
  
  while i < 12:
    
    list1.append(randint(1,100))
    i +=1
  print(f"main list is {list1} , evens are {evens(list1)} , reversed list is {reversem(list1)} and lastnfirst are {returninglastnfirst(list1)}")

def evens(number):
  list2 = []
  for i in number:
    if i % 2 == 0:
      list2.append(i)
  return list2
def samenumber(number):
  #bunu da beceremedim
  
  return None

def reversem(incoming_list):
  list2 = incoming_list [:]
  return list2[::-1]

def returninglastnfirst(slatt):
  y = slatt[0]
  z = slatt[-1]
  return y , z

main()

    
