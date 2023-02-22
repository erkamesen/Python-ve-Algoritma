"""
'Kullanıcıdan alınan onluk sayı sistemindeki(decimal) sayıyı ikili sayı sistemine(binary) çeviren programı tasarlayınız.'
"""


def DecimalToBinary(num):
        if num >= 1:
            DecimalToBinary(num // 2)
        print(num % 2, end="")
sayi = int(input("Lütfen çevrilecek sayıyı giriniz: ")) # 15
DecimalToBinary(15) # 01111
