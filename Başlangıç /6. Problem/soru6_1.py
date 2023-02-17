"""
set1 = {3,2,4,5,6,7,8}
set2 = {4,12,5,1,6,8}
Verilen 2 tane kümenin birleşimini çıktı olarak gösteren programı tasarlayın.
"""



set1 = {3,2,4,5,6,7,8} 
set2 = {4,12,5,1,6,8}
set3 = set1.union(set2)
print(set3)
# {1, 2, 3, 4, 5, 6, 7, 8, 12}





set1 = {3,2,4,5,6,7,8} 
set2 = {4,12,5,1,6,8}
set3 = set1 | set2
print(set3)
# {1, 2, 3, 4, 5, 6, 7, 8, 12}
