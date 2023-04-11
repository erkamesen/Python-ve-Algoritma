# Merge Sort

Insertion Sort'da, Big-O gösteriminden dolayı input'um arttığında n2 olduğunda dolayı çalışma zamanı artıyor.

Peki daha hızlı bir şekilde sıralama yapılabilir mi? Evet, Merge Sort burada yardımımıza koşuyor. Bir listeyi her adımda parçaya ayırıp tek eleman kalıncaya kadar bölüyor. Böldükten sonra sıralı bir şekilde bize sunuyor (Performans).

![merge-sort](https://raw.githubusercontent.com/Kodluyoruz/taskforce/main/veri-yapilari-algoritmalar/merge-sort/figures/merge-sort.png)

![big-o-merge](https://raw.githubusercontent.com/Kodluyoruz/taskforce/main/veri-yapilari-algoritmalar/merge-sort/figures/big-o-merge.png)

Insertion sort'da, time complexity n2 olduğundan ötürü çalışma zamanımız artıyordu. Merge sort'da ise nlogn olduğu için açık ara performans olarak daha iyi diyebiliriz.

Kaynaklar:
- [merge-sort-detail-with-code](https://www.programiz.com/dsa/merge-sort)
- [merge-sort-article](https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort)
- [merge-sort-nedir-kod-dökümanı](http://cagataykiziltan.net/algoritmalar/1-siralama-algoritmalari/4-birlestirmeli-siralama/)
- [merge-sort-wiki](https://tr.wikipedia.org/wiki/Birle%C5%9Ftirmeli_s%C4%B1ralama)


# Proje 

[16,21,11,8,12,22] -> Merge Sort

- Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
- Big-O gösterimini yazınız.


Aşamalar:
1. [16,21,11,8,12,22] Listeyi ortadan bölelim.
2. [16,21,11] [8,12,2]
