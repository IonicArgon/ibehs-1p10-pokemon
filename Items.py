# base class for the pokeballs and berries
class AbstractPokeball:
    def __init__(self, name, modifier):
        self.name = name
        self.modifier = modifier

    def get_name(self):
        return self.name
    
    def get_modifier(self):
        return self.modifier

# the pokeballs
class Pokeball(AbstractPokeball):
    def __init__(self):
        super().__init__("Pokeball", 1)

class Greatball(AbstractPokeball):
    def __init__(self):
        super().__init__("Greatball", 1.5)

class Ultraball(AbstractPokeball):
    def __init__(self):
        super().__init__("Ultraball", 2)

class Masterball(AbstractPokeball):
    def __init__(self):
        super().__init__("Masterball", 255)

# the base class for the berries
class AbstractBerry:
    def __init__(self, name=None, modifier=1):
        self.name = name
        self.modifier = modifier

    def get_name(self):
        return self.name
    
    def get_modifier(self):
        return self.modifier

# the berries
class Razzberry(AbstractBerry):
    def __init__(self):
        super().__init__("Razzberry", 1.5)

class SilverPinapBerry(AbstractBerry):
    def __init__(self):
        super().__init__("Silver Pinap Berry", 1.8)

class GoldenRazzberry(AbstractBerry):
    def __init__(self):
        super().__init__("Golden Razzberry", 2.5)