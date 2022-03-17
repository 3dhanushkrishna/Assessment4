def type_adder(list1):
    list2 = []

    for i in list1:
        list2.append(type(i))
    return list2

list1 = [3.14, 66, "Teddy", [], {}]
print(type_adder(list1))
