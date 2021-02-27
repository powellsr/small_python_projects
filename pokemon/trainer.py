class Trainer:
  def __init__(self, name, pokemon=[]):
    self.name = name
    self.pokemon = pokemon
    self.active_pokemon = None
    if len(pokemon) > 0:
      self.active_pokemon = pokemon[0]

  def potion(self):
    if self.active_pokemon.health == self.active_pokemon.max_health:
      print('It won\'t have any effect...')
    else:
      self.active_pokemon.health += 20
      if self.active_pokemon.haelth > self.active_pokemon.max_health:
        self.active_pokemon.health = self.active_pokemon.max_health
      print(self.active_pokemon.name, 'had it\s health restored!', 
      self.active_pokemon.name, 'has', str(self.active_pokemon.health), 
      'health')

  def attack(self, other):
    print(self.active_pokemon.name, 'attacked', other.active_pokemon.name +  '!')
    self.active_pokemon.attack(other.active_pokemon)


  def switch(self, new_pokemon):
    for pkmn in self.pokemon:
      if pkmn.name == new_pokemon:
        self.active_pokemon = pkmn
        print('Switched to', new_pokemon)
        return
    print('No such pokemon in party')


  def __repr__(self):
      repr_string = ''
      repr_string += self.name
      repr_string += '\n'
      for pkmn in self.pokemon:
          repr_string += '\t> '
          if pkmn == self.active_pokemon:
              repr_string += '* '
          repr_string += pkmn.name
          repr_string += '\t'
          repr_string += 'Health: '
          repr_string += str(pkmn.health)
          repr_string += ' / '
          repr_string += str(pkmn.max_health)
          repr_string += '\n'
      return repr_string
