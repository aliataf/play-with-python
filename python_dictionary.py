my_d = {'test': 1, 2: True}
my_d['test'] = 4
# del my_d[2]
print(my_d)

for key, value in my_d.items():
    print(key, value)