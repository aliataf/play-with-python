def ispresent(person):
    names = ['A', 'B', 'C']
    if person in names:
        return True
    else:
        return False

def nodigit(person):
    if person.isalpha():
        return True
    else:
        return False