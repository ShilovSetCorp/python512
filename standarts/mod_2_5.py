import operator as op
from functools import partial


# print(op.add(4, 5))
# print(op.mul(4, 5))
# print(op.contains([2, 4, 5], 5))
#
# x = [1, 2, 3]
# f = op.itemgetter(1)  # f(x) == x[1] == 2
# print(f(x))
#
# g = op.attrgetter("sort")  # f(x) == x.sort
# print(g([4, 5, 6]))
#
# r = int("1101", base=2)
# print(r)
# int_2 = partial(int, base=2)
# t = int_2("1101")
# print(t)
#
# sort_by_last = partial(list.sort, key=op.itemgetter(-1))  # itemgetter(-1) - last element
# y = ["abc", "cba", "abb"]
# sort_by_last(y)
# print(y)  # sorted by last element in strings


def mod_checker(x, mod=0):
    return lambda y: y % x == mod


mod_3 = mod_checker(3)

print(mod_3(3))
print(mod_3(4))
print(op.__doc__)
