"""
'Kullanıcıdan alınan 2 tarih arasında kaç saat olduğunu hesaplayıp kullanıcıya gösteren programı tasarlayın.'
"""


from datetime.datetime import strptime()

tarih1 = input("Lütfen ilk tarihi giriniz: ") # 25/10/1994
tarih2 = input("Lütfen ikinci tarihi giriniz: ") # 25/10/2004

date_format = "%d/&m/%Y"
t1 = strptime(tarih1, date_format)
t2 = strptime(tarih2, date_format)
gun_farki = (t2-t1).days # 3653
saat_farki = gun_farki * 24 # 87672
print(saat_farki)
