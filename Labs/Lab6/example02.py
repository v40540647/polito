
def Countwords(count):
  numofwords = 0
  unwanteds = ["'","!",",",".","?"]
  for i in count:
    if i == " ":
      continue
    elif i in unwanteds:
      continue
    else:
      numofwords += 1
  return numofwords

def main():
  ayy = input("Enter your sentence bud : ")
  slatt = Countwords(ayy)
  print(slatt)

main()