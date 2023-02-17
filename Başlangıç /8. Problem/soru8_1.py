"""
' set1 = {1,12,2,6,7,8}
set2 = {15,0,1,3,6}
Verilen kümelerden set1 in set2 den farkını bulup sonucu ekrana çıktı olarak veren programı tasarlayın.'
"""

set1 = {1,12,2,6,7,8} 
set2 = {15,0,1,3,6}
new_set = set1 - set2
print(new_set)
# {8, 2, 12, 7}


set1 = {1,12,2,6,7,8} 
set2 = {15,0,1,3,6}
new_set = set1.diffence(set2)
print(new_set)
# {8, 2, 12, 7}
