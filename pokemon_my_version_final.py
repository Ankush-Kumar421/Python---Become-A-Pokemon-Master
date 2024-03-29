class Pokemon:
  """ To create a pokemon, give it a name, type, and level. Its max health is 
  equal to its level. Its starting health is equal to the max health. Also, the 
  pokemon is not knocked out."""
  def __init__(self, name, type, level=5):
    self.name = name
    self.level = level
    self.type = type
    self.max_health = level * 5
    self.health = level * 5
    self.is_knocked_out = False

  def __repr__(self):
    """Printing a pokemon will tell you its name, its type, its level, and how 
    much health it has remaining."""
    return f"This level {self.level} {self.name} has {self.health} hit points"\
             + f" remaining. It's a {self.type} type Pokemon."

  def lose_health(self, damage):
    # Decrease health from a pokemon and prints the current health remaining.
    self.health -= damage
    if self.health > 0:
      #If pokemon has health greater than 0 after being damaged, then 
      #print out current health.
      self.health - damage
      print(f"{self.name} now has {self.health} health remaining.")
    else:
      #If pokemon health becomes 0 or less, then set health to 0 and knock out 
      #the pokemon. 
      self.health = 0
      self.knocked_out()
    
  def gain_health(self, amount):
    # Increase a pokemon's health when a potion is used. Then print the current 
    # health remaining.
    # Check to see if the pokemon health is 0.
    if self.health == 0:
      print(f"{self.name} can't heal because it is knocked out!")
    else:
      health_before_potion = self.health
      self.health += amount
      # Make sure the health does not go over the max health. Health gained is 
      # equal to the difference between max health and health before the use of 
      # the potion.
      if self.health > self.max_health:
        self.health = self.max_health
        gained_health = self.max_health - health_before_potion
        print(f"{self.name} gained {gained_health} health.")
        print(f"{self.name} now has {self.health} health.")
      else:
        # If health increased is below max health, then health gained is equal 
        # to the value of the potion. 
        print(f"{self.name} gained {amount} health.")
        print(f"{self.name} now has {self.health} health.")

  def knocked_out(self):
    #If the pokemon was knocked out, then set the status to True.
    self.is_knocked_out = True
    # A knocked out pokemon should not have any health. We check to see if the 
    # knocked out pokemon health is set to 0. If its not, then we set it 
    # to zero. This is just a safety precaution. 
    if self.health != 0:
      self.health = 0
    print(f"{self.name} was knocked out!")

  def revive(self):   
    """If the pokemon health is 0 and the player uses the revival potion, then 
    increase the pokemon's health by half of its max health. Also, change the 
    status of the pokemon "knocked out" to False.""" 
    if self.health == 0:
      self.health += round(self.max_health / 2)
      self.is_knocked_out = False
    print(f"{self.name} has revived.")

  def attack(self, other_pokemon):
    """Pokemon attacks and deals damage to another pokemon. The other pokemon 
    loses health."""
    damage = 0
    # Check to make sure the pokemon isn't knocked out.
    if self.is_knocked_out == True:
      print(f"{self.name} can't attack because it is knocked out!")
    # If the attacking pokemon has an advantage over the other pokemon, then 
    # it deals damage equal to twice the attacking pokemon's level.
    elif (self.type == "Fire" and other_pokemon.type == "Grass") or \
          (self.type == "Water" and other_pokemon.type == "Fire") or \
          (self.type == "Grass" and other_pokemon.type == "Water"):
      damage += 2 * self.level
      print(f"{self.name} attacked {other_pokemon.name} for {damage} damage.")
      print("It's super effective!")
      other_pokemon.lose_health(damage)
      # If the attacking pokemon has a disadvantange, then it deals damage 
      # equal to half the attacking pokemon level.
    elif (self.type == "Grass" and other_pokemon.type == "Fire") or \
        (self.type == "Fire" and other_pokemon.type == "Water") or \
        (self.type == "Water" and other_pokemon.type == "Grass"):
      damage += round(0.5 * self.level)      
      print(f"{self.name} attacked {other_pokemon.name} for {damage} damage.")
      print("It's not very effective...")
      other_pokemon.lose_health(damage)
    # If the attacking pokemon has neither advantange or disadvantage, then it 
    # deals damage equal to its level to the other pokemon. 
    else:
      damage += self.level
      print(f"{self.name} attacked {other_pokemon.name} for {damage} damage.")
      other_pokemon.lose_health(damage)

# Testing attacking, losing health.    
attacking_pokemon = Pokemon("Charmander", "Fire", 2)
other_pokemon = Pokemon("Bulbasaur", "Grass", 4)
attacking_pokemon.attack(other_pokemon)
print(other_pokemon.health)
other_pokemon.lose_health(4)
print(other_pokemon)

print()
#Testing gaining health
other_pokemon.gain_health(80) 
print(other_pokemon)

# Three classes that are subclasses of Pokemon. Charmander is a fire type, 
# Squirtle is a water type, and Bulbasaur is a grass type. 
class Charmander(Pokemon):
  def __init__(self, level=5):
    super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
  def __init__(self, level=5):
    super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
  def __init__(self, level=5):
    super().__init__("Bulbasaur", "Grass", level)
  

class Trainer:
  """ To create a trainer, give it a list of pokemon, a number of potions on 
  hand, and a name. Also, when the trainer is created, the first pokemon in 
  their list of pokemon is considered an active pokemon which is the index 0 
  in the list."""
  def __init__(self, pokemon_list, num_potions, num_revivals, name):
    self.pokemons = pokemon_list
    self.potions = num_potions
    self.revival_potions = num_revivals
    self.current_pokemon = 0
    self.name = name

  def __repr__(self):
    # Prints the name of the trainer, the pokemon they currently have, and the 
    # current active pokemon.
    print(f"The trainer {self.name} has the following pokemon:")
    for pokemon in self.pokemons:
      print(pokemon)
    return f"The current active pokemon is " \
          + f"{self.pokemons[self.current_pokemon].name}."
    

  def use_potion(self):
    # The trainer uses a potion on the active pokemon, assuming the trainer 
    # has at least one potion on hand. 
    if self.potions > 0:
      self.potions -= 1
      print(f"You used a potion on {self.pokemons[self.current_pokemon].name}.")
      self.pokemons[self.current_pokemon].gain_health(20)      
    else:
      print("You don't have any more potions.")

  def attack_other_trainer(self, other_trainer):
    # Your current pokemon attacks the other trainer's current pokemon
    my_pokemon = self.pokemons[self.current_pokemon]
    their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
    my_pokemon.attack(their_pokemon)

  def use_revival_potion(self):
    # The trainer uses a revival potion on a knocked out pokemon, assuming the 
    # trainer has at least one potion on hand.
    if self.revival_potions > 0:
      self.revival_potions -= 1
      print(f"You used a revival potion on "\
            + f"{self.pokemons[self.current_pokemon].name}.")
      self.pokemons[self.current_pokemon].revive()      
    else:
      print("You don't have any more revival potions.")
    
    
  def switch_active_pokemon(self, new_active):
    """Switches the active pokemon to the number given as a parameter."""
    # First check to see the number is valid (between 0 and 
    # the length of the list). 
    if new_active < len(self.pokemons) and new_active >= 0:
      # You can't switch to a pokemon that is knocked out
      if self.pokemons[new_active].is_knocked_out:
        print(f"{self.pokemons[new_active].name} is knocked out. You can't "
            "make it your active pokemon.")
      # You also can't switch to your current pokemon
      elif new_active == self.current_pokemon:
        print(f"{self.pokemons[new_active].name} is already your active "
              "pokemon.")
      else:
        # Switches the pokemon.
        self.current_pokemon = new_active
        print(f"{self.pokemons[new_active].name} it's your turn!")

# Six pokemons are made with different levels. If no level is given, 
# its default level is 5.
a = Charmander(7)
b = Squirtle()
c = Squirtle(1)
d = Bulbasaur(10)
e = Charmander()
f = Squirtle(2)


# Two trainers are created. The first three pokemon are given to trainer 1, 
# the second three are given to trainer 2. 
trainer_one = Trainer([a, b, c], 2, 2, "Alex")  
trainer_two = Trainer([d, e, f], 3, 1, "Ash")

print()
print(trainer_one)
print()
print(trainer_two)
print()

# Testing attacking, giving potions, and switching pokemon.
trainer_one.attack_other_trainer(trainer_two)
print()
trainer_two.attack_other_trainer(trainer_one)
print()
trainer_two.use_potion()
print()
print(trainer_two.potions) # Testing to see if the number of potions remaining 
# on hand also decreased. 
print()
trainer_one.attack_other_trainer(trainer_two)
print()
trainer_two.switch_active_pokemon(0)
trainer_two.switch_active_pokemon(1)
print()

#Testing pokemon cannot health past its maximum health, a pokemon cannot attack 
# if its knocked out, cannot switch to a pokemon that is knocked out
trainer_two.switch_active_pokemon(0)
trainer_one.attack_other_trainer(trainer_two)
trainer_one.attack_other_trainer(trainer_two)
trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one) # Knocked out Pokemon 
# cannot attack.
trainer_two.switch_active_pokemon(1)
trainer_two.switch_active_pokemon(0)
#trainer_two.use_potion() # Can't heal a knocked out pokemon. 
#trainer_two.use_revival_potion()
#print(trainer_two.revival_potions)













  




