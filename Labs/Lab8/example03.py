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
  column1 = []
  column2 = []
  column3 = []
  column4 = []
  column5 = []
  diag1 = []
  diag2 = []
  sum1 =0
  sum2 =0
  sum3 =0
  sum4 =0
  sum5 =0
  sum_1 =0
  sum_2 =0
  sum_3 =0
  sum_4 =0
  sum_5 =0
  sums1 =0
  sums2 =0

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
  if n == 2:
    column1.extend((list1[0],list1[2]))
    column2.extend((list1[1], list1[3]))
  elif n == 3:
    column1.extend((list1[0],list1[3], list1[6]))
    column2.extend((list1[1], list1[4],list1[7]))
    column3.extend((list1[2],list1[5],list1[8]))
  elif n == 4:
    column1.extend((list1[0],list1[4], list1[8],list1[12]))
    column2.extend((list1[1], list1[5],list1[9],list1[13]))
    column3.extend((list1[2],list1[6],list1[10],list1[14]))
    column4.extend((list1[3],list1[7],list1[11],list1[15]))
  elif n ==5:
    column1.extend((list1[0],list1[5], list1[10],list1[15],list1[20]))
    column2.extend((list1[1], list1[6],list1[11],list1[16],list1[21]))
    column3.extend((list1[2],list1[7],list1[12],list1[17],list1[22]))
    column4.extend((list1[3],list1[8],list1[13],list1[18],list1[23]))
    column5.extend((list1[4],list1[9], list1[14],list1[19],list1[24]))
  if n == 2:
    diag1.extend((list1[0],list1[3]))
    diag2.extend((list1[1],list1[2]))
  elif n == 3:
    diag1.extend((list1[0],list1[4],list1[8]))
    diag2.extend((list1[2],list1[4],list1[6]))
  elif n == 4:
    diag1.extend((list1[0],list1[5],list1[10],list1[15]))
    diag2.extend((list1[3],list1[6],list1[9],list1[12]))
  elif n == 5:
    diag1.extend((list1[0],list1[6],list1[12],list1[18],list1[24]))
    diag2.extend((list1[4],list1[8],list1[12],list1[16],list1[20]))
  for i in row1:
    sum1 += i
  for i in row2:
    sum2 += i
  for i in row3:
    sum3 += i
  for i in row4:
    sum4 += i
  for i in row5:
    sum5 += i
  for i in column1:
    sum_1 += i
  for i in column2:
    sum_2 += i
  for i in column3:
    sum_3 += i
  for i in column4:
    sum_4 += i
  for i in column5:
    sum_5 += i
  for i in diag1:
    sums1 += i
  for i in diag2:
    sums2 += i
  
  if sum1 == sum2 and sum2 == sum3 and sum3 == sum4 and sum4 == sum5 and sum5 == sum_1 and sum_1 == sum_2 and sum_2 == sum_3 and sum_3 == sum_4 and sum_4 == sum_5 and sum_5 == diag1 and diag1 == diag2:
    return "This is a magic square"
  
main()


#BU AMK kODU ÇALIŞMIYOR

