def main():
  list1 = [6,9,4,2,0,9,9,9]
  list2 = [9,1,1,7,8,]
  gg = merge(list1,list2)
  print(gg)

def merge(a,b):
  list3 = []
  if len(b) >= len(a):
    for i in range(0,len(a)):
      list3.append(a[i])
      list3.append(b[i])
    for j in range(len(a) , len(b)):
      list3.append(b[j])
  else:
    for i in range(0,len(b)):
      list3.append(a[i])
      list3.append(b[i])
    for j in range(len(b) , len(a)):
      list3.append(a[j])
  return list3


main()
