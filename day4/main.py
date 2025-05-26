def solve(filename):
    M = []
    with open(filename, "r") as f:
        while l := f.readline():
            M.append(l.rstrip())
    #print([len(x) for x in M], len(M))
    n = len(M) # M is a n x n
    s = 0
    for i in range(n):
        for j in range(n):
            words = []

            if i <= n-4: # ----
                words.append(M[i][j]+M[i+1][j]+M[i+2][j]+M[i+3][j])
                if j > 2: # /
                    words.append(M[i][j]+M[i+1][j-1]+M[i+2][j-2]+M[i+3][j-3])
                if j <= n-4: # \
                    words.append(M[i][j]+M[i+1][j+1]+M[i+2][j+2]+M[i+3][j+3])
            if j <= n-4: # |
                words.append(M[i][j]+M[i][j+1]+M[i][j+2]+M[i][j+3])

            for w in words:
                if w == "XMAS" or w == "SAMX":
                    s += 1

    return s


def solve2(filename):
    M = []
    with open(filename, "r") as f:
        while l := f.readline():
            M.append(l.rstrip())
    #print([len(x) for x in M], len(M))
    n = len(M) # M is a n x n
    s = 0
    for i in range(n):
        for j in range(n):
            if M[i][j] != "A":
                continue
            if i > n-2 or i < 1:
                continue
            if j > n-2 or j < 1:
                continue
            l = M[i-1][j-1]+M[i][j]+M[i+1][j+1] # \
            r = M[i-1][j+1]+M[i][j]+M[i+1][j-1] # /
            if l == "MAS" or l == "SAM":
                if r == "MAS" or r == "SAM":
                    s += 1
    return s

filename = "demo_input.csv" #10x10
filename = "input.csv" #140x140, ok for n**2 complexity

print(solve(filename))
print(solve2(filename))
