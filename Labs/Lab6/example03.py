def find(ysl, thugger):
  slatt =False
  if thugger in ysl:
    slatt = True
  return slatt

def main():
  boi = input("Enter the word bud : ")
  mat = input("Enter subsequence dude : ")
  ayy = find(boi , mat)
  print(ayy)

main()

