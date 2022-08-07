set_a = {1, 2, 3, 4, 5, 5}
set_b = {3, 4, 5, 6, 7, 8}
print(set_a)
print("union", set_a.union(set_b)) # or |
print("intersection", set_a.intersection(set_b)) # or &
print("difference", set_a.difference(set_b)) # or -
print("symmetrical difference", set_a.symmetric_difference(set_b)) # or ^

set_a.add(6)
print(set_a)

set_a.remove(2)
print(set_a)

set_a.discard(3)
print(set_a)
