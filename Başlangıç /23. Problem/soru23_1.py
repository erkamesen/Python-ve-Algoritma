"""
'Kullanıcıdan bir gün bilgisi alıp eğer gün cumartesi yada pazar ise ekrana "Bugün tatil!" yazan programı tasarlayın.'
"""

gun = input("Lütfen bulunduğunuz günü girin: ").lower()
if gun == "cumartesi" or gun == "pazar":
  print("Bugün tatil!")
else:
 print("Haydi işe!")
