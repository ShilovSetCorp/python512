classes = {}


def add_class(classes, class_name, class_parents):
    if class_name not in classes:
        classes[class_name] = []
    classes[class_name].extend(class_parents)
    for parent in class_parents:
        if parent not in classes:
            classes[parent] = []


def found_path(classes, start, end, path=[]):
    path += [start]
    if start == end:
        return path
    if path not in classes:
        return None
    for node in classes[start]:
        if node not in path:
            newpath = found_path(classes, node, end, path)
            if newpath:
                return newpath
    return None


def answer(classes, parent, child):
    if not (parent or child) in classes or not found_path(classes, child, parent):
        return 'No'
    return 'Yes'


n = int(input())

for _ in range(n):
    class_description = input().split()
    class_name = class_description[0]
    class_parents = class_description[2:]
    add_class(classes, class_name, class_parents)

q = int(input())

for _ in range(q):
    request = input().split()
    parent = request[0]
    child = request[1]
    print(answer(classes, parent, child))
