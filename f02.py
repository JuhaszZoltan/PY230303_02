szoveg:str = input('írj be egy tetszőleges szöveget: ')
szoveg = szoveg.lower()
ek:str = 'áéíóöőúüű'
em:str = 'aeiooouuu'
for i in range(len(ek)): szoveg = szoveg.replace(ek[i], em[i])
spec:str = ',;:.!?'
for sc in spec: szoveg = szoveg.replace(sc, '\0')
szavak:list[str] = szoveg.split()
szoveg = szavak[0]
for szo in szavak[1:]: szoveg += szo.title()
print(f'calmeCase változat: {szoveg}')