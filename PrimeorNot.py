num = 2

if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "is not a Prime Number")
            break
    else:
        print(num, "is a Prime Number")