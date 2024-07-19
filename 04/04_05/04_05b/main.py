def has_unique_characters(data):
    unique_characters = frozenset(['!', '@', '#', '&', '*', "_", '?'])
    for x in data:
       if x in unique_characters:
           return True
       else:
        return False

print(has_unique_characters('!sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
