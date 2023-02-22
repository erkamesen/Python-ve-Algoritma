"""
'Kullanıcıdan miktar ve alınacak yüzde(%) bilgisini alıp miktarın yüzdesini gösteren programı tasarlayın.'
"""

miktar = int(input("Lütfen miktarı giriniz: ")) # 1000
yuzde = int(input("Lütfen yüzde miktarını giriniz: ")) # 20

sonuc = (miktar*yuzde)/100
print(sonuc) # 200
