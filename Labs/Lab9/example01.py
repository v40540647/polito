def main():
  list1 = [1,1,2,1,9,8,1,55,4,8,7,999,969]
  print(Swap(list1))
  print(Moveright(list1))
  print(Evenwitzero(list1))
  print(larger(list1))
  print(popmiddle(list1))
  print(evensfront(list1))
  print(largest(list1))
  print(secondlargest(list1))
  print(constantlyinc(list1))
  print(adjacent(list1))
  print(duplicate(list1))
  

def Swap(a):
  newlist = a[:]
  newlist[-1] = a[0]
  newlist[0] = a[-1]
  return newlist

def Moveright(a):
  newlist= a[:]
  j = len(a)
  for i in range(0,j-1):
    newlist[i+1] = a[i] 
  newlist[0] = a[j-1]
  return newlist

def Evenwitzero(a):
  newlist = a[:]
  for i in range(0,len(a)):
    if (a[i] % 2) == 0:
      newlist[i] = 0
  return newlist

def larger(a):
  newlist = a[:]
  for i in range(1,len(a)-1):
    if newlist[i] > newlist[i-1] and newlist[i] > newlist[i+1]:
      continue
    else:
      if newlist[i-1] > newlist[i+1]:
        newlist[i] = newlist[i-1]+1
      else:
        newlist[i] = newlist[i+1]+1
  return newlist

def popmiddle(a):
  newlist = a[:]
  if len(a) %2 == 0:
    newlist.pop(len(a)//2)
    newlist.pop((len(a)//2)-1)
  else:
    newlist.pop(len(a)//2)
  return newlist

def evensfront(a):
  newlist = a[:]
  for i in range(0,len(a)):
    if a[i] % 2 == 0:
      for i in range(0,len(a)-1):
        newlist[i+1] = a[i]
      newlist[0] = a[i]
    else:
      continue
    ###Not working dunno why
  return newlist

def largest(a):
  i = 0
  for s in range(0,len(a)):
    if a[s]>i:
      i = a[s]
    else:
      continue

  return i

def secondlargest(a):
  newlist = a[:]
  newlist.sort()
  return newlist[-2]

def constantlyinc(a):
  i = 0
  for s in range(0,len(a)-1):
    if a[s] >a[s+1]:
      i+=1
    else:
      continue

  if i >0:return False
  else:return True
 

def adjacent(a):
  for s in range(1,len(a)):
    if a[s] == a[s-1]:
      return True
      break
    else:continue
  return False


def duplicate(a):
  newlist = []
  for i in range(0,len(a)):
    if a[i] in newlist:
      return True
      break
    else:
      newlist.append(a[i])

  return False


if __name__ == '__main__':
  main()