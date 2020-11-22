foo = 11
bar = 77
boo = 0


def my_func(foo, bar):
  woo = 31
  print(f"foo {foo} and bar {bar} and and woo {woo} annnd {boo}")


my_func(99,78)

print(foo)
# Methodlarda içeride verdiğin değer dışarıya yansımaz. dışarıda 77 olarak belirledğin woo değeri içeride farklı bir değer alabilir ama dışarıda hala dışarıda verdiğin değerdir.

#print(woo)  da çıkmayacaktır çünki sadece içeride tanımlı dışarıda yazdıramazsın
boo = 21

my_func(99,78)

#Artık boo değeri değişmiş bir şekilde yazdıracaktır
yap = my_func

yap(91,71)
#my_func yerine artık yap yazarak da aynı methodu çağırabiliriz.

# Açıkta bırakmamak için func related şeyleri genellikle son bir func a daha alırız. Genellikle buna main ismini veririz.
