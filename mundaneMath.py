def math():
    s = 0
    for i in range(1,101):
        if i % 2 == 0:
            s = s + i
            i = i +1
    return s
print(math())


