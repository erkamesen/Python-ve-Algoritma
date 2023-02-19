"""
'Kullanıcıdan notunu alıp eğer not 50 den düşükse "Kaldın", fazla ise "Geçtin" yazan programı tasarlayın.'
"""

not = int(input("Lütfen notunuzu giriniz: "))
if not >= 50:
  print("Geçtin")
else:
  print("Kaldın")
