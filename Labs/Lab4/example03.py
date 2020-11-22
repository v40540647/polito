list1 = []
list2 = []
a = 0
n = int(input("number of elements you will type:"))

for i in range(0,n):
  s = float(input("Enter the number:"))

  list1.append(s)

for i in list1:
  a += i
  list2.append(a)
  print(a)

print(list2)

  