list1 = []
list2 = []
list3 = []
n = int(input("number of elements you will type:"))

for i in range(0,n):
  s = int(input("Enter the number:"))

  list1.append(s)
#2 li terkar edenleri aykliyor
for num in range(n):
  if list1[num] == list1[num-1]:
    list2.append(list1[num])
#3 lu tekrar edenleri ayikliyor
for num in range(len(list2)-1):
  if list2[num] != list2[num-1]:
    list3.append(list2[num])
print(list3)