char = input("Enter a word")
list1 = []
for word in char:
  if word >= "A" and word <= "Z":
    list1.append(word)
j = ''.join(list1)
print(j)
