"""
' set1 = {12,2,0,3,8}
set2 = {15,10,12,3,6}
Verilen kümelerin simetrik farkını bulup ekrana yazan programı tasarlayın.'
"""


set1 = {12,2,0,3,8}
set2 = {15,10,12,3,6} 
new_set = set1 ^ set2
print(new_set)
# {0, 2, 6, 8, 10, 15}
