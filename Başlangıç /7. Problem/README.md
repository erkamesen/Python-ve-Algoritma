# Soru 7 - Başlangıç

## Soru 7.1

'
set1 = {5,2,4,6,7,1} <br>
set2 = {5,3,11} <br>
Verilen 2 kümenin kesişimini çıktı olarak gösteren programı tasarlayın.'

Verilenler:
- set1 = {5,2,4,6,7,1} 
- set2 = {5,3,11} 

Adımlar:
- set1 ve set2 nin kesişimini alıp bir dğeişkene ata
- değişkeni ekrana yaz <br>
End

```
set1 = {5,2,4,6,7,1} 
set2 = {5,3,11} 
set3 = set1.intersection(set2)
print(set3)
# 5
```

```
set1 = {5,2,4,6,7,1} 
set2 = {5,3,11} 
set3 = set1 & set2
print(set3)
# {5}
```

## Soru 7.2

'set1 = {5,2,4,6,7,1} <br>
set2 = {5,3,11} <br>
set3 = {4,5,12,2,1,0} <br>
Verilen 3 kümenin kesişimini çıktı olarak gösteren programı tasarlayın.'

Verilenler:
- set1 = {5,2,4,6,7,1}
- set2 = {5,3,11}
- set3 = {4,5,12,2,1,0}

Adımlar:
- set1, set2 ve set3 ün kesişimini alıp bir değişkene ata.
- değişkeni çıktı olarak ekrana yaz
End

```
set1 = {5,2,4,6,7,1}
set2 = {5,3,11,1}
set3 = {4,5,12,2,1,0}
new_set = set1 & set2 & set3
# {5, 1}
```

