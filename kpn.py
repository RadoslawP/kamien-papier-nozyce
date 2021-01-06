#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
liczba = random.randint(0, 2)

if liczba==0:
	wybor_komputera='kamien'
elif liczba==1:
	wybor_komputera='papier'
else:
	wybor_komputera='nozyce'

print ("Komputer wybral: ", wybor_komputera)
