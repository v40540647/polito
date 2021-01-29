g = open("output.txt", "w")

a = 0
for line in reversed(open("input.txt", "r").readlines()):
   g.write(line)
   if a < 1:
      g.write("\n")
   a+= 1


### DUZ ###
g = open("input.txt", "r")
j = open("output.txt", "w")
a = 1
for line in g:
  j.write(f"{a}")
  j.write(line)
  a+=1
