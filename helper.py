"""BombParty_Helper.py: Simple programme qui t'aide à trouver des mots !"""

__author__ = "Pewoh"
__copyright__ = "Copyright 2020, The BombParty Helper Project"

import pyperclip
import random
import requests


repeat = True;

while repeat==True:
    mots = input("Entrez mots : ");
    print(mots)

    words = open("words.txt", "r")

    for ligne in words:
        if mots in ligne:
            print(ligne)
            pyperclip.copy(ligne)

    repeat = input("Voulez-vous tapez un autre mot ? O/N")

    if repeat=="o":
        repeat=True;
    else:
        repeat=False;
    
words.close()
    

