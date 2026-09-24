

for i in range(10000, 50001, 10000):
    distancia = 225000000
    tiempo_horas = distancia / i
    tiempo_dias = tiempo_horas / 24 

    print(f"Velocidad: {i} km/h -> Tiempo: {tiempo_dias} días")