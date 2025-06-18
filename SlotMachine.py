# Write code below 💖
import random

symbols = ['🍒', '🍇', '🍉', '🍊', '🍋', '🍋‍🟩', '7️⃣']

while True:

  results = random.choices(symbols, k = 3)

  print(results[0] + " | " + results[1] + " | " + results[2])

  if results[0] == results[1] and results[1] == results[2] and results[0] == '7️⃣':
    print("Jackpot! 💰")
  else:
    print("You have lost. Thanks for playing!")
  user_input = input("Would you like to keep playing? Answer Y or N: ")
  print (user_input)

  if user_input.lower() == "n":
    print("Goodbye")
    break