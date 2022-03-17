def prefix_adder(list1):
    list2 = []

    for i in list1:
        if len(i) > 0:
            list2.append("Dr. " +i)
        return list2

list1 = ["Sekar", "Chandra", "Pradeep", "Dhanush"]
print(prefix_adder(list1))