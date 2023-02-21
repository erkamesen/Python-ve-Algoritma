"""
'kullanıcıdan alınan 10 adet sayı ile aşağıdaki gibi bir tablo oluşturan programı tasarlayın.

Sayı  Karesi  Küpü  Karesi+Küpü
1     1       1       2
2     4       8       12
..    ..      ..      ..
..    ..      ..
..    ..
..

'
"""


print("Sayı\tKaresi\tKüpü\tKaresi+küpü")
for i in range(10):
  sayi = int(input("Lütfen işlem yapılacak sayıyı giriniz: "))
  karesi = sayi**2
  kupu = sayi**3
  toplam = karesi + kupu
  print(f"{sayi}\t\t{karesi}\t\t{kupu}\t\t{toplam}")
  
"""
Sayı	  Karesi	  Küpü	  Karesi+küpü
Lütfen işlem yapılacak sayıyı giriniz: 1
1		1		1		2
Lütfen işlem yapılacak sayıyı giriniz: 2
2		4		8		12
Lütfen işlem yapılacak sayıyı giriniz: 3
3		9		27		36
Lütfen işlem yapılacak sayıyı giriniz: 4
4		16		64		80
Lütfen işlem yapılacak sayıyı giriniz: 5
5		25		125		150
Lütfen işlem yapılacak sayıyı giriniz: 6
6		36		216		252
Lütfen işlem yapılacak sayıyı giriniz: 7
7		49		343		392
Lütfen işlem yapılacak sayıyı giriniz: 8
8		64		512		576
Lütfen işlem yapılacak sayıyı giriniz: 9
9		81		729		810
Lütfen işlem yapılacak sayıyı giriniz: 10
10		100		1000		1100
"""
