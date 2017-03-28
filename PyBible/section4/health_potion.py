import random   #import random mod

health = 50     #setting starting player health
difficulty = 1  # difficulty settting of game, easy1, medium2, hard3

potion_health = int(random.randint(25,50) / difficulty)
#giving health potion randomint; then dividing by difficulty harder the difff less health you get, and remove float

health = health + potion_health #taking current health then adding potion_health

print(health) #testing printing to make sure everthing works
