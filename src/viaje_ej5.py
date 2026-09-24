
respuesta = "s"
while respuesta.lower() == "s":
    distancia_km = int(input("Introduce la distancia:"))  
    velocidad_kmh = int(input("Introduce la velocidad:"))
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    respuesta = input("¿Quieres hacer otra simulación? (s/n)")

print("Fin")