# -*- coding: utf-8 -*-

# zbiory są nieuporządkowane, elementy nie powtarzają się, elementy nie są indeksowane

s = set([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
t = set("Hello")

print(s)
print(t)

# unia
print(t | s)

# intersekcja, w tym przypadku zwraca pusty zbiór set()
print(t & s)

# różnica
print(t - s)

# różnica symetryczna, elementy z t i s, ale nie jednocześnie w obu
print(t ^ s)

# dodaje cały string, a nie poszczególne elementy osobno
t.add("world")
t.add('x')
print(t)

# nie powtarza dublowanych elementów
s.update([17, 19, 21, 23, 25, 27, 29])
print(s)

t.remove("world")
print(t)

# pusty zbiór
empty = set()
print(empty)

# słownik to tak naprwdę tablica asocjacyjna
stock = {
    "name":"GOOG",
    "shares":100,
    "price":490.10
}

# uzyskanie danych
name = stock["name"]
value = stock["shares"] * stock["price"]

# aktualizacja i dodanie danych
stock["shares"] = 75
stock["date"] = "October 10, 2013"

print(stock)

# można indeksować po liczbach i tuples, nie można po listach i słownikach (zmienna zawartość)

# pusty słownik
prices = {}
prices = dict()

# szybki lookup po nieuporządkowanych danych
prices = {
    "GOOGL" : 490.10,
    "AAPL" : 123.50,
    "IBM" : 91.50,
    "MSFT" : 52.13
}

# przynależność do słownika
if "SCOX" in prices:
    p = prices["SCOX"]
else:
    p = 0.0

# krótsza metoda sprawdzenia i przypisania
p = prices.get("SCOX", 0.0)

# usunięcie elementu
del prices["IBM"]

# uzyskanie kluczy
syms = list(prices)
print(syms)

# inny sposób na listę kluczy i wartości
keys = list(prices.keys())
values = list(prices.values())

print(keys)
print(values)
