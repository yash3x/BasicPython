magicNumber = int(input('Enter the magic number: '))

for n in range(101):
    if n == magicNumber:
        print(n, "Is the magic number")
        break
    else:
        print(n)