dziennik = {1:"Kowalski", 2:"Nowak", 3:"Lisek"}

print(dziennik.get(1))
print(dziennik[1])
dziennik[4] = "Mucha"
print(dziennik[4])

for key in dziennik.keys():
    print(key)

for value in dziennik.values():
    print(value)

del dziennik[1]

for value in dziennik.values():
    print(value)

dziennik[2] = "Nowy uczen"
print("Nowy uczen to " + dziennik[2])
