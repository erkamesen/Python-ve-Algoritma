"""
'kullanıcıdan 3 adet renk alan ve eğer renk aşağıdaki listede yoksa listeye ekleyen programı tasarlayın.
renkler = ["siyah", "mavi", "pembe", "kırmızı","yeşil"]'
"""



renkler = ["siyah", "mavi", "pembe", "kırmızı","yeşil"]
for i in range(3):
  renk = input("Lütfen kontrol etmek için bir renk giriniz: ")
  if renk in renkler:
    print("Renk listede mevcut")
  else:
    renkler.append(renk)
print(renkler)
