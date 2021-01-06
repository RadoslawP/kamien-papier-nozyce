#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
zwyciezca=''
liczba = random.randint(0, 2)

if liczba==0:
	wybor_komputera='kamien'
elif liczba==1:
	wybor_komputera='papier'
else:
	wybor_komputera='nozyce'

wybor_uzytkownika=input('Kamien, papier czy nozyce? ')
print ("Wybrales "+wybor_uzytkownika+ ", a komputer wybral "+wybor_komputera+"!")

if wybor_komputera==wybor_uzytkownika:
	zwyciezca='Remis'
elif wybor_komputera=='papier' and wybor_uzytkownika=='kamien':
	zwyciezca='Komputer'
elif wybor_komputera=='kamien' and wybor_uzytkownika=='nozyce':
	zwyciezca='Komputer'
elif wybor_komputera=='nozyce' and wybor_uzytkownika=='papier':
	zwyciezca='Komputer'
else:
	zwyciezca='Uzytkownik'

print(zwyciezca, 'wygral!')
