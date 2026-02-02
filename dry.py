# 💿 Music Library

artist = ''
album = ''

albums = ['Good Kid, Mad City - Kendrick Lamar',
          'The Carter IV - Lil Wayne'
         ]

print('+++++++++++++++++++')
print('Xephy Music')
print('+++++++++++++++++++\n')

for i in albums:
  print(f'{albums.index(i)}) {i}')

print('\n+++++++++++++++++++\n')

print(f'You have {len(albums)} albums in your library.')
answer = input('Would you like to add an album?: ')

while (answer == 'Y'):
  artist = str(input('Please enter the name of the artist: \n'))
  album = str(input('Please enter the name of the album: \n'))
  albums.append(f'{artist} - {album}')
  for i in albums:
    print(f'{albums.index(i)}) {i}')
  print('\n+++++++++++++++++++\n')
  answer = input('Would you like to add another album?: ')