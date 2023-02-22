"""
'Kullanıcıdan alınan cümleyi ters çevirip başına ve sonuna çift tırnak ekleyip kullanıcıya gösteren programı tasarlayın.'
"""


cumle = input("Lütfen çevirme kiçin bir cümle giriniz: ") # Python yüksek seviye ve nesne yöenlimli bir dildir.
ters_cumle = cumle[::-1]
ters_cumle = '"'+ters_cumle+'"'
print(ters_cumle) 

# ".ridlid rib ilmilneöy ensen ev eyives kesküy nohtyP"
