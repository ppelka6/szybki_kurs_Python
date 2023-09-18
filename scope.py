imie = "Paula"
nazwisko = "Nowak"

def przedstaw_sie():
    global nazwisko
    nazwisko = "Kowal"
    print(nazwisko)
    print(imie)


print(imie)
print(nazwisko)
przedstaw_sie()
print(nazwisko)
