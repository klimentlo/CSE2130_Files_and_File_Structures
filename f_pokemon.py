#f_pokemon.py

'''
title: pokemon
author: kliment lo
date: november 17, 2022
'''

import csv

def readCSV(number):
    if number == 1:
        FILE = open("pokemon_no_mega - pokemon_no_mega.csv", newline="")
    if number == 2:
        FILE = open("types.csv", newline="")
    READER = csv.reader(FILE)
    POKEMON = []
    for row in READER: # for each node in the array)
        POKEMON.append(row)
    FILE.close()
    return POKEMON

def getBalls(balls):
    balls + 90
    return balls

def getPokemon(POKEMONS, pokemon):
    '''
    requests user for pokemon
    :return:
    '''
    POKEMON = input(f"{pokemon} pokemon: ").lower()
    for i in range(len(POKEMONS)):
        if POKEMONS[i][1].lower() == POKEMON:
            return POKEMONS[i]
    print("It does not exist! ")
    getPokemon(POKEMONS, pokemon)



if __name__ == "__main__":
    POKEMONLIST = readCSV(1)
    ATTRIBUTES = readCSV(2)
    print(POKEMONLIST)
    for i in range(len(ATTRIBUTES)):
        print(ATTRIBUTES[i])
    ATTACKER = getPokemon(POKEMONLIST, "Attacking")
    DEFENDER = getPokemon(POKEMONLIST, "Defending")

    ATTRIBUTESA = ATTACKER[2:4]
    ATTRIBUTESD = DEFENDER[2:4]
    print(ATTRIBUTESA)
