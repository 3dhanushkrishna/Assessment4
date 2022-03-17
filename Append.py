def name_adder(x, y):
    for i in x:
        if len(i) > 0:
            y.append(i)
        return y

x = ["Dhanush" ,"kumar"]
y = ["Pradeep", "Kumar"]

print(name_adder(x, y))