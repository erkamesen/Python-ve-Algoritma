# Selection Sort

En basit sorting algoritmalarından biridir.

![insertion-sort](https://raw.githubusercontent.com/Kodluyoruz/taskforce/main/veri-yapilari-algoritmalar/insertion-sort/figures/insertion-sort.png)

Verilen örüntüye ait en küçük elemanı buluyor ve en baştaki sayı ile yer değiştiriyor. 
Peki ya devamı? İkinci en küçük elemanı buluyor ve 2. sıra ile değiştiriyor. Baktın ki 2.sıradaki eleman en küçük hiç dokunma!!!.
Hemen 3. sıraya geç. 4, 5 derken dizi bitti. İşte insertion sort'un temel çalışma prensibini öğrendin.

![big-o-insertion](https://raw.githubusercontent.com/Kodluyoruz/taskforce/main/veri-yapilari-algoritmalar/insertion-sort/figures/insertion-sort.png)










## Proje 

[22,27,16,2,18,6] -> Insertion Sort

- Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
- Big-O gösterimini yazınız.
- Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız

- [7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.


```
Average case: Aradığımız sayının ortada olması
Worst case: Aradığımız sayının sonda olması
Best case: Aradığımız sayının dizinin en başında olması.
```

Aşamalar:
1. [22,27,16,2,18,6] Listenin en küçük elemanı 2 olduğu için en baştaki 22 ile yer değiştirsin. (n)
2. [2,27,16,22,18,6] Listenin ikinci en küçük elemanı 6 olduğu için 27 ile yer değiştirsin. (n-1)
3. [2,6,16,22,18,27] Listenin üçüncü en küçük elemanı 16 olduğu için aynı yerde kalsın. (n-2)
4. [2,6,16,22,18,27] Listenin dördüncü en küçük elemanı 18 olduğu için 22 ile yer değiştirsin. (1)
5. [2,6,16,18,22,27] => Sonuç

- 1 den n e kadar olan sayıların toplamı n*(n+1)/2 = n^2+n/2 
- n^2+n/2 dominant n^2 -> Big-O o(n²)
- 18 Sayısı ortada olduğundan dolayı "Average Case" kapsamına girer.

Aşamalar:
- [7,3,5,8,2,9,4,15,6] Listenin en küçük elemanı 2 olduğu için en baştaki 7 ile yer değiştirsin. (n)
- [2,3,5,8,7,9,4,15,6] Listenin ikinci en küçük elemanı 3 olduğu için olduğu yerde kalsın. (n-1)
- [2,3,5,8,7,9,4,15,6] Listenin üçüncü en küçük elemanı 4 olduğu için 5 ile yer değiştirsin. (n-2)
- [2,3,4,8,7,9,5,15,6] Listenin dördüncü en küçük elemanı 5 olduğu için 8 ile yer değiştirsin. (n-3)
- [2,3,4,5,7,9,8,15,6]
