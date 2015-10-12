# -*- coding: utf-8 -*-

import sys

# string to indeksowana od zera sekwencja znaków

hello = "Hello gulci!"

# przedział zamknięty-otwarty
# jeśli brakuje elementów, to zakładamy, że chodzi o początek lub koniec
print(hello[0:4])
print(hello[:5])
print(hello[5:])

# py nigdy nie próbuje interpretować zawartości stringa jako int
print("19" + "84")
print(int("19") + int("84"))

born = 1984
print("str", str(born))
print("repr, dokładna wartość obiektu", repr(born))
print("format", format(born, "4d"))

num3point4 = 3.4
# float podwójnej precyzji nie potrafi dokładnie zapisać ułamka o podstawie dziesiętnej, tutaj się to udało

print("str", str(num3point4))
print("repr", repr(num3point4))
print("format", format(num3point4, "0.5f"))

# listy są indeksowa całkowicie, od zera
# pusta lista
#names = []
#names = list()
names = ["John", "Barbara", "Josef", "Henry", "Bron"]
a = names[1]
names[4] = "Bronislaw"
names.append("Sebastian")
names.insert(0, "Caroline")
print(names)
b = names[0:2]
c = names[:3]
d = names[3:]
names[0:2] = ["Ursula", "Victoria", "Melanie"]
print(b)
print(c)
print(d)
print(names)
nums = [1, 2, 3] + [4, 5]
print(nums)

lists = [1, "gulci", 3.14, ["gulci", 8, 6, [101, 102]], 15]
print(lists[1])
print(lists[3][2])
print(lists[3][3][1])

if len(sys.argv) != 2:
    print("Please supply a filename")
    raise SystemExit(1)

f = open(sys.argv[1])
# wczytujemy wszystkie linie do listy
lines = f.readlines()
f.close()

# list comprehension
fvalues = [float(line) for line in lines]
print("min", min(fvalues))
print("max", max(fvalues))

# możemy skrócić program do postaci
fvalues = [float(line) for line in open(sys.argv[1])]
print(fvalues)
