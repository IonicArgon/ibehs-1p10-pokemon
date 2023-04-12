# IMPORT EVERYTHING
from Pokemon_class import Pokemon
from PokemonDirectory import PokemonDirectory
from Items import *
import random as rd

# this is our pokedex
Pokedex = PokemonDirectory("pokemon.csv")

# this is our list of caught pokemon
list_of_caught_pokemon = []

# this runs when we catch a pokemon
def catch_pokemon():
    # generate a random pokemon
    pokemon_id = str(rd.randint(1, 721))
    pokemon_csv = Pokedex.get_pokemon(pokemon_id)
    types = [pokemon_csv[1], pokemon_csv[2]]
    pokemon = Pokemon(pokemon_csv[0], types)
    
    # generate random stats based on CP
    generated_cp = rd.randint(5, 1500) 
    random_range = round(15 * (generated_cp/1500))
    random_range = 2 if random_range <= 1 else random_range
    random_scaled_stats = [i for i in rd.choices(range(1, random_range), k=3)]
    
    # set the pokemon's stats
    pokemon.set_CP(generated_cp)
    pokemon.set_stats(*random_scaled_stats)
    pokemon.set_catch_rate()

    print(f'\nYou encountered a wild {pokemon.get_name()}!')
    print("It has the following stats:")
    pokemon.display_details()

    # handling the catching of the pokemon
    throw_counter = 0
    while True:
        # getting action
        contin = input("Would you like to throw a Pokeball? (y/n): ")
        if contin.lower() == "n":
            print("\nYou ran away!\n")
            break
        elif contin.lower() == "y":
            pass
        else:
            print("\nInvalid input. Please try again.\n")
            continue

        # getting pokeball
        pokeball = None
        pokeball_ask = input("Which Pokeball would you like to use? (Pokeball [p], Greatball [g], Ultraball [u], Masterball [m]): ")
        if pokeball_ask.lower() == "p":
            pokeball = Pokeball()
        elif pokeball_ask.lower() == "g":
            pokeball = Greatball()
        elif pokeball_ask.lower() == "u":
            pokeball = Ultraball()
        elif pokeball_ask.lower() == "m":
            pokeball = Masterball()
        else:
            print("\nInvalid input. Please try again.\n")
            continue

        # getting berry
        berry = AbstractBerry()
        berry_ask = input("Would you like to use a berry? (Razzberry [r], Silver Pinap Berry [s], Golden Razzberry [g], None [n]): ")
        if berry_ask.lower() == "r":
            berry = Razzberry()
        elif berry_ask.lower() == "s":
            berry = SilverPinapBerry()
        elif berry_ask.lower() == "g":
            berry = GoldenRazzberry()
        elif berry_ask.lower() == "n":
            pass

        # catching the pokemon
        pokemon.capture(pokeball, berry)
        if pokemon.get_caught():
            print(f'\nYou caught the {pokemon.get_name()}!\n')
            list_of_caught_pokemon.append(pokemon)
            break
        else:
            print("\nYou missed!\n")
            throw_counter += 1

        if throw_counter == 3:
            print("\nYou ran out of Pokeballs!")
            print(f'The {pokemon.get_name()} ran away!\n')
            break

# this is the main function
def main():
    print("Welcome to the Pokemon GO Catching Simulator!")

    # main loop
    while True:
        # menu
        print("What would you like to do?")
        print("1. Catch a Pokemon")
        print("2. View your Pokemon")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print()
            catch_pokemon()
        elif choice == "2":
            if len(list_of_caught_pokemon) == 0:
                print("\nYou have not caught any Pokemon yet!\n")
            else:
                print("\nYour Pokemon:")
                print(f'{"Name":<15}{"CP":<15}')
                for pokemon in list_of_caught_pokemon:
                    print(f'{pokemon.get_name():<15}{pokemon.get_CP():<15}')
                print()
        elif choice == "3":
            print("\nThank you for playing!\n")
            break
        else:
            print("\nInvalid input. Please try again.\n")

if __name__ == "__main__":
    main()