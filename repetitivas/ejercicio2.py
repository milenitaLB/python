"""
En un supermercado, se ha implementado la estrategia de descuento, según el valor de la compra y la balota que el cliente saque de una bolsa secreta. Las condiciones se listan a continuación:
- si el valor de la compra es superior igual a 50.000 pesos y saca:
a. balota roja el descuento será del 10%
b. balota verde el descuento será del 15%
c. balota azul el descuento será del 20%
d. balota amarilla el descuento será del 50%
e. balota negra el descuento será del 100%
-Si la compra es inferior a 50.000 pesos no participará del sorteo, para este caso se muestra un mensaje y se  imprimirá solo el valor a pagar.
elabore un algoritmo que permita leer la compra, evaluar las condiciones e imprimir el valor de la compra, e color de la balota  el  valor del descuento y el valor a pagar.
"""
compra = 1

while compra > 0:
    
    compra = float(input("Ingrese el valor de la compra (en pesos): "))
    
    if compra >= 50000:
        
        balota = input("Ingrese el color de la balota (roja, verde, azul, amarilla, negra): ")
        
        
        if balota == "roja":
            descuento = 0.10
        elif balota == "verde":
            descuento = 0.15
        elif balota == "azul":
            descuento = 0.20
        elif balota == "amarilla":
            descuento = 0.50
        elif balota == "negra":
            descuento = 1.00
        else:
            print("Color de balota no válido")
            continue
        
        
        valor_a_pagar = compra - (compra * descuento)
    else:
        print("Compra inferior a 50,000 pesos. No participa en el sorteo.")
        valor_a_pagar = compra
    
    # Imprimir resultados
    print(f"Valor de la compra: {compra} pesos")
    print(f"Color de la balota: {balota}")
    print(f"Descuento: {descuento * 100}%")
    print(f"Valor a pagar: {valor_a_pagar} pesos")