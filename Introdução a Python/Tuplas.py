tuple = ()

tuple = tuple + (1,)
tuple = tuple + ([2, 3, 4, 5, 6],)

print(tuple)

print(type(tuple))

tuple[1][2] = 100

print(tuple)
