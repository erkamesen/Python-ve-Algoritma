"""
'Kullanıcıdan 2 sayı alıp bir değişkene atayan ve ardından bu değişkenlerin değerini hazfıza değeri yardımı ile birbiri
arasında değiştiren programı tasarlayın.'
"""


a = int(input("Lütfen ilk sayıyı giriniz: ")) # 3
b = int(input("Lütfen ikinci sayıyı gitiniz: ")) # 5
Print(f"Birinci sayı: {a}\nİkinci sayı: {b}")

c = a # c = 3
a = b # a = 5
b = c # b = 3 

Print(f"Birinci sayı: {b}\nİkinci sayı: {a}")
