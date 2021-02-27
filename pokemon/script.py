from trainer import Trainer
from pokemon import Pokemon
import move

#print('Hello world')

squirtle = Pokemon('Squirtle', 5, 22, 22, 'Water')
bulbasaur = Pokemon('Bulbasaur', 5, 20, 20, 'Grass')
charmander = Pokemon('Charmander', 5, 19, 19, 'Fire')
pikachu = Pokemon('Pikachu', 5, 18, 18, 'Electric')


ash = Trainer('Ash', [squirtle, pikachu])
gary = Trainer('Gary', [bulbasaur, charmander])

print(ash)
print(gary)

ash.attack(gary)

print(ash)
print(gary)
