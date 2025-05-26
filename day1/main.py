def parse(filename):
    l1, l2 = [], []
    with open(filename, "r") as f:
        while l := f.readline():
            l = l.split(" ")
            a, b = l[0].rstrip(), l[3].rstrip()
            l1.append(a),
            l2.append(b)
    return l1, l2

l1, l2 = parse("demo_input.csv")
print(l1)
print(l2)
