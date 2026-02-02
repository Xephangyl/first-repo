gpoints = 0
rpoints = 0
hpoints = 0
spoints = 0

print('Q1) Do you like Dawn or Dusk?')
print('   1) Dawn')
print('   2) Dusk')

answer = int(input())

if answer == 1:
  gpoints += 1
  rpoints += 1
elif answer == 2:
  hpoints += 1
  spoints += 1
else:
  print('Wrong Input')


print("Q2) When I'm dead, I want people to remember me as: ")
print('   1) The Good')
print('   2) The Great')
print('   3) The Wise')
print('   4) The Bold')

answer = int(input())

if answer == 1:
  hpoints += 2
elif answer == 2:
  spoints += 2
elif answer == 3:
  rpoints += 2
elif answer == 4:
  gpoints += 2
else:
  print('Wrong Input')

print('Q3) Which kind of instrument most pleases your ear?')
print('   1) The violin')
print('   2) The trumpet')
print('   3) The piano')
print('   4) The drums')

answer = int(input())

if answer == 1:
  spoints += 4
elif answer == 2:
  hpoints += 4
elif answer == 3:
  rpoints += 4
elif answer == 4:
  gpoints += 4
else:
  print('Wrong Input')


print('Gryffindor: ' + str(gpoints))
print('Ravenclaw: ' + str(rpoints))
print('Hufflepuff: ' + str(hpoints))
print('Slytherin: ' + str(spoints))

if gpoints > rpoints and gpoints > hpoints and gpoints > spoints:
  print('Gryffindor is the winner!')
elif rpoints > hpoints and rpoints > spoints:
  print('Ravenclaw is the winner!')
elif hpoints > spoints:
  print('Hufflepuff is the winner!')
else:
  print('Slytherin is the winner!')
