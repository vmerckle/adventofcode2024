numbers = [str(i) for i in range(0, 10)]
def parse(filename, logic=False):
    with open(filename, "r") as f:
        s = f.read()
    
    n = len(s)
    i = -1
    lp = []
    doing = True
    while i < n:
        i += 1
        if n-i <= 8:
            break
        if s[i:i+4] == "do()":
            doing = True
        if logic and not doing:
            continue

        if s[i:i+7] == "don't()":
            doing = False


        if s[i:i+4] != "mul(":
            continue
        i += 4
        # very manual, otherwise use a regex..
        a = ""
        while s[i] in numbers:
            a += s[i]
            i += 1
            if len(a) == 3:
                break
        if s[i] != "," or len(a) == 0:
            continue
        a = int(a)
        i += 1
        b = ""
        while s[i] in numbers:
            b += s[i]
            i += 1
            if len(b) == 3:
                break
        if s[i] != ")" or len(b) == 0:
            continue
        b = int(b)
        lp.append((a,b))
    return lp

def multall(lp):
    return sum([a*b for a,b in lp])


filename = "demo_input.csv"
filename = "input.csv"
print(multall(parse(filename)))
print(multall(parse(filename, logic=True)))
