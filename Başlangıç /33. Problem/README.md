# Soru 33 - Başlangıç



## Soru 33.1

'aşağıdaki gibi 5 adet renk ismi saklanan listeden kullanıcıdan alınan renge göre rengin içinde olup olmadığını kontrol eden ve ona göre cevap yazan programı tasarlayın. <br>
renkler = ["siyah", "mavi", "pembe", "kırmızı","yeşil"]'


Adımlar:
1. listeyi oluştur
2. Kullanıcıdan bir renk al ve bir değişkene ata.
3. eğer renk listede varsa "Renk listede var" çıktısını ekrana ver.
4. eğer yoksa "Renk listede yok" çıktısını ekrana ver. <br>
End

```
renkler = ["siyah", "mavi", "pembe", "kırmızı","yeşil"]
renk = input("Lütfen kontrol etmek için bir renk giriniz: ")
if renk in renkler:
  print("Renk listede var")
else:
  print("Renk listede yok")
```

## Soru 33.2

'kullanıcıdan 3 adet renk alan ve eğer renk aşağıdaki listede yoksa listeye ekleyen programı tasarlayın. <br>
renkler = ["siyah", "mavi", "pembe", "kırmızı","yeşil"]'

Adımlar:
1. listeyi oluştur.
2. 3 adımlı bir for döngüsü başlat
3. Kullanıcıdan her adımda bir renk al.
4. eğer renk listede varsa "Renk zaten mevcut" çıktısı ver.
5. eğer yoksa rengi listeye ekle.
6. listeyi ekrana yaz. <br>
End


renkler = ["siyah", "mavi", "pembe", "kırmızı","yeşil"]
for i in range(3):
  renk = input("Lütfen kontrol etmek için bir renk giriniz: ")
  if renk in renkler:
    print("Renk listede mevcut")
  else:
    renkler.append(renk)
print(renkler)
```
