"""
'Kullanıcıdan alınan bilgilere göre karenin alanını ve çevresini bulan fonksiyonları ve programı tasarlayın.A=a²P=4a'
"""

def alan_bul(kenar):
  sonuc = kenar**2
  return sonuc
  
def cevre_bul(kenar):
  sonuc = kenar*4
  return sonuc
  
kenar_uzunlugu = int(input("Lütfen bir kenar uzunluğunu giriniz: ")) # 5

print("Alan:",alan_bul(kenar_uzunlugu)) # 25
print("Çevre:",cevre_bul(kenar_uzunlugu)) # 20
