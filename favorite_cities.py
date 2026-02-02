class City:
  def __init__(self, name, country, population, landmarks, currency, founded, mayor):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.currency = currency
    self.founded = founded
    self.mayor = mayor

kc = City('Kansas City', 'United States', 510704, 'American Jazz Museum', 'USD', 1850, 'Quinton Lucas')
tokyo = City('Tokyo', 'Japan', 14180000, 'Meiji Shinto Shrine', 'Yen', 1889, 'Yuriko Koike')

print(vars(kc))
print(vars(tokyo))