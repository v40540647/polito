size = int(input("How large do you want ? :"))

for i in range(size):
  print("*" * size)

for z in range(size):
  print(" "* (size-z), "*" * (2*z - 1))
for y in range(size, 0, -1):
  print(" "*(size-y), "*" * (2*y-1))
