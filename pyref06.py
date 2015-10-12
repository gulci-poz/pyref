# -*- coding: utf-8 -*-

def remainder(a, b):
    # truncating division, ilosć wystąpień b w a, zostaje reszta modulo
    q = a // b
    r = a - q * b
    return r

result = remainder(35, 15)
print(result)
