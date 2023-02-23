"""
'kullanıcıdan 5 isim ve notlarını alan ve sözlük biçiminde kullanıcıya gösteren programı tasarlayın.'
"""


sozluk = {}

for i in range(5):
  isim = input("Lütfen isminizi giriniz: ") # erkam ensar enes onur ulaş
  _not = int(input("Lütfen notunuzu giriniz: ")) # 100 21 95 60 43
  sozluk[isim] = _not
print(sozluk)
# {'erkam': 100, 'ensar': 21, 'enes': 95, 'onur': 60, 'ulaş': 43}
