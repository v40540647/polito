r_old = int(input("input ; "))
a = 32310901
b = 1729
m = 2**24
run = 0
for i in range(0,100):
  r_new = (a*r_old + b)%m
  r_old = r_new
  print(r_new)