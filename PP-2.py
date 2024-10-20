def my_function(a, b=[]):

    b.append(a)

    return b



x = my_function(1)

y = my_function(2, [])

z = my_function(3)



print(x, y, z)