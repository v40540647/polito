def main():
  list1 =[1,4,9,16,]
  list2 =[4,6,7,9,21,21,21]
  j =Sortedmerge(a=list1 , b=list2)
  print(j)
def Sortedmerge(a,b):
  list3 = []
  if len(a)>= len(b):
    for i in range(0,len(b)):
      if a[i] <= b[i]:
        list3.append(a[i])
        list3.append(b[i])
      else:
        list3.append(b[i])
        list3.append(a[i])
    for s in range(len(b),len(a)):
      list3.append(a[s])
  else:
    for i in range(0,len(a)):
      if a[i] <= b[i]:
        list3.append(a[i])
        list3.append(b[i])
      else:
        list3.append(b[i])
        list3.append(a[i])
    for s in range(len(a),len(b)):
      list3.append(b[s])
  return list3

# Eksik cunku eger list1 in 2. elemani list2 nin 1. elemanindan kucuk ise calismayacaktir. bu daha cok index karsilastirma makinesi oldu




main()