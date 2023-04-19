upcaseA = 65
upcaseZ = 90
str = input('string to parse: ')
indices = []
i = 0
for char in str:
    if ord(char) >= upcaseA and ord(char) <= upcaseZ:
        indices.append(i)
    i += 1
print(indices)



