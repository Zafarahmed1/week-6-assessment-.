
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
list3 = [50, 60, 70, 80, 90]


set1 = set(list1)
set2 = set(list2)
set3 = set(list3)


common_elements = set1.intersection(set2, set3)


duplicate_list = list(common_elements)


print("Duplicate elements:", duplicate_list)