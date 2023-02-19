"""
'Kullanıcıdan bir gün bilgisi alıp hafta içi mi hafta sonu mu olduğunu ekrana çıktı olarak yazan programı tasarlayın.
Eğer 7 günden farklı bir şey yazarsa program hata versin.'
"""


hafta_ici = ["PAZARTESİ","SALI","ÇARŞAMBA","PERŞEMBE","CUMA"]
hafta_sonu = ["CUMARTESİ","PAZAR"]

gun = input("Lütfen bulunduğunuz günü girin: ").upper()

if gun in hafta_ici:
  print("Bugün hafta içi")
elif gun in hafta_sonu:
  print("Bugün hafta sonu")
else:
  print("Bu bir gün değil")
