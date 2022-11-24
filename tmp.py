num = 5
try:
    for num in num:
        print(num)
except TypeError:
    print(TypeError)
    print(num)
