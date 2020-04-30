def beolvas(file):
    with open(file, 'r') as f:
        N = next(f)
        N = int(N)
        adat = []
        for sor in f.read().splitlines():
            p1, p2 = map(int, sor.split(" "))
            adat.append((p1, p2))
    return(adat, N)

def jatek(N, DATA):
    if N == 0 or len(DATA) == 0:
        return (None, None)
    r_nyertes = r_pont = None
    for index in range(N):
        p1, p2 = DATA[index]
        kulonbseg = abs(p1 - p2)
        if p1 > p2:
            nyertes = 'p1'
        else:
            nyertes = 'p2'
        if not r_nyertes and not r_pont:
            r_nyertes = nyertes
            r_pont = kulonbseg
        if kulonbseg > r_pont:
            r_nyertes = nyertes
            r_pont = kulonbseg
    return (r_nyertes, r_pont)

file="input.txt"
DATA, N=beolvas(file)
nyertes, pont = jatek(N, DATA)
print(nyertes, pont)