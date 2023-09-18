imie = "Anna"
nazwisko = "Lisek 'Nowak'"
adres = "Warszawa"

print(nazwisko)
print('Czytam książke "Gdzie jest Nemo"')
print('\\Czytam \t książke \n \"Gdzie jest Nemo\"')

print("male litery".upper())
print("DUZE LITERY".lower())
print(imie.islower())
print(nazwisko.isupper())


for char in "Bartek":
    print(char)

print(imie[0])
print(imie[0:4])
print(imie.index("a"))
print("Ala" in "Ala ma kota")
print("Alka" not in "Ala ma kota")

print(" ".join(["Ala", "ma", "kota"]))
print("Ala,ma,kota,i,psa".split(","))
print(imie.startswith("A"))
print(imie.endswith("la"))