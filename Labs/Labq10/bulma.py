g = open("input.txt", "r")
j = open("output.txt", "r")
pp = input("Enter the word you want to search :")
for a in g:
   if pp in a:
      print(f"the Word exist on input file and its line is : {a}")

for p in j:
   if pp in p:

      print(f"the Word exist on output file and its line is : {pp}")