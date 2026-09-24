distancia_viaje = int(input("Introduce la distancia de tu viaje:"))
if distancia_viaje < 150000:
    print("No hay paradas")
else:
    for i in range(150000, distancia_viaje + 1, 150000):
        print(f"Parada en el km {i}")
    Total_paradas = distancia_viaje // 150000
    print(f"Total de paradas para repostar {Total_paradas}")

