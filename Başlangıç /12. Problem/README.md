# Soru 12 - Başlangıç

## Soru 12.1

'Aşağıdaki şekili çıktı olarak veren programı tasarlayın. 
```
* 
** 
*** 
**** 
*****
```
'

Adımlar:
1. 5 adımlı bir for döngüsü oluştur.
2. her adımda adım sayısının bir fazlasıyla "*" karakterini çarpıp ekrana yazdır.
End

```
for i in range(0,5): # 0 1 2 3 4
  print((i+1)*"*")
  
"""
*
**
***
****
*****
"""
```


## Soru 12.2
'Aşağıdaki şekili çıktı olarak veren programı tasarlayın. <br>
```
     *
    **
   ***
 *****
******
```
'

Adımlar:
1. bir değişken oluştur ve değerini 4 ver.
2. 5 adımlı bir for döngüsü oluştur.
3. oluşturulan değişkenle " " karakterini çarpıp adım sayısının bir fazlasının "*" çarpımı ile topla
4. değişkenin değerini bir azalt. <br>
End

```
j = 4
for i in range(5):
    print((" "*j)+(i+1)*"*")
    j -=1
"""
    *
   **
  ***
 ****
*****
"""
```

