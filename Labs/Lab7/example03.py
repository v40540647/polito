

def main ():
  list1 = ["a" , "b" , "c" , "d" , "s"]
  list2 = ["a" , "b" , "c" , "d","f" , "d"]
  equal(list1,list2)

def equal(list1 , list2):
  i = 0
  if len(list1)<len(list2):

   while i < len(list1):
     if list1[i] == list2[i]:
       print(f"The {i} th element is the same")
     else :
       print("They are not the same")
       break
     i+=1
  else:
    while i < len(list2):
     if list1[i] == list2[i]:
       print(f"The {i} th element is the same")
     else :
       print("They are not the same")
       break
     i+=1
  
main()
