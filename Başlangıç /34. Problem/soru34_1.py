"""
'Kullanıcıdan 5 adet renk alıp listede saklayan ve ardından listenin son itemini atıp listeyi kullanıcıya gösteren programı tasarlayın.'
"""


renkler = []
for i in range(5):
  renkler.append(input("Lütfen bir renk giriniz: "))
renkler.pop()
print(renkler)
