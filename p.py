import json

#this is the file where i stor the informations 
#pokeomon Class that contains the name,photo of front and back and health, skill
class Pokemon:
    def __init__(self, name, backPhoto,skill,frontPhoto,health):
        self.name = name
        self.backPhoto  = backPhoto 
        self.skill = skill
        self.frontPhoto = frontPhoto
        self.health = health
    def reset(self, buf):
        name = buf.name
        health = buf.health
    #     # Pokemon.mySkill

    # def take_damage(self, damage):
    #     self.hp -= damage

    # def is_alive(self):
    #     return self.hp > 0
#start with this global variables 
control = -1
badgeCollect = set()
name = "Pikachu"
health= 100
#have 6 differnt pokemons 
Bulbasaur = Pokemon("Bulbasaur","Bulbasaur_back.png",["Growl","Tackle","Vine Whip","Leech Seed"],"Bulbasaur_Front.png",100)
Charmander = Pokemon("Charmander","Charmander_back.png",["Scratch","Growl","Ember","Dragon Breath"],"Charmander_Front.png",100)
Squirtle = Pokemon("Squirtle","Squirtle_back.png",["Tackle","Tail Whip","Water Gun","Bite"],"Squirtle_Front.png",100)
Pikachu = Pokemon("Pikachu","Pikachu_back.png",["Tackle","Electro Ball","ThunderBolt","Bite"],"Pikachu_Front.png",100)
Gyarados = Pokemon("Gyarados","Gyarados_back.png",["Water Gun","Scratch","ThunderBolt","Dragon Breath"],"Gyarados_Front.png",100)
Onix = Pokemon("Onix","Onix_back.png",["Growl","Tackle","Bite","Scratch"],"Onix_Front.png",100)

#the defauls value of the chosne pk is Pikachu
pokemonChosen = Pikachu


#def getName(variable):
    #for name, value in locals().items():
     #   if value is variable:
      #      return name
    #return None
# def getName(variable, namespace):
#     l = [name for name, value in namespace.items() if value is variable]
#     for i in l:
#         if i != None:
#             return i


# loaded_data = {
#     getName(control, globals()) : control,
#     "Pokemon.name" : name,
#     getName(health, globals()) : health
# }


# def saveData(l = [control, health], strl = [name]):
#     for i in l:
#         loaded_data[getName(i, globals())] = i    
#     loaded_data["Pokemon.name"] = strl    
#     with open('data.json', 'w') as file:
#          json.dump(loaded_data, file)


# # x = 10
# # print(get_var_name(x, globals()))  # ['x']

# def loadtedData():
#     global control
#     global name
#     global health
#     with open('data.json', 'r') as file:
#         loaded_data = json.load(file)
#     if loaded_data != None:
#         control = loaded_data["control"]
#         name = loaded_data["Pokemon.name"]
#         health = loaded_data["health"]
#     else:
#         control = -1
#         name = "Pikachu"
#         health = 100

