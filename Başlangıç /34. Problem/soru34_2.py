"""
'Kullanıcıdan 5 adet renk alıp listede saklayan ve ardından listenin ilk itemini atıp listeyi kullanıcıya gösteren programı tasarlayın.'
"""



renkler = []
for i in range(5):
  renkler.append(input("Lütfen bir renk giriniz: "))
ilk_renk = renkler[0]
renkler.remove(ilk_renk)
print(renkler)
