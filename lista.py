imiona = ["Bartek", "Anna", "Ola", "Andrzej", 1 , 3 ,6]
print(imiona[0])
print(imiona[3])
print(imiona[0:2])
print(imiona.index("Bartek"))
imiona.append("Olek")
imiona.insert(0, "Zuzka")
print(imiona)
print(len(imiona))
imiona.remove("Anna")
del imiona[0]
print(imiona)

pierwsza_lista = ["lampa", "koc", "wiadro"]
druga_lista = ["auto", "lot", 1,2,3]
print(pierwsza_lista*3)
print(pierwsza_lista + druga_lista)
pierwsza_lista.sort()

koc,lampa,krzeslo = pierwsza_lista
print(koc)
print(lampa)
print(krzeslo)
