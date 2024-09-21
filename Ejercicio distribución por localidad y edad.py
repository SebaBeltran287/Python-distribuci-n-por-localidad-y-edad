import os
import math
os.system("cls")
concepcion=0
talcahuano=0
coronel=0
hualpen=0
san_pedro=0
chiguayante=0
entre18y25=0
mayores25=0
total=0
continuar="si"
while continuar=="si":
    os.system("cls")
    ejecutar="si"
    input("Ingrese su nombre: ")
    edad=0
    while  edad<18:
        edad=int(input("Ingrese su edad: "))
        if edad<18:
            print("Usted no tiene 18 años")
    if 25<edad:
        mayores25=mayores25+1
    else:
        entre18y25+=1
    while ejecutar=="si":
        print("1. Concepción")
        print("2. Talcahuano")
        print("3. Coronel")
        print("4. Hualpén")
        print("5. San Pedro")
        print("6. Chiguayante")
        localidad= int(input("Ingrese el numero correspondiente a la localidad: "))
        if localidad==1 or localidad==2 or localidad==3 or localidad==4 or localidad==5 or localidad==6:
            ejecutar="no"
            if localidad==1:
                concepcion+=1
            if localidad==2:
                talcahuano+=1
            if localidad==3:
                coronel+=1
            if localidad==4:
                hualpen+=1
            if localidad==5:
                san_pedro+=1
            if localidad==6:
                chiguayante+=1
        else:
            print("No seleccionó ninguna opción")
            ejecutar="si"
    continuar=input("¿Desea ingresar otro alumno?(si/no): ")
    total=total+1
print(f"Total de Alumnos Ingresados: {total}")
print("Distribución por Localidad")
print(f"Concepción: {concepcion}" , round(concepcion*100/total,1),"%")
print(f"Talcahuano: {talcahuano}" , round(talcahuano*100/total,1),"%")
print(f"Coronel: {coronel}" , round(coronel*100/total,1),"%")
print(f"Hualpén: {hualpen}" , round(hualpen*100/total,1),"%")
print(f"San Pedro: {san_pedro}" , round(san_pedro*100/total,1),"%")
print(f"Chiguayante: {chiguayante}" , round(chiguayante*100/total,1),"%")

print("Distribución por Edad")
print(f"Entre 18 y 25: {entre18y25}" , round(entre18y25*100/total,1),"%")
print(f"Mayores a 25: {mayores25}" , round(mayores25*100/total,1),"%")
