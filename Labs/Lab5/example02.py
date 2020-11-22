trials = 1
while trials <= 3:
  password = input("Enter the PIN! : ")
  if password != "1234":
    print("Your PIN is incorrect")
    trials = trials + 1
    continue
  else:
    print(f"Sucessfull login! Number of trials : {trials}")
    break
else:
  print("Your card has been blocked")


    