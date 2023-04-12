import csv

class PokemonDirectory:
    def __init__(self, csv_file):
        self.directory = {}
        self.csv_file = csv_file
        self.__load_directory()

    # loads the csv file into a dictionary
    def __load_directory(self):
        with open(self.csv_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                dictionary_index = row[0]
                if dictionary_index in self.directory:
                    continue
                self.directory[dictionary_index] = row[1:]

    # returns the pokemon's data
    def get_pokemon(self, id_number):
        return self.directory[id_number]