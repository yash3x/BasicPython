def add_number(*args):
    total = 0
    for a in args:
        total +=a
    print(total)

add_number(3)
add_number(3, 32)
add_number(2, 32, 10, 100)
