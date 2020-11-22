word = input("Enter a word")
position = 1
vowels = ['a', 'e', 'i', 'o', 'u']
for i in (word.lower()):
  if i in vowels:
    print(i , position)
  position += 1