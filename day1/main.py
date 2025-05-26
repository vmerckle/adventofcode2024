def parse(filename):
    l1, l2 = [], []
    with open(filename, "r") as f:
        while l := f.readline():
            l = l.split(" ")
            a, b = l[0].rstrip(), l[3].rstrip()
            l1.append(int(a)),
            l2.append(int(b))
    return l1, l2

def absdist(l1, l2):
    l1.sort()
    l2.sort()
    a = 0
    for i in range(len(l1)):
        a += abs(l1[i] - l2[i])
    return a

filename = "demo_input.csv"
filename = "input.csv"
l1, l2 = parse(filename)

print(absdist(l1, l2))

def similarity(l1, l2):
    freq = {}
    for x in l2:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    s = 0
    for x in l1:
        if x in freq:
            s += x * freq[x]
    return s

print(similarity(l1, l2))
