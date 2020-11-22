list1 = []
even = 0
odd = 0
n = int(input("number of elements you will type:"))

for i in range(0,n):
  s = float(input("Enter the number:"))

  list1.append(s)

for i in list1:
  if i%2 == 0:
    even = even+1
  else:
    odd = odd + 1

print(list1)
print(f"Number of odd numbers is {odd}")
print(f"Number of even numbers is {even}")

