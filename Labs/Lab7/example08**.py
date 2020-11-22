from random import randint

def main():
  list1 = []
  i = 0
  while i < 10:
    list1.append(randint(0,50))
    i += 1
  print(list1)
  for i in list1:
    for i in range(1,9):
      if i > ((list1[i-1] + list1[i+1])//2):
        list1.pop(i)
    
  print(list1)

main()