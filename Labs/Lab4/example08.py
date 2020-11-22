word = input("enter a word")
long = 0
for i in word:
  if i == " ":
    long = long
  else:
    long = long + 1


print(long)