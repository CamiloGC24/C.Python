PAISES = 14
DATOS = 6
paises = [ "Costa Rica", "Argentina", "Panamá", "Chile", "Uruguay",
    "Paraguay", "Colombia", "Perú", "Ecuador","Bolivia","Brasil",
    "México","Nicaragua","Venezuela"]
datos = [ [2290, 569, 4 , 300255, 527.7, 131],  [75, 22.8, 3.3, 9500, 416.7, 127],
          [5.9, 1, 5.9, 744, 744, 126], [2600, 634, 4.1, 276000, 435.3, 106],
          [140, 30.8, 4.5, 13430, 436, 96],[26542, 5601,4.7, 2200000, 392.8, 83],
          [10900, 2964, 3.7, 869453, 293.3, 80], [11.5, 3.3, 3.5, 850, 257.6, 74],
          [5.5, 1, 5.5, 386, 386, 70], [34, 7, 4.9, 2000, 287.4, 59],
          [16.5, 3.6, 4.6, 965, 268.1, 58], [48, 19.6, 2.5, 2687, 137.2, 56],
          [168, 31.3, 5.4, 8445, 269.6, 50], [168000, 690854, 0.2, 1308000, 1.9, 8]]

print(f"\n{paises}")
pais = input(f"\n Introdue un pais de la lista: ")
if pais in paises:
    pos = paises.index(pais)
    print(f"\n Parte 1: {pais}", end = ":")
    for x in range(len(datos[pos])):
        if x == len(datos[pos])-1:
            print(datos[pos][x],"\n")
        else:
            print(datos[pos][x],end=", ")

count = 0

for i in range(len(datos)):
    count += datos[i][5]

print(f"El numero total de bigMacs en america Latina: {count}\n")

print(f"Los países que superan los 100 son", end = ".")
for i in range(len(datos)):
    if datos[i][5] > 100:
        print(f"{paises[i]}", end = " ")
print("\n")