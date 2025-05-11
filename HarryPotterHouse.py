# Write code below 💖

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print(" 1) Dusk")
print(" 2) Dawn")
answer1 = int(input("Do you like Dawn or Dusk? "))

if answer1 == 1:
    Ravenclaw += 1
    Gryffindor += 1
elif answer1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input")

print(" 1) The Good")
print(" 2) The Great")
print(" 3) The Wise")
print(" 4) The Bold")
answer2 = int(input("When I'm dead, I want people to remember me as: "))

if answer2 == 1:
    Hufflepuff += 2
elif answer2 == 2:
    Slytherin += 2
elif answer2 == 3:
    Ravenclaw += 3
elif answer2 == 4:
    Gryffindor += 2
else:
    print("Wrong input")

print(" 1) Violin")
print(" 2) Drums")
print(" 3) Piano")
print(" 4) Trumpet")
answer3 = int(input("Which kind of instrument most pleases your ear? "))

if answer3 == 1:
    Slytherin += 2
elif answer3 == 2:
    Hufflepuff += 4
elif answer3 == 3:
    Ravenclaw += 4
elif answer3 == 4:
    Gryffindor += 4
else:
    print("Wrong input")

print('Hufflepuff Score:', Hufflepuff)
print('Slytherin Score:', Slytherin)
print('Ravenclaw Score:', Ravenclaw)
print('Gryffindor Score:', Gryffindor)

house_scores = {
  "Hufflepuff": Hufflepuff,
  "Slytherin": Slytherin,
  "Ravenclaw" : Ravenclaw,
  "Gryffindor" : Gryffindor
}
winner = max(house_scores, key = house_scores.get)
print ("You belong in... " + winner + "!")