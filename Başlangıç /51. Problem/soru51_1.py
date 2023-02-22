"""
'Kullanıcıdan alınan 2 tarih arasında kaç gün olduğunu hesaplayıp kullanıcıya gösteren programı tasarlayın.'
"""


from datetime.datetime import strptime()

tarih1 = input("Lütfen ilk tarihi giriniz: ")
tarih2 = input("Lütfen ikinci tarihi giriniz: ")

date_format = "%d/&m/%Y"
t1 = strptime(tarih1, date_format) # 25/10/1994
t2 = strptime(tarih2, date_format) # 25/10/2004
gun_farki = (t2-t1).days # 3653
print(gun_farki) 
