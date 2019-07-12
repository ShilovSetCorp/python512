def summ(x, y):
    print(x + y)


summ(3, 5)
summ(56, 67)
print(type(summ))
print(id(summ))

a = [1, 2, 3]
print(id(a))
print(id([1, 2, 3]))

b = [1, 2, 3]
c = b
print(c is b)
print(b is [1, 2, 3])


def list_sum(lst):
    res = 0
    for el in lst:
        res += el
    return res


def summm(a, b):
    return a + b


y = summm(12, 345)
z = list_sum([1, 2, 3])
print(y)
print(z)

x = [1, 2, 3]

x.append(4)
x.append(5)

print(x)

top = x.pop()
print(top)
print(x)

top = x.pop()
print(top)
print(x)


def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        y = x + 1
        while True:
            if y % 5 == 0:
                return y
            y += 1


print(closest_mod_5(7))

lst = [10, 20]
summm(*lst)  # = summm(lst[0], lst[1])

args = {'a': 10, 'b': 20}
summm(**args)  # = summm(key1 = args[key1]


#                        key2 = args[key2])


def printab(a, b, **kwargs):
    print("a ", a)
    print("b ", b)
    print("additional arguments:")
    for key in kwargs:
        print(key, kwargs[key])


printab(10, 20, c=30, d=40, jimmi=123)


def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res


print(s(21))


def combineCounter(n, k):
    if k > n:
        return 0
    elif k == 0:
        return 1
    else:
        return combineCounter(n - 1, k) + combineCounter(n - 1, k - 1)


n, k = map(int, input().split())

print(combineCounter(n, k))

n = int(input())
scopes = {'global': {'funcs': [], 'vars': []}}


def add(scopes, current_namespace, what):
    if current_namespace not in scopes:
        scopes[current_namespace] = {}
        scopes[current_namespace]['vars'] = []
        scopes[current_namespace]['vars'].append(what)
    else:
        if 'vars' not in scopes[current_namespace]:
            scopes[current_namespace]['vars'] = []
            scopes[current_namespace]['vars'].append(what)
        else:
            scopes[current_namespace]['vars'].append(what)


def create(scopes, current_namespace, parent_namespace):
    if current_namespace not in scopes:
        scopes[current_namespace] = {}
        scopes[current_namespace]['funcs'] = []
        scopes[current_namespace]['vars'] = []
        scopes[parent_namespace]['funcs'].append(current_namespace)
        scopes[current_namespace]['parent'] = parent_namespace
    else:
        if 'funcs' not in scopes[current_namespace]:
            scopes[current_namespace]['funcs'] = []
            scopes[current_namespace]['parent'] = parent_namespace
            scopes[current_namespace]['funcs'].append(current_namespace)
        else:
            scopes[current_namespace]['funcs'].append(current_namespace)
            scopes[parent_namespace]['funcs'].append(current_namespace)


def search(scopes, namespace, what):
    if what in scopes[namespace]['vars']:
        return namespace
    else:
        try:
            upper_namespace = scopes[namespace]['parent']
        except KeyError:
            return None
        return search(scopes, upper_namespace, what)


#
# for i in range(n):
#     command = input().split()
#     if command[0] == 'add':
#         add(scopes, command[1], command[2])
#     elif command[0] == 'create':
#         create(scopes, command[1], command[2])
#     elif command[0] == 'get':
#         print(search(scopes, command[1], command[2]))


class My:
    pass


print(My)
x = My()
print(x)


class MySec:
    def __init__(self):
        self.count = 0


print(MySec)
m1 = MySec()
print(m1.count)


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0

    def can_add(self, v):
        if self.current + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        self.current += v


class Buffer:

    def __init__(self):
        self.arr = []

    def add(self, *a):
        self.arr.extend(a)
        while len(self.arr) - 5 >= 0:
            print(sum(self.arr[0:5]))
            self.arr = self.arr[5:]

    def get_current_part(self):
        print(self.arr)


class Buffer:

    def __init__(self):
        self.current_part = []

    def add(self, *a):
        self.current_part.extend(a)
        while len(self.current_part) - 5 >= 0:
            print(sum(self.current_part[0:5]))
            self.current_part = self.current_part[5:]

    def get_current_part(self):
        return self.current_part

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()


class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar()
a.foo()

c = A()

print(a.val)
print(b.val)
print(c.val)