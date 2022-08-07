with open("new_file.txt", mode = 'r') as file:
    for x in file:
        print(x)

""" try:
    with open('new_file.txt', 'a') as file:
        file.writelines(['\nThis is a new file', '\nThis is another line'])
except FileNotFoundError as e:
    print("Error", e) """
