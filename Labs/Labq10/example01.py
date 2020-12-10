eyy = open("inputfile.txt" , 'r')
slatt = open("outputfile.txt" , 'w')
a = 0
for line in eyy:
  slatt.write(f"/**\ {eyy.readline()}")
eyy.close()
slatt.close()
