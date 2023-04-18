"""
'Kullanıcıdan alınan metinin içindeki harf veya rakamların sayısını sözlük yardımı ile kullanıcıya gösteren programı tasarlayın.'
"""


sozluk = dict()

giris = input("Lütfen bir metin giriniz:").lower().strip() #Erkam Esen

for i in giris:
    if i != "":
        sozluk[i] = sozluk.get(i, 0) + 1
print(sozluk)

# {'e': 3, 'r': 1, 'k': 1, 'a': 1, 'm': 1, ' ': 1, 's': 1, 'n': 1}
