def find_minimum_element(sorted_list):
    if len(sorted_list) == 0:
        return None
    else:
        return sorted_list[0]


sorted_list = [10, 20, 30, 40, 50, 60]
minimum_element = find_minimum_element(sorted_list)

if minimum_element is not None:
    print("Minimum element:", minimum_element)
else:
    print("The list is empty.")