"""
'aşağıdaki gibi 5 adet renk ismi saklanan listeden kullanıcıdan alınan renge göre rengin içinde olup olmadığını kontrol eden ve ona göre cevap yazan programı tasarlayın.
renkler = ["siyah", "mavi", "pembe", "kırmızı","yeşil"]'
"""


renkler = ["siyah", "mavi", "pembe", "kırmızı","yeşil"]
renk = input("Lütfen kontrol etmek için bir renk giriniz: ")
if renk in renkler:
  print("Renk listede var")
else:
  print("Renk listede yok")
