# print("cabdc".find("abc"))
# s = "asdasdas"
# print(s.rfind("as"))
# print(s.find("as"))
# print(s.startswith(("as", "asd")))
# print(s.startswith("as"))
# print(str.find.__doc__)

# capital = "London is the capital of Great Britain"
# template = "{} is the capital of {}"
# print(template.format("Moscow", "Russia"))
# template = "{1} is the capital of {0}"
# print(template.format("London", "Great Britain"))
# template = "{cap} is the capital of {country}"
# print(template.format(country="Great Britain", cap="London"))
#
# s, a, b = (input() for _ in range(3))
#
#
# def f(s, a, b, counter=0):
#     if a in b and a in s:
#         return 'Impossible'
#     if s == s.replace(a, b):
#         return counter
#     else:
#         counter += 1
#         s = s.replace(a, b)
#         return f(s, a, b, counter)
#
#
# print(f(s, a, b))

s, t = (input() for _ in range(2))
counter = 0
for i in range(len(s)):
    if s.find(t, i, i + len(t)) >= 0:
        counter += 1
print(counter)
