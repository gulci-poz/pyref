# -*- coding: utf-8 -*-

for n in range(1, 10):
    print("%d do potęgi 2 to %d" % (n, n**2))

for n in range(100, 0, -5):
    print("%d do potęgi 2 to %d" % (n, n**2))

# w py2 dla bardzo dużych list używa się xrange(), np. xrange(100000000)
# w przypadku xrange() wartości są tworzone na żądanie
# w py3 range() robi to, co xrange() w py2; stara funkcjonalność range() została usunięta

# możemy również iterować po stringach, listach, słownikach i liniach pliku

a = "Hello World"
for c in a:
    print(c)

b = ["Dave", "Mark", "Ann", "Phil"]
for name in b:
    print(name)

c = {'GOOG' : 490.10, 'IBM' : 91.50, 'AAPL' : 123.15}
for key in c:
    print(key, c[key])

f = open("portfolio.csv")
for line in f:
    print(line, end = '')
