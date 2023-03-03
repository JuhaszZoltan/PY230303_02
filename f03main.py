from f03module import *

egitestek:list[Egitest] = []
file = open(file='egitestek.txt', mode='r', encoding='utf-8')
for s in file: egitestek.append(Egitest(s))

print(f'1. feladat: {len(egitestek)} égitest van a listában')

bsz:int = 0
for e in egitestek:
    if e.hol_kering == 'Nap':
        bsz += 1
print(f'2. feladat nap körül keringő égitestek száma: {bsz}')

mi:int = 0
for i in range(1, len(egitestek)):
    if egitestek[i].tavolsag < egitestek[mi].tavolsag:
        mi = i
print(f'3. feladat: a {egitestek[mi].elnevezes} kering a legközelebb')

elk:list[str] = []
for e in egitestek:
    if not e.direktirany:
        elk.append(e.elnevezes)
print('4. feladat: ellenkező irányba keringő égitestek:')
for n in elk:
    print(f'\t- {n}')

ke:str = input('5. feladat - keredsett égitest neve: ')
for e in egitestek:
    if e.elnevezes == ke:
        if e.felfedezo != '---' and e.felf_ev != 0:
            print(f'\tfelfedező: {e.felfedezo}')
            print(f'\tfelfedezés éve: {e.felf_ev}')
        else:
            print(f'\tA {ke} benne van a listában,')
            print('\tde a felfedezésének körülményei nem ismertek')
        break
else: print(f'\ta {ke} nem szerepel a listába')
