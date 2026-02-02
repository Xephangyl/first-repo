class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

gates_bbq = Restaurant()
gates_bbq.name = 'Gates Bar-B-Q'
gates_bbq.category = 'Barbecue Restaurant'
gates_bbq.rating = 4.0
gates_bbq.delivery = True

niecies = Restaurant()
niecies.name = 'Niece\'s Restaurant'
niecies.category = 'Family Restaurant'
niecies.rating = 4.4
niecies.delivery = False

print(vars(bobs_burgers))
print(vars(gates_bbq))
print(vars(niecies))