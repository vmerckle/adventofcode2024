def parse(filename):
    ll = []
    with open(filename, "r") as f:
        while line := f.readline():
            line = line.split()
            ll.append([int(x) for x in line])
    return ll



# obviously inefficient pbdampener, no need to read the list again
# same complexity however
def safe(l, pbdampener=False):
    if len(l) <= 1:
        return True
    # sequence must be strictly monotonous,
    # but not change by more than 3

    up = l[0] < l[1] # true if increasing
    lastx = l[0]
    for i in range(1, len(l)):
        x = l[i]
        d = abs(x - lastx)
        if d == 0 or d > 3: # integers
            if not pbdampener:
                return False
            second = list(l)
            second.pop(i)
            l.pop(i-1)
            return safe(l) or safe(second)
        if up != (lastx < x): # necessary ()
            if not pbdampener:
                return False
            second = list(l)
            second.pop(i)
            l.pop(i-1)
            if i == 2:
                third= list(l)
                third.pop(0)
                return safe(l) or safe(second) or safe(third)
            return safe(l) or safe(second)
        lastx = x
    return True

filename = "demo_input.csv"
filename = "input.csv" # 1000 lines of 8 elements
ll = parse(filename)

#print(f"{len(ll)} lines of {max([len(l) for l in ll])} elements")
#print(safe(ll[-1]))
print(sum([safe(l) for l in ll]))
print(sum([safe(l, pbdampener=True) for l in ll]))
