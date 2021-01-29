number = int(input("Gimme the number! : "))
j = 0
for i in range(2,number):
  if (number % i) == 0:
    print("this is not a prime number")
    j = 1
    break
if j == 0:
  print(f"{number} is a prime number")
  
   

  
