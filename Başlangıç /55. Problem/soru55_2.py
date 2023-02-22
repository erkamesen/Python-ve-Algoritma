"""
'Kullanıcıya saati göstermek için evet yada hayır sorusu sorup evet derse güncel saati gösteren programı tasarlayın.'
"""


from datetime import datetime

sorgu = input("Güncel saati görmek ister misiniz ? (e/h): ").lower()
if sorgu == "e":
  saat = datetime.now().hour
  dakika = datetime.now().minute
  print(f"{saat}:{dakika}") # 16:02
elif sorgu == "h":
  print("Tamam, iyi günleri dilerim !")
else:
  print("Lütfen geçerli bir giriş sağlayınız.")
