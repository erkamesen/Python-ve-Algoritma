"""
'Kullanıcıdan aldığı sayının faktoriyelini hesaplayan programı tasarlayın.'
"""

sayi = int(input("Lütfen faktoriyeli alınacak sayıyı giriniz: ")) # 5

fak = 1
for i in range(1, sayi+1):
  fak *= i
  
print(f"{sayi} Sayısının Faktoriyeli: {fak}")
# 5 Sayısının Faktoriyeli: 120
