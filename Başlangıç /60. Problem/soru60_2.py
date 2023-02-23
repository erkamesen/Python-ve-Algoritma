"""
'Aşağıda verilen sözlüğün value larını alt alta yazdıran programı tasarlayın.

sozluk = {1:"bir", 2:"iki", 3:"üç", 4:"dört", 5:"beş", 6:"altı", 7:"yedi", 8:"sekiz", 9:"dokuz", 10:"on"}'
"""



sozluk = {1:"bir",
                  2:"iki",
                  3:"üç",
                  4:"dört",
                  5:"beş",
                  6:"altı",
                  7:"yedi",
                  8:"sekiz",
                  9:"dokuz",
                  10:"on"
                  }
for i in range(1, len(sozluk)+1):
  sayi = sozluk[i]
  print(sayi)
"""
bir
iki
üç
dört
beş
altı
yedi
sekiz
dokuz
on
"""
