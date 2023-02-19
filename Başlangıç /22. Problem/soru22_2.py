"""
'kullanınıcın girdiği harfin sesli mi sessiz mi olduğunu söyleyen ayrıca eğer kullanıcı
rakam girerse rakam olduğunu ve 1 haneden fazla girerse hata döndüren programı tasarlayın.'
"""


sesli_harfler = ["a","e","ı","i","o","ö","u","ü"]
rakamlar = ["0","1","2","3","4","5","6","7","8","9"]
giris = input("Lütfen bir harf giriniz")
if len(giris) == 1:
  if giris in sesli_harfler:
    print(f"{giris} harfi sesli bir harftir.")
  elif giris in rakamlar:
    print("Bu bir rakamdır.")
  else:
    print(f"{giris} harfi sessiz bir harftir.")
 else:
  print("Lütfen sadece 1 karakter giriniz.")
