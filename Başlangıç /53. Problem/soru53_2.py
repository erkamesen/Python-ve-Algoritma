"""
'Kullanıcıdan yaşını alıp saniyeye, dakika ve saate çevirerek kullanıcıya gösteren programı tasarlayın.'
"""


yas = float(input("Lütfen yaşınızı giriniz: ")) # 27

saat_yas = yas*360*24 # 233280
dakika_yas = yas*360*24*60 # 13996800
saniye_yas = yas*360*24*60*60 # 839808000
print(f"Şu zamana kadar tam olarak {saat_yas} saat, {dakika_yas} dakika, {saniye_yas} saniye yaşadınız.")

# Şu zamana kadar tam olarak 233280 saat, 13996800 dakika, 839808000 saniye yaşadınız.
