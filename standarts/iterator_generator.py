from random import random


def gener(k):
    for y in range(k):
        if y > 1:
            return 'No more elements'
        yield random()


gen = gener(3)
for i in gen:
    print(i)

print(type(gener(5)))
