def rzeczy(pierwsza_rzecz, *args):
    print(pierwsza_rzecz)
    print(args[0])
    for arg in args:
        print(arg)

rzeczy("lampa", "stolik", "drzewko", "telefon")

def dziennik(klasa, **kwargs):
    print("Klasa " + klasa)
    for nazwisko in kwargs.keys():
        print(nazwisko)
    print(kwargs.get("Kowalski"))

dziennik("3C", Kowalski='1', Nowak='2', Wisniewski='3')

def dziennik1(klasa='1C', **kwargs):
    print("Klasa " + klasa)
    for nazwisko in kwargs.keys():
        print(nazwisko)
    print(kwargs.get("Kowalski"))

dziennik1('3C', Kowalski='1', Nowak='2', Wisniewski='3')