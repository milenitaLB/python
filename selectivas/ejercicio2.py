"""
Desarrollar los siguientes algoritmos en Python: 
un grupo de 10 estudiantes presentan un examen de algoritmia. Hacer un algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e imprima:
• La cantidad de estudiantes que obtuvieron una calificación menor a 50. 
• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70.
• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80. 
• La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
La calificación obtenida en el examen de algoritmia debe ser entre 1 y 100.
"""
contador1=0
contador2=0
contador3=0
contador4=0
estudiante1=int(input("ingresar nota del estudiante_1:"))
estudiante2=int(input("ingresar nota del estudiante_2:"))
estudiante3=int(input("ingresar nota del estudiante_3:"))
estudiante4=int(input("ingresar nota del estudiante_4:"))
estudiante5=int(input("ingresar nota del estudiante_5:"))
estudiante6=int(input("ingresar nota del estudiante_6:"))
estudiante7=int(input("ingresar nota del estudiante_7:"))
estudiante8=int(input("ingresar nota del estudiante_8:"))
estudiante9=int(input("ingresar nota del estudiante_9:"))
estudiante10=int(input("ingresar nota del estudiante_10:"))

#if variable Estudiante1<50 or variable Estudiante1>50 or variable Estudiante1<70 or variable Estudiante1>70 or variable Estudiante1<80 or variable Estudiante1>80
if  estudiante1<50:
    contador1+=1 #suma al contador
elif estudiante1>=50 and estudiante1<70:
    contador2+=1
elif estudiante1>=70 and estudiante1<80:
    contador3+=1  
elif estudiante1>80:
    contador4+=1
if  estudiante2<50:
    contador1+=1 #suma al contador
elif estudiante2>=50 and estudiante2<70:
    contador2+=1
elif estudiante2>=70 and estudiante2<80:
    contador3+=1  
elif estudiante2>80:
    contador4+=1 
if  estudiante3<50:
    contador1+=1 #suma al contador
elif estudiante3>=50 and estudiante3<70:
    contador2+=1
elif estudiante3>=70 and estudiante3<80:
    contador3+=1  
elif estudiante3>80:
    contador4+=1 
if  estudiante4<50:
    contador1+=1 #suma al contador
elif estudiante4>=50 and estudiante4<70:
    contador2+=1
elif estudiante4>=70 and estudiante4<80:
    contador3+=1  
elif estudiante4>80:
    contador4+=1     
if  estudiante5<50:
    contador1+=1 #suma al contador
elif estudiante5>=50 and estudiante5<70:
    contador2+=1
elif estudiante5>=70 and estudiante5<80:
    contador3+=1  
elif estudiante5>80:
    contador4+=1
if  estudiante6<50:
    contador1+=1 #suma al contador
elif estudiante6>=50 and estudiante6<70:
    contador2+=1
elif estudiante6>=70 and estudiante6<80:
    contador3+=1  
elif estudiante6>80:
    contador4+=1
if  estudiante7<50:
    contador1+=1 #suma al contador
elif estudiante7>=50 and estudiante7<70:
    contador2+=1
elif estudiante7>=70 and estudiante7<80:
    contador3+=1  
elif estudiante7>80:
    contador4+=1 
if  estudiante8<50:
    contador1+=1 #suma al contador
elif estudiante8>=50 and estudiante8<70:
    contador2+=1
elif estudiante8>=70 and estudiante8<80:
    contador3+=1  
elif estudiante8>80:
    contador4+=1 
if  estudiante9<50:
    contador1+=1 #suma al contador
elif estudiante9>=50 and estudiante9<70:
    contador2+=1
elif estudiante9>=70 and estudiante9<80:
    contador3+=1  
elif estudiante9>80:
    contador4+=1    
if  estudiante10<50:
    contador1+=1 #suma al contador
elif estudiante10>=50 and estudiante10<70:
    contador2+=1
elif estudiante10>=70 and estudiante10<80:
    contador3+=1  
elif estudiante10>80:
    contador4+=1
print(f"la cantidad de estudiantes con nota menor a 50:{contador1}")
print(f"la cantidad de estudiantes con nota de 50 o mas y menor que 70:{contador2}")
print(f"la cantidad de estudiantes que obtuvieron nota de 70 o mas y menos que 80:{contador3}")
print(f"la cantidad de estudiantes que obtuvieron una nota de 80 o mas:{contador4}")