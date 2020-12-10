row1 = [0,101,101,101,101,101,101,101,101,10]
row2 = [10,10,10,10,10,10,10,10,10,10]
row3 = [10,10,10,10,10,10,10,10,10,10]
row4 = [10,10,20,20,20,20,20,20,10,10]
row5 = [10,10,20,20,20,20,20,20,10,10]
row6 = [10,10,20,20,20,20,20,20,10,10]
row7 = [20,20,30,30,40,40,30,30,20,20]
row8 = [20,30,30,40,50,50,40,30,30,20]
row9 = [30,40,50,50,50,50,50,50,40,30]


def main():
  

  table(row1,row2,row3,row4,row5,row6,row7,row8,row9)
  print("++++++++++++++++++++++++++++++++++++++++++++++++++")
  manual(10)
  #print(choose((input("Enter Row")),int(input("Enter Column"))))
  
  table(row1,row2,row3,row4,row5,row6,row7,row8,row9)




def table(a,b,c,d,e,f,g,h,j):
  print("Coulmn 0   1   2   3   4   5   6   7   8   9")
  print("-----------------------------------------------")
  print(f"RowA  {a}")
  print(f"RowB  {b}")
  print(f"RowC  {c}")
  print(f"RowD  {d}")
  print(f"RowE  {e}")
  print(f"RowF  {f}")
  print(f"RowG  {g}")
  print(f"RowH  {h}")
  print(f"RowJ  {j}")

def choose(row,column):
  if row == "A":
    if row1[column] > 0:
      row1.pop(column)
      row1.insert(column, 0 )
    else:
      return "Your Seat Was reserved by another person"
  elif row == "B":
    if row2[column] > 0:
      row2.pop(column)
      row2.insert(column, 0 )
    else:
      return "Your Seat Was reserved by another person"
  elif row == "C":
    if row3[column] > 0:
      row3.pop(column)
      row3.insert(column, 0 )
    else:
      return "Your Seat Was reserved by another person"
  elif row == "D":
    if row4[column] > 0:
      row4.pop(column)
      row4.insert(column, 0 )
    else:
      return "Your Seat Was reserved by another person"
  elif row == "E":
    if row5[column] > 0:
      row5.pop(column)
      row5.insert(column, 0 )
    else:
      return "Your Seat Was reserved by another person"
  elif row == "F":
    if row6[column] > 0:
      row6.pop(column)
      row6.insert(column, 0 )
    else:
      return "Your Seat Was reserved by another person"
  elif row == "G":
    if row7[column] > 0:
      row7.pop(column)
      row7.insert(column, 0 )
    else:
      return "Your Seat Was reserved by another person"
  elif row == "H":
    if row8[column] > 0:
      row8.pop(column)
      row8.insert(column, 0 )
    else:
      return "Your Seat Was reserved by another person"
  elif row == "J":
    if row9[column] > 0:
      row9.pop(column)
      row9.insert(column, 0 )
    else:
      return "Your Seat Was reserved by another person"
  return "YOUR RESERVATION HAS BEEN DONE SUCCESFULLY"
  

def manual(price):
  for i in range(0,len(row1)):
    if price == row1[i]:
      row1.pop(i)
      row1.insert(i,0)
      break
    else:
      for i in range(0,len(row2)):
        if price == row2[i]:
          row2.pop(i)
          row2.insert(i,0)
          break
        else:
          for i in range(0,len(row3)):
            if price == row3[i]:
              row3.pop(i)
              row3.insert(i,0)
              break
            else:
              for i in range(0,len(row4)):
                if price == row4[i]:
                  row4.pop(i)
                  row4.insert(i,0)
                  break
                else:
                  for i in range(0,len(row5)):
                    if price == row5[i]:
                      row5.pop(i)
                      row5.insert(i,0)
                      break
                    else:
                      for i in range(0,len(row6)):
                        if price == row6[i]:
                          row6.pop(i)
                          row6.insert(i,0)
                          break
                        else:
                          for i in range(0,len(row7)):
                            if price == row7[i]:
                              row7.pop(i)
                              row7.insert(i,0)
                              break
                            else:
                              for i in range(0,len(row8)):
                                if price == row8[i]:
                                  row8.pop(i)
                                  row8.insert(i,0)
                                  break
                                else:
                                  for i in range(0,len(row9)):
                                    if price == row9[i]:
                                      row9.pop(i)
                                      row9.insert(i,0)
                                      break
                                    else:
                                      return "WE COULND'T FIND A SEAT WITH YOUR CRITERIA"
                  
      
    

      

    

    
    

  

main()