"""
set1 = {5,12,52,0,8}
set2 = {2,5,1,9,8}
set3 = {4,5,6,0,10}
verilen 3 kümenin birleşimini ekrana yazdıran programı tasarla.
"""

set1 = {5,12,52,0,8} 
set2 = {2,5,1,9,8} 
set3 = {4,5,6,0,10} 
new_set = set1 | set2 | set3
print(new_set)
# {0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 52}
