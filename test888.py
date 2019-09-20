import ephem

g = input()
nfm = ephem.next_full_moon(g)
print(nfm)