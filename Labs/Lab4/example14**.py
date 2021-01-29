from random import randint

n = randint(10,100)
turn = randint(0,1)
smartdumb = randint(0,1)
while n > 1:
    ####HUMANSTURN####
  if turn == 1:
    print("HUMANS TURN")
    size =int( input("Extract the number of marbles : "))
    if size > (n/2) or size < 0:
      size = int(input("Enter a valid number"))
    n = n - size
    turn + 1
    if n == 1:
      print("HUMAN LOST , DUMB HUMAN!") 

      ####COMPUTERSTURN####
  if turn == 0:
    print("COMPUTERS TURN")
    if smartdumb == 0:
      numb = randint(1,(n/2))
      n = n - numb
    elif smartdumb == 1:
      if n > 64:
        n = n - 31
      elif n > 32


