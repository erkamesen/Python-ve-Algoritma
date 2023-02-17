# Soru 6 - Başlangıç

## Soru 6.1

'
set1 = {3,2,4,5,6,7,8} <br>
set2 = {4,12,5,1,6,8} <br>
Verilen 2 tane kümenin birleşimini çıktı olarak gösteren programı tasarlayın.'

Verilenler:
- set1 = {3,2,4,5,6,7,8}
- set2 = {4,12,5,1,6,8}

Adımlar:
- set1 ve set2 nin birleşimini alıp bir değişkene ata.
- değişkeni çıktı olarak ekrana yaz. <br>
End

```
set1 = {3,2,4,5,6,7,8} 
set2 = {4,12,5,1,6,8}
set3 = set1.union(set2)
print(set3)
# {1, 2, 3, 4, 5, 6, 7, 8, 12}
```

```
set1 = {3,2,4,5,6,7,8} 
set2 = {4,12,5,1,6,8}
set3 = set1 | set2
print(set3)
# {1, 2, 3, 4, 5, 6, 7, 8, 12}
```
## Soru 6.2

'
set1 = {5,12,52,0,8} <br>
set2 = {2,5,1,9,8} <br>
set3 = {4,5,6,0,10} <br>
verilen 3 kümenin birleşimini ekrana yazdıran programı tasarla.'

Verilenler:
- set1 = {5,12,52,0,8} 
- set2 = {2,5,1,9,8} 
- set3 = {4,5,6,0,10} 

Adımlar:
1. set1, set2 ve set3 ün birleşimini al ve bir değişkene ata.
2. değişkeni çıktı olarak ekrana yaz.

```
set1 = {5,12,52,0,8} 
set2 = {2,5,1,9,8} 
set3 = {4,5,6,0,10} 
new_set = set1 | set2 | set3
print(new_set)
# {0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 52}
```
