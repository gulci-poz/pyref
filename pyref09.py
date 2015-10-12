# -*- coding: utf-8 -*-

# tail -f, wypisanie końcowej części pliku, do tego pokazuje przyrosty pliku

import time

def tail(f):
    # pozycjonowanie relatywne od końca pliku - 2
    # offset - 0, czyli jesteśmy na EOF

    # ma sens z 1, absolutnie od początku pliku
    # ale po przeszukaniu pliku pętla będzie na zawsze w True, ale już nigdy nie zobaczy nowej linii, bo plik jest wczytany tylko raz
    f.seek(0, 2)
    while True:
        # w pętli czytamy kolejną linię pliku, jeśli jej nie ma, to czekamy na jej pojawienie się

        # nie będzie to działać, ponieważ musielibyśmy co chwilę aktualizować o twarty plik, a on zostal otwarty tylko raz

        # jak zrobić update pliku? to nie jest banalne, autor książki to olał
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

# implementacja grep

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line: yield line

# w yield chodzi o to, że zwraca każdą zadaną wartość
# wielokrotne zwracanie
# tail będzie cały czas wywoływał next i zwracał tę wartość do yield

# tail -f | grep py

tail_log = tail(open("out.txt"))
pylines = grep(tail_log, "py")

for line in pylines:
    print(line, end = '')
