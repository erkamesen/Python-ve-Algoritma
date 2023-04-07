"""
'kullanıcıdan alınan isimle bir .txt dosyası oluşturup bu dosyanın içine kullanıcının yaşını yazan programı tasarlayın.'
"""

isim = input("Lütfen isminizi giriniz: "))
with open(isim, "w") as f:
  age = input("Lütfen yaşınızı giriniz: "))
  f.write(age)
