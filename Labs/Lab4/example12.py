number = int(input("Gimme the number! : "))
for i in range(0,number+1):
  if i >= 2:
   for a in range(2 , i):
     if (i % a == 0):
      break
   else:
     print(i)

  
