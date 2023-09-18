class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "Nazywam się: " + self.imie + self.nazwisko

class Student(Osoba):

    def __init__(self, imie, nazwisko, numer_indeksu):
        Osoba.__init__(self,imie,nazwisko)
        self.indeks = numer_indeksu

    def podaj_nr_indeksu(self):
        return self.indeks

    def przedstaw_sie(self):
        return "Jestem studentem pierwszego roku i mam na imie " + self.imie

student = Student("Paula", "Lisek", 12445)
print(student.przedstaw_sie())
print(student.podaj_nr_indeksu())

