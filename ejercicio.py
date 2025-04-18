""""
Supóngase que en una reciente elección hubo cuatro candidatos, con identificadores 1, 2, 3, 4. 
Usted habrá de encontrar mediante un programa, el número de votos correspondiente a cada candidato y el porcentaje que obtuvo respecto al total de los votantes. 
El usuario ingresara los votos de manera desorganizada, tal y como se obtuvieron en la elección, el final de datos está representado por un cero.
Observe, como ejemplo, la siguiente lista.: 1 3 1 4 2 2 1 3 1 1 1 3 4 1 2 4 4 0, osea que no importa la cantidad de votos con tal que al ingresar 0 al final 
"""
# Contadores para los votos de cada candidato
votos1 = 0
votos2 = 0
votos3 = 0
votos4 = 0

print("Ingresa los votos (1, 2, 3 o 4). Escribe 0 para terminar.")

# Ciclo para leer votos
voto = int(input("Voto: "))
while voto != 0:
    if voto == 1:
        votos1 += 1
    elif voto == 2:
        votos2 += 1
    elif voto == 3:
        votos3 += 1
    elif voto == 4:
        votos4 += 1
    else:
        print("Voto inválido. Debe ser 1, 2, 3 o 4.")
    
    voto = int(input("Voto: "))

# Calcular total de votos
total = votos1 + votos2 + votos3 + votos4

# Calcular porcentajes (evitando división por cero)
if total > 0:
    por1 = (votos1 / total) * 100
    por2 = (votos2 / total) * 100
    por3 = (votos3 / total) * 100
    por4 = (votos4 / total) * 100
else:
    por1 = por2 = por3 = por4 = 0

# Mostrar resultados
print("\nResultados:")
print("Candidato 1: ", votos1, "votos -", round(por1, 2), "%")
print("Candidato 2: ", votos2, "votos -", round(por2, 2), "%")
print("Candidato 3: ", votos3, "votos -", round(por3, 2), "%")
print("Candidato 4: ", votos4, "votos -", round(por4, 2), "%")