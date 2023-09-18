class Pies:

    gatunek = 'pies domowy'

    def __init__(self,rasa,imie,wiek):
        print("Metoda init")
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):
        return "Hau hau"

    def zaprezentuj_psa(self):
        print("Rasa to: " + self.rasa)
        print("Imie to: " + self.imie)
        print("Wiek psa to: " + str(self.wiek))

reksio = Pies("kundelek", "Ares", "2")
print(reksio.wiek)
print(reksio.rasa)
print(reksio.imie)
print(Pies.gatunek)
reksio.wiek = 6
print(reksio.wiek)
Pies.gatunek = "Ptak"
print(reksio.gatunek)
print(reksio.szczekaj())
print(reksio.zaprezentuj_psa())