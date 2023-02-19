"""
'Kullanıcıya öğrenci olup olmadığını sorup eğer öğretmense alttaki not listesini gösteren eğer öğrenciyse "Not sistemimize hoşgeldiniz" yazan programı tasarlayın.
not_listesi = [("ahmet", 44), ("ali", 20), ("erkam", 100)]'
"""

meslek = input("Lütfen mesleğinizi giriniz: ").lower()
if meslek == "öğretmen":
  for not in not_listesi:
    print(not, end=" ")
else:
  print("Not sistemimize hoşgeldiniz")
