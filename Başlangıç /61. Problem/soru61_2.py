"""
'Kullanıcıdan alınan byte ı GB ye çeviren programı tasarlayın. 1 GB = 1.073.741.824 Bayt.'
"""


byte = int(input("Lütfen dönüştürmek istedğiniz byte miktarını giriniz: ")) # 1073741824000

gb = byte / 1073741824

print(f"{byte} byte = {gb} GB")
# 1073741824000 byte = 1000.0 GB
