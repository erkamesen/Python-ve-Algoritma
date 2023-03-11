"""
'Kullanıcıdan alınan kare alanı bilgisine göre kullanıcıya karenin çevresini çıktı olarak veren fonksiyonla programı tasarlayın.A=a²P=4a'
"""



def alandan_cevreye(alan):
  kenar_uzunlugu = alan**0.5
  cevre = kenar_uzunlugu *4
  return cevre
  
alan = int(input("Lütfen karenin alanını giriniz: ")) # 9

cevre = alandan_cevreye(alan)
print("Çevre:",cevre) # Çevre: 12.0
