str = 'reversal'
reversed_str = str[::-1]
print(reversed_str)

# recursive approach
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
print(string_reverse(str))