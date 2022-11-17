#f_pokemon.py

'''
title: pokemon
author: kliment lo
date: november 17, 2022
'''

import csv

def readFile():
    FILE = open("pokemon_no_mega - pokemon_no_mega.csv", newline="")
    READER = csv.reader(FILE)
    POKEMON = []
    for row in READER: # for each node in the array)
        POKEMON.append(row)
        print(row)
    FILE.close()
    return POKEMON

def getPokemon(POKEMONS):
    '''
    requests user for pokemon
    :return:
    '''
    POKEMON = input("Attacking pokemon: ")
    for i in range(len(POKEMONS)):
        if POKEMONS[i][1] == POKEMON:
            print("it exists!")
            return print("balls")
        if i == 721:
            print("It doesn't exist")
            getPokemon(POKEMONS)
if __name__ == "__main__":
    POKEMONLIST = readFile()
    ATTACKER = getPokemon(POKEMONLIST)