"""
'Kullanıcıya tarihi göstermek için evet yada hayır sorusu sorup evet derse bulunduğu tarihi gösteren programı tasarlayın.'
"""


from datetime import datetime

sorgu = input("Bugünün tarihini görmek ister misiniz ? (e/h): ").lower()
if sorgu == "e":
  print(datetime.now()) # datetime.datetime(2023, 2, 22, 16, 2, 47, 225009)
elif sorgu == "h":
  print("Tamam, iyi günleri dilerim !")
else:
  print("Lütfen geçerli bir giriş sağlayınız.")
