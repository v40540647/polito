word = input("Enter a word")
vowels = ['a', 'e', 'i', 'o', 'u']
for x in (word.lower()):
  if x in vowels:
   word = word.replace(x, "_")
print(word)