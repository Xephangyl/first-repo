class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(f'{self.name} {self.name}!')

  def display_details(self):
    print(f'Entry Number: {self.entry}')
    print(f'Name: {self.name}')
    print(f'Type: {self.types}')
    print(f'Description: {self.description}')
    if self.is_caught:
      print(f'{self.name} has already been caught!')
    else:
      print(f'{self.name} has not been caught.')


bulbasaur = Pokemon(1, 'Bulbasaur', 'Grass and Poison', "Bulbasaur is a small, quadrupedal amphibian Pokémon that has blue-green skin with darker patches.", True)
charmeleon = Pokemon(5, 'Charmeleon', 'Fire', "Charmeleon is a bipedal, reptilian Pokémon. It has dark red scales and a cream underside from the chest down.", False)
lucario = Pokemon(448, 'Lucario', 'Fighting and Steel', "Lucario is a bipedal, canine-like Pokémon with predominantly blue and black fur.", True)

bulbasaur.display_details()
bulbasaur.speak()
charmeleon.display_details()
charmeleon.speak()
lucario.display_details()
lucario.speak()