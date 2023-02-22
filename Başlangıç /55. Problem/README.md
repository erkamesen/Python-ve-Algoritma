# Soru 55 - Başlangıç

## Soru 55.1

'Kullanıcıya tarihi göstermek için evet yada hayır sorusu sorup evet derse bulunduğu tarihi gösteren programı tasarlayın.'

Adımlar:
1. datetime modülünden datetime ı import et.
2. kullanıcıya tarihi görmek isteyip istemediğini sor.
3. eğer evet diyorsa güncel tarihi kullanıcıya göster.
4. eğer hayır diyorsa tamam iyi günler dilerim çıktısını ekrana ver. <br>
End


```
from datetime import datetime

sorgu = input("Bugünün tarihini görmek ister misiniz ? (e/h): ").lower()
if sorgu == "e":
  print(datetime.now()) # datetime.datetime(2023, 2, 22, 16, 2, 47, 225009)
elif sorgu == "h":
  print("Tamam, iyi günleri dilerim !")
else:
  print("Lütfen geçerli bir giriş sağlayınız.")
```
## Soru 55.1

'Kullanıcıya saati göstermek için evet yada hayır sorusu sorup evet derse güncel saati gösteren programı tasarlayın.'

Adımlar:
1. datetime modülünden datetime ı import et.
2. kullanıcıya saati görmek isteyip istemediğini sor.
3. eğer evet diyorsa:
- güncel saati al ve bir değişkene ata.
- güncel dakikayı al ve bir dğeişkene ata.
- "saat:dakika" formatında kullanıcıya göster.
4. eğer hayır diyorsa tamam iyi günler dilerim çıktısını ekrana ver. <br>
End


```
from datetime import datetime

sorgu = input("Bugünün tarihini görmek ister misiniz ? (e/h): ").lower()
if sorgu == "e":
  saat = datetime.now().hour
  dakika = datetime.now().minute
  print(f"{saat}:{dakika}") # 16:02
elif sorgu == "h":
  print("Tamam, iyi günleri dilerim !")
else:
  print("Lütfen geçerli bir giriş sağlayınız.")
```
