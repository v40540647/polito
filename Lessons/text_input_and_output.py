#### kelimeyi listeli ayirmak ###
infile = 'I bring the heat like Laflame'
#for line in infile:
#  line = infile.rsplit()
#print(line)

#### Or can be done like this ###
#print(str.split(infile))

### you can set the max amount of slitting ###
#print(infile.split(" ",maxsplit=1))

### Maxsplit = 0 means just make a list ###
### Maxspluit negative means split() ###

### rsplit means splitting starting from the right ###
#print(infile.rsplit(maxsplit = 1))
#print(infile)

### This splits every letter ###
#print(list(infile))

### Bir harf/birsey gordugun anda splitleme (deletes the numbr you want to findout)###
#print(infile.split("t"))


#for line in infile:
#  print(line)

## Normalde disarida yazilmis her textin sonunda bir alt satira gecmek inin \n ifadesi bulunmaktadir. eger ki disaridan bir dosya calistirilamk istenirse (Ornegin print(f"555{n}444") yazdigimiz zaman n line inin sonunda \n oldugu icin yadigi zaman 555 n #atlsatirda da 444 yazicaktir )]

##bunu engellemek icin rstrip denilen bir eleman var. bu eleman sayasinde \nlerden kurlulabiliriz. Bu eleman ayrica ikili veya uclu    bosluklari da silmekte. rstrip in icine kouylan seyleri de sagdan baslayarak silmeye baslar. meslea rstrip(".")komutu  "Fooo ...../..." metninde / e kadar butun noktalari siler. eger ikisini birden silmek istersen rstrip(/.) yazamn lazim)

##strip = hem sagdan hem soldan siler
##lstrip = soldan
##rstrip = sagdan


### Bu kodu pycharmda pycharm dosyasinin icine slatt.x adli dosya yazdiktan sonra yaptim. basically bu kodun yapigi sey iceridekileri okuyup line basina ??? sonuna @@@ koymak ###
#Filename = "slatt.x"

#def main():
  #  file =open(Filename , "r")
    #for i in file:
      #  i = i.rstrip()
      #  print(f"??? {i} @@@")