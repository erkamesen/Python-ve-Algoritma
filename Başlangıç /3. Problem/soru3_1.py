"""
Kullanıcıdan "isim" ve "yaş" bilgisi alıp ekrana alttaki formatta gösterecek programı yazın.

 # Merhaba benim adım Erkam ve 27 yaşındayım.
 """
 
 
ad = input("Adınız: ")
yas = input("Yaşınız: ")
print(f"Merhaba benim adım {ad} ve {yas} yaşındayım.")
&
print("Merhaba benim adım {} ve {} yaşındayım.".format(ad, yas))
