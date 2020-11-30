def main():
  list1 = []
  slatt = int(input("enter n for n x n matrix: "))
  for i in range(0,(slatt*slatt)) :
    list1.append(int(input()))
  j = row_creator(list1,slatt)
  print(j)

def row_creator(list1 , n):
  row1 = []
  row2 = []
  row3 = []
  row4 = []
  row5 = []
  if n == 2:
    for i in range(0,2):
      row1.append(list1[i])
    for j in range(2,4):
      row2.append(list1[j])
  elif n == 3:
    for i in range(0,3):
      row1.append(list1[i])
    for j in range(3,6):
      row2.append(list1[j])
    for x in range(6,9):
      row3.append(list1[x])
  elif n == 4:
    for i in range(0,4):
      row1.append(list1[i])
    for j in range(4,8):
      row2.append(list1[j])
    for x in range(8,12):
      row3.append(list1[x])
    for f in range(12,16):
      row4.append(list1[f])
  elif n == 5:
    for i in range(0,5):
      row1.append(list1[i])
    for j in range(5,10):
      row2.append(list1[j])
    for x in range(10,15):
      row3.append(list1[x])
    for f in range(15,20):
      row4.append(list1[f])
    for z in range(20,25):
      row5.append(list1[z])
  else:
    return "Bro I cant calculate that"
  return row1,row2,row3,row4,row5
  
main()



    


