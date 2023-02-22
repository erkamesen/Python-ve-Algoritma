"""
'Kullanıcıdan 2 sayı alıp bir değişkene atayan ve ardından bu değişkenlerin değerini hazıfa değeri olmadan birbiri ile değiştiren programı tasarlayın.'
"""


a = int(input("Lütfen ilk sayıyı giriniz: ")) # 6
b = int(input("Lütfen ikinci sayıyı gitiniz: ")) # 7
Print(f"Birinci sayı: {a}\nİkinci sayı: {b}")

a, b = b, a

Print(f"Birinci sayı: {b}\nİkinci sayı: {a}")
