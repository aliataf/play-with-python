my_lists = [1, 2, 3]

def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_lists, 4)
print(my_lists)
print(new_list)