"""
'Kullanıcıdan alınan açının sin ve cos değerlerini bulan programı tasarlayın.'
"""


from math import sin, cos

aci = float(input("Lütfen dönüştürmek üzere bir açı giriniz: "))

sin_aci = sin(aci)
cos_aci = cos(aci)
print(f"sin değeri: {sin_aci}\ncos değeri: {cos_aci}")
