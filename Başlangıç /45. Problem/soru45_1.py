"""
'1 den 30 a kadar sadece tek sayıları gösteren programı tasarlayın.'
"""

for sayi in range(1,31):
  if sayi %2==0:
    continue
  else:
    print(sayi)
