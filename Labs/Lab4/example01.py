list1 = []

n = int(input("number of elements you will type:"))

for i in range(0,n):
  s = float(input("Enter the number:"))

  list1.append(s)

print(f"{max(list1)} is the greatest number you have typed")