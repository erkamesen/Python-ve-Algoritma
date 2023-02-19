"""
'kullanıcıdan 2 adet sayı alıp parametre olarak 2 sayı alan ve bu sayıların büyük olanını döndüren fonksiyonu tasarlayın.'
"""



def min_sayi(n1, n2):
  if n1 < n2:
    return n1
  else:
    return n2

sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
print(min_sayi(n1=sayi1, n2=sayi2))
