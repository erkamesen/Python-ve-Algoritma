"""
'Kullanıcıdan alınan GB yi byte a çeviren programı tasarlayın. 1 GB = 1.073.741.824 Bayt.'
"""


gb = int(input("Lütfen dönüştürmek istedğiniz GB yi giriniz: ")) # 15.5

byte = gb * 1073741824

print(f"{gb} GB = {bytes} byte")
# 15.5 GB = 16106127360 byte
