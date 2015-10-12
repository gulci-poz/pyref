# -*- coding: utf-8 -*-

# generator to funkcja, która używa yield

# wersja dla py2

def countdown(n):
    print "Counting down!"
    while n > 0:
        # generuj wartość (n)
        yield n
        n -= 1

# dostajemy obiekt, który produkuje sekwencję rezultatów poprzez kolejne wywołania next(), __next__() w py3
# za każdym razem funkcja zwraca wartość przekazaną do yield i zawiesza wykonanie
count_from = countdown(10)

# obiekt generatora
print count_from

# next() nic nie wypisuje na ekranie
count_from.next()
count_from.next()
count_from.next()

# countdown kilka razy wywoła next i zbiór zwróconych wartości będzie wykorzystany w for
for i in countdown(5):
    print i,
