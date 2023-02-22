"""
'Kullanıcıdan aldığı 5 sayının faktoriyelini hesaplayan fonksiyonla, programı tasarlayın.'
"""


def fakt(sayi):
  fak = 1
  for i in range(1, sayi+1):
    fak *= i
  return fak
 
for i in range(5):
  sayi = int(input("Lütfen faktoriyeli alınacak sayıyı giriniz: ")) # 4 5 10 15 20
  print(fakt(sayi=sayi))
  
"""
Lütfen faktoriyeli alınacak sayıyı giriniz: 4
24
Lütfen faktoriyeli alınacak sayıyı giriniz: 5
120
Lütfen faktoriyeli alınacak sayıyı giriniz: 10
3628800
Lütfen faktoriyeli alınacak sayıyı giriniz: 15
1307674368000
Lütfen faktoriyeli alınacak sayıyı giriniz: 20
2432902008176640000
"""
