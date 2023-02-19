"""
'Kullanıcıdan 2 adet sayı ve bir adet operatör(+, -, *, /) alıp operatöre göre 2 sayı arasında işlem yapan programı tasarlayın.'
"""


num1 = int(input("Lütfen ilk sayıyı giriniz: "))
num2 = int(input("Lütfen ikinci sayıyı giriniz: "))
islem = input("Lütfen yapacağınız işlemi giriniz(+, -, *, /): )
if islem == "+":
  print(num1+num2)
elif islem == "-":
  print(num1-num2)
elif islem == "*":
  print(num1*num2)
elif islem == "/":
  print(num1/num2)
