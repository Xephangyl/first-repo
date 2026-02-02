stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  day = x - 1
  return stock_prices[day]

def max_price(a, b):
  daya = a - 1
  dayb = b - 1
  return max(stock_prices[daya], stock_prices[dayb])

def min_price(a, b):
  daya = a - 1
  dayb = b - 1
  return min(stock_prices[daya], stock_prices[dayb])

print(price_at(1))  #finds the price on a given day x
print(max_price(3, 6))  #finds the maximum price from day a to day b
print(min_price(1, 2))  #finds the minimum price from day a to day b