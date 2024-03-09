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
valorCompra=int(input("valor de la compra: "))

if valorCompra>=50000:
    300
    colorBalota=input("digite el color de la balota: ")  
    if colorBalota=="roja":
        
        descuento=valorCompra-(valorCompra*10)/100
        valorPagar=valorCompra-descuento
    elif colorBalota=="verde":
        
        descuento=valorCompra-(valorCompra*15)/100
        valorPagar=valorCompra-descuento
    elif colorBalota=="azul":
        descuento=valorCompra-(valorCompra*20)/100
        valorPagar=valorCompra-descuento
    elif colorBalota=="amarilla":
        descuento=valorCompra-(valorCompra*50)/100
        valorPagar=valorCompra-descuento
    elif colorBalota=="negra":
        descuento=valorCompra-(valorCompra*100)/100
        valorPagar=valorCompra-descuento
    print(f"valor de la compra:{valorCompra}")
    print(f"color de la Balota:{colorBalota}")
    print(f"valor del descuento:{valorPagar}")
    print(f"valor a pagar{descuento}")
else: 
    print("NO TIENE DESCUENTO ")


