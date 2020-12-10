def main ():
  list1 = [999,69,420,115,98,31]
  j = removemin(list1)
  print(j)
 

def removemin(listname):
  a = 2147483647
  for i in range(0,len(listname)):
    if i == listname[0]:
      continue
    if listname[i] > listname[i-1] and listname[i] < a:
      a = listname[i-1]
  listname.pop(listname.index(a))
  return listname

main()
