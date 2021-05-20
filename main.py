i = 1

n = input("Introduce the desired number of triples: ")

for i in range(0, eval(n)):
    a = i ** 2 - 1
    b = 2 * i
    c = i ** 2 + 1
    print(a, b, c)
    i += 1