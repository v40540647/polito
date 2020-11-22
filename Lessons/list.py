# Gördüğün gibi list2 yi list 1 e eşitlediğimz zaman list2 list 1 in kopyası oluyor. ancak list 2 için birşey değiştirmek istersen list 1 de de aynı değer değişiyor
list1 = [1,2,3,7]
print(list1)

list2 = list1
list2[0] = 9
print (list2)
print(list1)


#ancak buradaki list e : koyduğumuzda içindeki değer değişmez. Ayrı bir liste oluşturulmuş gibi düşünebilirsin.
list3 = list2 [:]
list3[0] = 999
print (list2)
print (list3)

#Another way to create a list
list4 = list("Giovanni")
print(list4)


#Ekleme
list1.append(999)
print(list1)

#Pozisyonunu belirledigin Ekleme
list1.insert(0, 66)
#possible list1.inert(4,input("Enter the element"))
print(list1)

# Checking
if 999 in list1:    # This returns boolean value
  print("JW is here")
#Checking the position
n = list1.index(999)   #Also doable for letters in a word 
print(n)
#Removing
list1.pop(4)   #No 7 anymore  #pop without number (pop()) removes the last 
print(list1)
#Removing without position
list1.append(3)
print(list1)
list1.remove(3)     #Only removes one 3
print(list1)   

#concatenate
newlist = list1 + list4
print(newlist)
#similar to this we can * the list 
jw = [9] * 3
print(jw)

# list intlerden olusuyorsa toplamlarini bulabilirsin
print(sum(list1))

#Sort alfabetik/buyukluk siralamasini yapar
isim = ["adami","Squirello", "bonelli"]
isim.sort()  #Dikkat! buyuk harf her zaman kucuk a dan once gelir
print(isim)
#Dikkat! Sort kelime siralamasi yapamaz!
beratinisimi = ("Berat")
 #beratinisimi.sort()
print(beratinisimi)
#Eger bu islemi ana listeyi degistirmeden yapmak stiyorsan sort yerine sorted kullanmalisin ama bu tek seferliktir
print(sorted(list1))
print(list1)
#Ters sortlamak istiyorsan :
yenilist = [1 , 9 , 77 , 2 , 8]
yenilist.sort(reverse=True)
print(yenilist)

#Baska bir listeyi kopyalamak 
temizlist = list(list1)
print(temizlist)

# =  ile kopyalamak ile list yontemiyle kopyalamak arasindaki fark
listdamn = list1
#eger bu asamadan sonra list1 i degistirirsem listdamn de degisecektir
#ancak list ile birlestirirsem yeni bir liste cacaktir ve list1 degisse de listdamn degismeyecektir


#belirli bir parca alinmak isteniyorsa [:] kullanmalisin
#range gibi sagdaki baslnagici soldaki birisi temsil eder
print(list1[2 : 5]) 

#ayni sekilde iceridekileri degistirmek/eklemek icin de kullanilabilir
foo = list("abcdef")
foo[2:3] = ["xxx","yyy","zzz"] # c yi cikar yerine 3 tane ekle
print(foo)
print(foo.index("zzz")) #artik d e f nin indexleri farkli
#birseyi cikarmadan da araya sıkıştırabiliriz 
foo[1:1] = ["Slatt"]  #eger [] siz slatt yazarsan harfleri teker teker yazar
print(foo)
print(foo.index("zzz"))
#Rangede oldugu gibi bunda da 3. part vardir.
print(foo[0:9:2])   #2 ser 2 ser yazar
#her 2 harfin arasina * eklemek
foo[::2] = ["*"] * 5
print(foo)