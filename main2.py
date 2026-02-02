# Create player data
player_data = [
  {'name': "Patrick Mahomes", 'position': "Quarterback", 'jersey': "15"},
  {'name': "Tyreek Hill", 'position': "Wide Receiver", 'jersey': "10"},
  {'name': "Travis Kelce", 'position': "Tight End", 'jersey': "87"}
]

#Print list of all positions
for p in player_data:
  print(p['position'])

#Update a players game stats
pmahomes = player_data[0]
print(pmahomes['name'])