#f_pokemon_TEACHER_VERSION.py

'''
title: pokemon type checker
author: brian hager
date: nov 21, 2022
'''

# --- INPUTS --- #
def openFileRead(FILENAME):
    return open(FILENAME)

def getFileContent(FILE):
    '''
    extracts the contents of the file into a 2D array
    :param FILE: (obj)
    :return: (list)(2d array)
    '''
    TEXT_LIST = FILE.readlines()
    FILE.close()
    for i in range(len(TEXT_LIST)):
        if TEXT_LIST[i][-1] == '\n':
            TEXT_LIST[i] = TEXT_LIST[i][:-1]
        TEXT_LIST[i] = TEXT_LIST[i].split(",")
    return TEXT_LIST

def getPokemon(POSITION):
    '''
    asks user for pokemon and checks that it's one that exists
    :param POSITION: attacking or defending pokemon
    :return: (str)
    '''
    global POKEMON
    MONSTER = input(f"{POSITION} Pokemon: ")
    for species in POKEMON:
        if species[1] == MONSTER:
            return MONSTER
    print("Your pokemon was not found! Please try again. ")
    return getPokemon(POSITION)


# --- PROCESSING --- #
def getPokemonTypes(ACTIVE):
    '''
    get both types of the given pokemon
    :param ACTIVE: (str)(name of pokemon)
    :return: (list)(types of active pokemon)
    '''
    global POKEMON
    POKE_TYPES = []
    for MONSTER in POKEMON: # for each line in the pokedex file
        print(MONSTER)
        if ACTIVE == MONSTER[1]: # if the inputted pokemon == the name of the pokemon
            POKE_TYPES.append(MONSTER[2]) # appends the first attribute of that pokemon
            if MONSTER[3] != "":  # if the pokemon has a second attribute
                POKE_TYPES.append(MONSTER[3]) # append the second attribute
            return POKE_TYPES

def getDamageMultiplier(ATTACK, DEFEND):
    '''
    determiens how the pokemon affects the damage delt by the attacking pokemon
    :param ATTACK: (list)(attributes)
    :param DEFEND: (list)(attributes)
    :return: (int)(multiplier)
    '''
    global TYPES
    MULTIPLIER = 1
    for i in range(len(ATTACK)):
        ATTACK_TYPE_NUM = getTypeNum(ATTACK[i])
        for j in range(len(DEFEND)):
            DEFEND_TYPE_NUM = getTypeNum(DEFEND[j])
            MULTIPLIER = MULTIPLIER * TYPES[ATTACK_TYPE_NUM][DEFEND_TYPE_NUM]
    return MULTIPLIER

def getTypeNum(TYPE):
    '''
    converts the pokemon type into its number equivalent based on the type table
    :param TYPE: (str)(pokemon)
    :return: (int)(row and column of attack and defend type)
    '''
    global TYPES_HEADING
    for i in range(len(TYPES_HEADING)):
        if TYPE == TYPES_HEADING[i]:
            return i

# --- OUTPUTS --- #
def displayDamageModifier(VALUE):
    '''
    displays the final damage modifier nicely
    :param VALUE: (int)(multiplier)
    :return: (none)
    '''
    print(f"VALUE: {VALUE}")
    if VALUE == 1:
        print("Types do not affect damage")
    if VALUE == 0:
        print("Attacks will do no damage")
    if VALUE > 1:
        print(f" Attacks will be SUPER EFFECTIVE and do {VALUE}x damage! ")
    else:
        NEW_VALUE = int(1/VALUE)
        print(f"Attacks will be NOT VERY AFFECTIVE and will do {NEW_VALUE}x damage! ")


# --- MAIN PROGRAM --- #

if __name__ == "__main__":
    POKEMON = getFileContent(openFileRead("pokemon_no_mega - pokemon_no_mega.csv"))
    TYPES = getFileContent(openFileRead("types.csv"))
    print(POKEMON)
    for i in range(len(TYPES)): # sanitizes the types of file
        TYPES[i].pop(0)
        for j in range(len(TYPES[i])):
            try:
                TYPES[i][j] = float(TYPES[i][j])
            except ValueError:
                pass
    TYPES_HEADING = TYPES.pop(0)

    while True:
        ATTACKING = getPokemon("Attacking")
        DEFENDING = getPokemon("Defending")

        ATTACKING_TYPES = getPokemonTypes(ATTACKING)
        DEFENDING_TYPES = getPokemonTypes(DEFENDING)
        print(ATTACKING_TYPES)
        print(DEFENDING_TYPES)

        DAMAGE_MULTIPLIER = getDamageMultiplier(ATTACKING_TYPES, DEFENDING_TYPES)

        displayDamageModifier(DAMAGE_MULTIPLIER)