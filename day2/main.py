def parse(filename):
    ll = []
    with open(filename, "r") as f:
        while line := f.readline():
            line = line.split()
            ll.append([int(x) for x in line])
    return ll

filename = "demo_input.csv"
filename = "input.csv" # 1000 lines of 8 elements
ll = parse(filename)
#print(f"{len(ll)} lines of {max([len(l) for l in ll])} elements")

def safe(l):
    if len(l) <= 1:
        return True
    # sequence must be strictly monotonous,
    # but not change by more than 3

    up = l[0] < l[1] # true if increasing
    lastx = l[0]
    for x in l[1:]:
        d = abs(x - lastx)
        if d == 0 or d > 3: # integers
            return False
        if up != (lastx < x): # necessary ()
            return False
        lastx = x
    return True

#print(safe(ll[-1]))
print(sum([safe(l) for l in ll]))
