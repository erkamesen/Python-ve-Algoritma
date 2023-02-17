"""
' set1 = {5,2,4,6,7,1}
set2 = {5,3,11}
Verilen 2 kümenin kesişimini çıktı olarak gösteren programı tasarlayın.'
"""

set1 = {5,2,4,6,7,1} 
set2 = {5,3,11} 
set3 = set1.intersection(set2)
print(set3)
# {5}


set1 = {5,2,4,6,7,1} 
set2 = {5,3,11} 
set3 = set1 & set2
print(set3)
# {5}
