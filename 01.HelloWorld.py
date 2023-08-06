x = 10
y = 11

print(id(x))
print(id(y))

import keyword

lst = keyword.kwlist

for ls in lst:
    print(ls)

b_1 = 0b11
print(b_1)

o_1 = 0o11
print(o_1)

# real part + imaginary part  >> to represent the complex number
y = 1 + 2j
print(y/2)

import random as r

print(r.randint(0, 10))

print(list(range(0, 10))[-1:10])
