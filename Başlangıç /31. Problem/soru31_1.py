"""
'Kullanıcıdan alınan notun aşağıdaki verilenlere göre karşılığını kullanıcıya gösteren programı tasarlayın.
eğer 89 dan büyükse "A+"
eğer 79 dan büyükse "A"
eğer 69 dan büyükse "B"
eğer 59 dan büyükse "C"
eğer 49 den büyükse "D"
Eğer hiç biri değilse "F"'
"""

ders_notu = int(input("Lütfen notunuzu giriniz: "))
if ders_notu >= 90:
  print("A+")
elif ders_notu >= 80 and ders_notu <= 90:
  print("A")
elif ders_notu >= 70 and ders_notu <= 80:
  print("B")
elif ders_notu >= 60 and ders_notu <= 70:
  print("C")
elif ders_notu >= 50 and ders_notu <= 60:
  print("D")
else:
  print("F")
