
def CountWowels(word):
  wowelnum = 0
  wowels= ["a","e","i","u","o"]
  for i in word:
    if i in wowels:
      wowelnum +=  1

  return wowelnum

def  main ():
  kelime = input("Enter String bud : ")
  aha = CountWowels(kelime)
  print(aha)

main()



