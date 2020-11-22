hey = input("Word")
listf = []
for i in hey:
  listf.append(i)
listf.sort(key=str)
b = ""
for a in range(0,len(listf)):
  b+=listf[a]
print(b)
