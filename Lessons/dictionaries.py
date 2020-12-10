tahta = {'7': ' ' , '8': ' ' , '9': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' ' }
#{}ile acilir. ilk element key ikinci element keyin karislik geldigi degerdir.
print(tahta['7'])
# [] ile cagirilir

# eger ki key yok ise normalde hata atar. eger keyin olmamasi durumunu goze aliyorsaniz try except KeyError yaparak calistirin. bu hatayi almamanin bir yolu daha var o da get methodu

#dictionaryname.get(key , key bulunmazsa yazilacak yazi
print(tahta.get("slatt","unknown"))

# dumduz dictionayr adi ve [] ile hem yeni key + element hem de existingi degistirmek mumkun

tahta["Slatt"] = "eyyyy"
print(tahta["Slatt"])

# del tahta["Slatt"]   1 . yol

# tahta.pop("Slatt")   2 . yol

# Saydirma
for key in tahta:
  print(tahta[key])

#keyle birlikte Saydirma
for key,word in tahta.items():
  print(f"{key} : {word}")

#ayni sekilde .key keyleri .values degerleri .items ikisini birlikte verir

