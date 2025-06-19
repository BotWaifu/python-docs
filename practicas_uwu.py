name = "Lopen"
level = 25
character_class = "Windrunner"
armor = 12.4
magic_resistance = 15
account_active = True

print ("Character Report")
print (f"{name} is a level {level} {character_class}.")
print(f"They have {armor} armor and {magic_resistance} magic resistance.")
print (f"Their account is currently active: {account_active}")

#Don´t edit below this line

print("============================================")
print("Character Report Complete")
print("Data types:")
print(f"name:{type(name).__name__},character_class:{type(character_class).__name__}")
print(f"armor:{type(armor).__name__},magic_resistance:{type(magic_resistance).__name__}")
print(f"account_active:{type(account_active).__name__}")

#calcular el promedio de los cuatros numeros en la variable e imprimir el promedio redondeado

game_one_score = 97
game_two_score= 92
game_three_score= 106
game_four_score= 105

#Don´t touch above this line

average_score = round((game_one_score + game_two_score + game_three_score + game_four_score) / 4)

print (average_score)

