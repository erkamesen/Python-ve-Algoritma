"""
'Kullanıcıdan alınan 2 kenar ile dik üçgenin uzunluğunu bulan programı tasarlayın.'
"""



# h² = b² + c² => h = (b**2+c**2)**0.5
b = float(input("Lütfen bir kenarı giriniz: "))
c = float(input("Lütfen bir kenarı giriniz: "))
h = (b**2+c**2)**0.5
print(h)
