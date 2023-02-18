"""
' Kullanıcıdan ad, adres ve telefon bilgisini alıp verilen şablon sözlüğü yeni bilgilerle update eden programı yazın.

bilgi={"ad":"Müşterinin Adı",
       "adres":"Müşterinin Adresi",
       "telefon":"Müşterinin Telefonu"}
     

'
"""

bilgi={"ad":"Müşterinin Adı",
       "adres":"Müşterinin Adresi",
       "telefon":"Müşterinin Telefonu"}
ad = input("Lütfen adınızı giriniz: ")
adres = input("Lütfen adresinizi giriniz: ")
telefon = input("Lütfen telefonunuzu giriniz: ")
bilgi["ad"] = ad
bilgi["adres"] = adres
bilgi["telefon"] = telefon
print(bilgi)
