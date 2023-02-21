"""
'Kullanıcının 2 sayı alıp bu sayılar dahil aralarındaki sayılarıda kullanıcıya yan yana olcau şekilde gösteren programı tasarlayın.'
"""


sayi1 = int(input("Başlangıç Sayısı: "))
sayi2 = int(input("Bitiş Sayısı: "))
for i in range(sayi1, sayi2+1): # döngüdeki son sayı sayılmadığı için +1 veriyoruz.
  print(i, end=" ")
