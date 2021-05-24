def several():
    n = input("Introduce the desired number of triples: ")

    for i in range(1, eval(n) + 1):
        a = i ** 2 - 1
        b = 2 * i
        c = i ** 2 + 1
        print(a, b, c)

def one():
    n = eval(input("Introduce the triple index: "))

    a = n ** 2 - 1
    b = 2 * n
    c = n ** 2 + 1
    print(a, b, c)

print("[1] Display a desired number of triples (from index 0)")
print("[2] Display just one triple by knowing its index (instantaneous)")
q = input("Please select one of above: ")

if q == "1":
    several()
elif q == "2":
    one()
else:
    print("ERROR: exiting...")
    exit()