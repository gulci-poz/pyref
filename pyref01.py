# -*- coding: utf-8 -*-
import sys

# użycie funkcji działa w py2, pod warunkiem, że drukujemy jeden element
# więcej elementów będzie drukowane jako tuple
print("Hello World!")

# w interactive py, zmienna _ przechowuje wynik ostatniej operacji

# w systemach unixowych można w razie czego uwzględnić ścieżkę do zmiennej środowiskowej #!/usr/bin/env python

# można wyjść z py shella podnosząc wyjątek raise SystemExit

principal = 1000
rate = 0.05
numyears = 5
year = 1

while year <= numyears:
    # zmiana wartości principal na float
    principal = principal * (1 + rate)

    # 3d justuje do prawej w trzech kolumnach, nie dodaje zer
    print("%3d %0.2f" % (year, principal))

    # bardziej nowoczesne podejście do formatowania, indywidualnie na wartość
    # format działa również w py2 ze starym print
    print(format(year, "3d"), format(principal, "0.2f"))

    # jest też metoda format() w stringu
    # pierwsza liczba - 0, 1 - to numer argumentu, druga liczba to format str
    print("{0:3d} {1:0.2f}".format(year, principal))

    year = year + 1

# w linii może być wiele instrukcji, trzeba je wtedy oddzielić średnikiem
# indentacja może mieć dowolną wielkość, ważne żeby była jednorodna w ramach jednego bloku

# else jest opcjonalny

a = 10
b = 20

if a < b:
    # nic nie robi, puste przejście
    pass
else:
    "No"

# w przypadku przełamania linii za pomocą \ możemy dowolnie wcinać ciąg dalszy w nowej linii

suffix = ".py"

if suffix == ".htm":
    content = "text/html"
elif suffix == ".jpg":
    content = "image/jpeg"
elif suffix == ".png":
    content = "image/png"
#else:
#    raise RuntimeError("Unknown content type")

# nie trzeba sprawdzać z if
s = "spam message"
has_spam = "spam" in s
print(has_spam)

f = open("pyref_def.txt")
line = f.readline()

while line:
    print(line, end = '')
    line = f.readline()
f.close()

# iteracja krócej

for line in open("pyref_def.txt"):
    print(line, end = '')

# można też użyć with

with open("pyref_def.txt") as f:
    print(f.read())

f = open("out.txt", "w")
year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    #print >> f, "%3d %0.2f" % (year, principal)
    #f.write("%3d %0.2f\n" % (year, principal))
    print("%3d %0.2f" % (year, principal), file = f)
    year = year + 1
f.close()

sys.stdout.write("Enter your name:\n")
# trzeba dać \n, inaczej wypisanie tekstu nastąpi później
name = sys.stdin.readline()
print(name)

# to samo daje nam raw_input() i input()
# można też przedefiniować sys.stdin i sys.stdout
# sys.stdin =
# sys.stdout =
