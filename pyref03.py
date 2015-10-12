# -*- coding: utf-8 -*-

# tuple - kolekcja danych
person = ("first_name", "last_name", "phone")

# notacja bez nawiasów
python_ver = "2.7.10", "3.5.0"

# pusty tuple
a = ()

# jednoelementowy tuple
b = ("b",)

# jednoelementowy tuple
c = "c",

# możemy się dostać do tuple po indeksie; działa też slicing i konkatenacja
print(person[1])

# unpacking
first_name, last_name, phone = person

# nie można modyfikować tuple; obiekt złożony z części

# dla poprawienia wydajności listy alokują więcej pamięci
# oszczędzamy pamięć korzystając z tuple dla list mniejszych niż kilkanaście elementów (dozen)

filename = "portfolio.csv"
portfolio = []

for line in open(filename):
    fields = line.split(",")
    #name = fields[0]
    #shares = int(fields[1])
    #price = float(fields[2])
    #stock = (name, shares, price)
    stock = (fields[0], int(fields[1]), float(fields[2]))
    portfolio.append(stock)

print(portfolio)

total = 0.0

for name, shares, price in portfolio:
    total += shares * price

print("Total worth of shares:", total)
