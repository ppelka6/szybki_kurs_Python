pierwszy_zbior = {"Warszawa", "Krakow", "Katowice", "Łódź"}
drugi_zbior = {"Warszawa"}

pierwszy_zbior.add("Kielce")
print(pierwszy_zbior)
pierwszy_zbior.add("Łódź")
print(pierwszy_zbior)

print(pierwszy_zbior - drugi_zbior)
print(pierwszy_zbior | drugi_zbior)
print(pierwszy_zbior & drugi_zbior)
print(pierwszy_zbior ^ drugi_zbior)

