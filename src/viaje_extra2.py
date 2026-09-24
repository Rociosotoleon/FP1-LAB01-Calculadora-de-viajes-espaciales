distancia_km = int(input("Introduce la distancia:"))  # distancia Tierra - Luna
velocidad_kmh = int(input("Introduce la velocidad:"))
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24
tiempo_semanas = int(tiempo_dias // 7)
dias = int(tiempo_dias % 7)
print(f"Tardarías {tiempo_semanas} semanas en llegar y {dias} dias.")