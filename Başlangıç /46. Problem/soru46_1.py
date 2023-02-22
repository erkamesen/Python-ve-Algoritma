"""
'Kullanıcıdan 5 adet not alıp bunları arrayde saklayan, ardından kullanıcının ismini de alıp, notların ortlaması hesaplayan ve notlarla sırasıyla aşağıdaki tabloyu dolduran programı tasarlayın.

Merhaba {kullanıcı adı}
Not Ortalaman: {notların ortalaması}
Tüm Notlar:
İngilizce: {not 1}
Matematik: {not 2}
Fizik: {not 3}
Türkçe: {not 4}
Kimya: {not 5}

"""

from array import array

a = array("i", [])

isim = input("Lütfen isminizi giriniz: ") # Erkam
toplam = 0
for i in range(5):
  ders_notu = int(input("Lütfen notunuzu giriniz: ")) # 50 80 80 60 70
  a.append(ders_notu)
  toplam += ders_notu
ortalama = toplam/5  
print(f"Merhaba {isim}\nNot Ortalaman: {ortalama}\nTüm Notlar:\nİngilizce: {a[0]}\nMatematik: {a[1]}\nFizik: {a[2]}\nTürkçe: {a[3]}\nKimya: {a[4]}")

"""
Merhaba Erkam
Not Ortalaman: 68.0
Tüm Notlar:
İngilizce: 50
Matematik: 80
Fizik: 80
Türkçe: 60
Kimya: 70
"""
