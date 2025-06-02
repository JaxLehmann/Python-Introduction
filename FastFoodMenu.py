food_array = [
  'Cheeseburger',
  'Fries',
  'Soda',
  'Ice Cream',
  'Cookie'
]
def get_item(int):
  if int == 1:
    return 'Cheeseburger'
  elif int == 2:
    return 'Fries'
  elif int == 3:
    return 'Soda'
  elif int == 4:
    return 'Ice Cream'
  elif int == 5:
    return 'Cookie'
  else:
    return 'That item does not exist'

def welcome():
  print('Welcome to Jax\'s Diner!')
  print('Here\'s the menu:')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')

welcome()

option = int(input('What would you like to order? '))
print(get_item(option))