"""
'bir yönetici çalışanlarına çalıştığı yıllara göre maaşına zam yapıyor. 1 sene ve üstü çalışanlara %10,
2 sene ve üstü çalışanlara %15, 3 sene ve üstü çalışanlara %20, 5 sene ve üstü çalışanlara ise %25 zam yaptığına göre
kullanıcıdan alınan yıl ve maaş bilgisine göre kullanıcıya yeni maaşını ve zam oranını gösteren programı tasarlayın.'
"""


maas = int(input("Lütfen güncel maaşınızı giriniz: "))
yil = float(input("Lütfen kaç yıldır çalıştığınızı giriniz: "))

if yil>1 and yil<2:
  yeni_maas = maas + maas*0.1
  print(f"Yeni Maaşınız:{yeni_maas}, zam oranı: %10")
elif yil>2 and yil<3:
  yeni_maas = maas + maas*0.15
  print(f"Yeni Maaşınız:{yeni_maas}, zam oranı: %15")
elif yil>3 and yil<5:
  yeni_maas = maas + maas*0.2
  print(f"Yeni Maaşınız:{yeni_maas}, zam oranı: %20")
elif yil>5:
  yeni_maas = maas + maas*0.25
  print(f"Yeni Maaşınız:{yeni_maas}, zam oranı: %25")
