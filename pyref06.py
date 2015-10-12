# -*- coding: utf-8 -*-

def remainder(a, b):
    # truncating division, ilość wystąpień b w a, zostaje reszta modulo - r
    q = a // b
    r = a - q * b
    return r

result = remainder(35, 15)
print(result)

def divide(a, b):
    q = a // b
    r = a - q * b
    return(q, r)

quotient, rem = divide(35, 15)
print("quotient %d, remainder %d" % (quotient, rem))

# domyślna wartość argumentu
def connect(hostname, port, timeout = 300):
    print(hostname, port, timeout)

# przy wywołaniu argument domyślny może zostać pominięty
connect('www.python.org', 80)
connect('www.learnpythonthehardway.com', 8080, 500)

# można też użyć nazw argumentów i podawać je w dowolnej kolejności
connect(port = 80, hostname = 'www.nasa.com')

# zmienne utworzone wewnątrz funkcji maja zasięg lokalny

count = 0

# istnieje możliwość zmiany wartości globalnej zmiennej wewnątrz funkcji

def foo():
    global count
    count += 1

foo()
print("count %d" % count)
