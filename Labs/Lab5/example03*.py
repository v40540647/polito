num = int(input("Gimme the number: "))
num_of_twos = 0
num_of_threes = 0
num_of_fives = 0
num_of_sevens = 0
num_of_elevens = 0
while num > 1:

 for i in range(99):
  if num%2 == 0:
    num = num/2
    num_of_twos = num_of_twos + 1
  else:
    if num%3 == 0:
      num/3
      num_of_threes = num_of_threes +1
    else:
        if num%5 == 0:
          num/5
          num_of_fives = num_of_fives +1
        else:
          if num%7 == 0:
            num/7
            num_of_sevens = num_of_sevens+1
          else:
            if num%11 == 0:
              num/11
              num_of_elevens = num_of_elevens +1
            else:
              print("birader o kadar da aptal bi sayi girme yani")
              break
else:
  print("bitti")

print(num_of_twos)
print(num_of_threes)
print(num_of_fives)
print(num_of_sevens)
print(num_of_elevens)
