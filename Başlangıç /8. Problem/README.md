# Soru 8 - Başlangıç

Soru 8.1

'
set1 = {1,12,2,6,7,8} <br>
set2 = {15,0,1,3,6} <br>
Verilen kümelerden set1 in set2 den farkını bulup sonucu ekrana çıktı olarak veren programı tasarlayın.'

Verilenler:
- set1 = {1,12,2,6,7,8} 
- set2 = {15,0,1,3,6} 

Adımlar:
1. set1 in set2 den farkını bulup bir değişkene ata.
2. sonucu ekrana yaz. <br>
End

```
set1 = {1,12,2,6,7,8} 
set2 = {15,0,1,3,6}
new_set = set1 - set2
print(new_set)
# {8, 2, 12, 7}
```
&
```
set1 = {1,12,2,6,7,8} 
set2 = {15,0,1,3,6}
new_set = set1.diffence(set2)
print(new_set)
# {8, 2, 12, 7}
```

Soru 8.2

'
set1 = {12,2,0,3,8} <br>
set2 = {15,10,12,3,6} <br>
Verilen kümelerin simetrik farkını bulup ekrana yazan programı tasarlayın.'

Verilenler:
- set1 = {12,2,0,3,8}
- set2 = {15,10,12,3,6} 

Adımlar:
1. set1 ve set2 nin simetrik farkını bir değişkene ata.
2. sonucu ekrana yaz <br>
End

```
set1 = {12,2,0,3,8}
set2 = {15,10,12,3,6} 
new_set = set1 ^ set2
print(new_set)
# {0, 2, 6, 8, 10, 15}
```
