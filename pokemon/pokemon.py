class Pokemon:
  def __init__(self, name, level, health, max_health, type, moves=[], is_knocked_out=False):
    self.name = name
    self.level = level
    self.health = health
    self.max_health = max_health
    self.type = type
    self.moves = moves
    self.is_knocked_out = is_knocked_out
    
  def lose_health(self, health_lost):
    if health_lost > self.health:
      self.knock_out()
    else:
      self.health -= health_lost
      print(self.name, 'now has', str(self.health), 'health')
           
  def knock_out(self):
    self.health = 0
    self.is_knocked_out = True
    print(self.name, 'is knocked out!')

  def revive(self):
    self.health = self.max_health
    self.is_knocked_out = False
    print(self.name, 'is revived!', self.name, 'has', self.health, 'health')

  def attack(self, other):
    damage = self.level
    print(self.name, 'attacked!')
    if self.has_advantage(other):
      damage *= 2
      print('It\'s super effective!')
    elif self.has_disadvantage:
      damage = damage // 2
      print('It\'s not very effective...')
    other.lose_health(damage)

  def has_advantage(self, other):
    if (self.type == 'Fire' and other.type == 'Grass') \
    or (self.type == 'Grass' and other.type == 'Water') \
    or (self.type == 'Water' and other.type == 'Fire'):
      return True
    return False

  def has_disadvantage(self, other):
    if (self.type == 'Fire' and other.type == 'Water') \
    or (self.type == 'Grass' and other.type == 'Fire') \
    or (self.type == 'Water' and other.type == 'Grass'):
      return True
    return False

  def list_moves(self):
      for move in moves:
          print(move.name, 'Pwr:', move.power, 'Acc:', move.accuracy, 'PP:', move.pp, '/'. move.max_pp)
