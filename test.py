def add(a, b):
    return a + b


if (val:=add(6, 7)) > 10:
    print("high")
else:
    print("low")

print(val)