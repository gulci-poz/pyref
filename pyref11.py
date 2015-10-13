# -*- coding: utf-8 -*-

# konsument-coroutines / producent-generator
matchers = [
    print_matches("python")
    print_matches("guido")
    print_matches("jython")
]

# przygotowania wszystkich ko-rutyn
for m in matchers:
    m.__next__()

# potrzebujemy działającego serwera www, który będzie pisał do loga
wwwlog = tail(open("access-log"))

for line in wwwlog:
    for m in matchers:
        # wysyłamy linię do każdego matchera (ko-rutyny)
        m.send(line)
