"""
Desarrollar los siguientes algoritmos en Python: 
un grupo de 10 estudiantes presentan un examen de algoritmia. Hacer un algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e imprima:
• La cantidad de estudiantes que obtuvieron una calificación menor a 50. 
• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70.
• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80. 
• La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
La calificación obtenida en el examen de algoritmia debe ser entre 1 y 100.
"""
menor_50 = 0
entre_50_y_70 = 0
entre_70_y_80 = 0
mayor_80 = 0

# Iteramos sobre los 10 estudiantes
for _ in range(10):
    calificacion = int(input("Ingrese la calificación del estudiante (entre 1 y 100): "))
    while calificacion < 1 or calificacion > 100:
        print("Calificación inválida. Debe estar entre 1 y 100.")
        calificacion = int(input("Ingrese la calificación del estudiante (entre 1 y 100): "))
       
    if calificacion < 50:
        menor_50 += 1
    elif calificacion < 70:
        entre_50_y_70 += 1
    elif calificacion < 80:
        entre_70_y_80 += 1
    else:
        mayor_80 += 1

print(f"Cantidad de estudiantes con calificación menor a 50: {menor_50}")
print(f"Cantidad de estudiantes con calificación entre 50 y 70: {entre_50_y_70}")
print(f"Cantidad de estudiantes con calificación entre 70 y 80: {entre_70_y_80}")
print(f"Cantidad de estudiantes con calificación mayor o igual a 80: {mayor_80}")