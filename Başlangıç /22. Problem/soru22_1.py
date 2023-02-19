"""
'kullanınıcın girdiği harfin sesli mi sessiz mi olduğunu söyleren programı tasarlayın.'
"""

sesli_harfler = ["a","e","ı","i","o","ö","u","ü"]
harf = input("Lütfen bir harf giriniz")
if harf in sesli_harfler:
  print(f"{harf} harfi sesli bir harftir.")
else:
  print(f"{harf} harfi sessiz bir harftir.")
