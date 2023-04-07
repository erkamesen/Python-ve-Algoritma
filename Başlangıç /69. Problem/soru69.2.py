"""
'kullanıcıdan alınan isimle bir .txt dosyası oluşturup bu dosyanın içine kullanıcıdan alınan 2 adet sayının toplamını yazan programı tasarlayın.'
"""

isim = input("Lütfen isminizi giriniz: "))
with open(isim, "w") as f:
  num1 = input("Lütfen ilk sayıyı giriniz: "))
  num2 = input("Lütfen ikinci sayıyı giriniz: "))
  sonuc = num1 + num2
  f.write(sonuc)
