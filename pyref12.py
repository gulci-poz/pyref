# -*- coding: utf-8 -*-

items = [37, 42]
items.append(73)

print(dir(items))

# funkcje z __ implementują operacje języka, np __add__() implementuje +

# powiększa listę, ale nie zapisuje jej do items
items.__add__([101, 102])
items.append(101)
print(items)

# object to root dla wszystkich typów w py
# Stack dziedziczy z object
# pierwszy argument każdej metody to zawsze referencja do obiektu, domyślnie oznacza się go self
# wszystkie operacje na atrybutach muszą się odwoływać do self
# __metody specjalne
# __init__ inicjalizacja obiektu po jego utworzeniu

class Stack(object):
    def __init__(self):
        # tworzymy pusty atrybut, listę stack
        self.stack = []
    def push(self, object):
        # przekazujemy obiekt do dołączenia do listy za pomocą push
        self.stack.append(object)
    def pop(self):
        # pop wywala ostatni obiekt z listy i go zwraca
        return self.stack.pop()
    def length(self):
        # zwracamy długość listy
        return len(self.stack)

s = Stack()
s.push("gulci")
s.push(31)
s.push([1984, 1984, 2013, 2015])
s.push((6, 1, 1984))

# tak możemy jedynie wydrukować wartość samego obiektu
print(s)

data = []

# ściągamy elementy ze stosu i zapisujemy w liście, drukujemy bieżący element
while s.length() > 0:
    data.append(s.pop())
    print(data[len(data)-1])

# zniszczenie obiektu s
del s

print(data)

# stos na liście - ewentualna kontynuacja
