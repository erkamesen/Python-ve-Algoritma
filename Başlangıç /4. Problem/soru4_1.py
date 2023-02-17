"""
 Kullanıcıdan yaş bilgisini alıp 18 yaşında veya daha büyükse "Oy kullanabilirsiniz!",
 eğer küçükse 18 e kalan seneyi hesaplayıp "Oy kullanamazsınız, lütfen sene bekleyiniz." çıktısı veren programı tasarlayın.
"""

yas = int(input("Lütfen yaşınızı giriniz: "))
if yas >= 18:
  print("Oy kullanabilirsiniz!")
else:
  fark = 18 - yas
  print(f"Oy kullanamazsınız, lütfen {fark} sene bekleyiniz.")
