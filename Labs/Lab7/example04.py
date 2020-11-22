def main ():
  list1 = ["a" ,"a","a", "b" , "c" , "d" , "s"]
  list2 = ["a" , "b","c"  , "d" ,"s" ]
  equal(list1,list2)

def equal(list1 , list2):
  i = 0
  a = 0

  while i < len(list1):
   if list1[i] in list2:
     None
   else :
     a = a + 1
     print("They are not the same")
     break
   i+=1
  while i < len(list2):
   if list2[i] in list1:
     None
   else :
     a = a +1
     print("They are not the same")
       
     break
   i+=1
  if a == 0:
    s = print("They are the same")
  else:
    s = "Slatt"
  return s
main()