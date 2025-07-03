warriors_roster = [
  {'name': 'Steph Curry', 'position': 'PG', 'Jersey Number': 30},
  {'name': 'Klay Thompson', 'position': 'SG', 'Jersey Number': 31},
  {'name': 'Draymond Green', 'position': 'PF', 'Jersey Number': 23},
  {'name': 'Andrew Bogut', 'position': 'C', 'Jersey Number': 12},
  {'name': 'Harrison Barnes', 'position': 'SF', 'Jersey Number': 40}
]

for player in warriors_roster:
  print (player['position'])

for player in warriors_roster:
  if player['Jersey Number'] == 30:
    player['Points per game'] = 32.5

for player in warriors_roster:
  if player['Jersey Number'] == 30:
    print (player['Points per game'])
  
for player in warriors_roster:
  if player['name'] == 'Draymond Green':
    player ['Total Points'] = 230
    player ['Games Played'] = 79
  if player['name'] == 'Steph Curry':
    player ['Total Points'] = 383
    player ['Games Played'] = 26
  if player ['name'] == 'Andrew Bogut':
    player ['Total Points'] = 136
    player ['Games Played'] = 12
  if player ['name'] == 'Klay Thompson':
    player ['Total Points'] = 826
    player ['Games Played'] = 66
  if player ['name'] == 'Harrison Barnes':
    player ['Total Points'] = 749
    player ['Games Played'] = 81

for player in warriors_roster:
  player ['Avg Points'] = player ['Total Points'] / player ['Games Played']

for player in warriors_roster:
  print(f"{player['name']} {player['Avg Points']:.2f}")