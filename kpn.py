#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#przygotowanie
import random
zwyciezca=''
liczba = random.randint(0, 2)

#losowe wybieranie
if liczba==0:
	wybor_komputera='kamien'
elif liczba==1:
	wybor_komputera='papier'
else:
	wybor_komputera='nozyce'

#sprawdzanie poprawnosci wyboru
wybor_uzytkownika=''
while  (wybor_uzytkownika != 'kamien' and
	wybor_uzytkownika != 'papier' and
	wybor_uzytkownika != 'nozyce'):
	wybor_uzytkownika=input('Kamien, papier czy nozyce? ')

#prezentowanie wyboru
print ("Wybrales "+wybor_uzytkownika+ ", a komputer wybral "+wybor_komputera+"!")

#logika gry
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

#Ogloszenie zwyciezcy
if zwyciezca=='Remis':
	print('Obaj wybralismy', wybor_komputera+', zagraj ponownie.')
else:
	print('Wygral', zwyciezca)
