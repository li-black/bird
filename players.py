players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
my_foods=['pizza','falafel','carrot cake']
firend_foods=my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite food are:")
print(firend_foods)
my_foods=['pizza','falafel','carrot cake']
firend_foods=my_foods[:]
my_foods.append('cannoli')
firend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite food are:")
print(firend_foods)
