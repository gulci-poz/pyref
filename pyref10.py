# -*- coding: utf-8 -*-

# coroutines - funkcje, które działają jako zadania i operują na sekwencji argumentów do nich wysyłanych; funkcje są tworzone za pomocą wyrażenia yield

def print_matches(matchtext):
    print("Looking for:", matchtext)
    while True:
        # pobierz linię tekstu
        line = (yield)
        if matchtext in line:
            print(line)

matcher = print_matches("python")
# przechodzimy do pierwszego (yield)
matcher.__next__()
# yield zwraca zawartość linii do funkcji
# coroutine jest uśpiona do czasu wywołania send()
# potem przetwarzanie następuje do napotkania (yield), potem jest znów suspend
# i tak do napotkania close()
matcher.send("hello world")
matcher.send("python is cool")
matcher.close()
