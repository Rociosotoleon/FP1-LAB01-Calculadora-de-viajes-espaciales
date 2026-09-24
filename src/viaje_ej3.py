edad = int(input("Introduce tu edad:"))
nivel_fisico = int(input("Introduce tu nivel fisico  entre 1 y 10:"))

while  not (1 <= nivel_fisico <= 10):
     nivel_fisico = int(input("Valor incorrecto. Introduce tu nivel fisico  entre 1 y 10:"))

if edad < 18:
    print("Debes ser mayor de edad")
elif nivel_fisico < 5:
        print("Debes estar en mejor forma")
else: 
    print("¡Listo para despegar!")


