# Segundo Punto

'''
1.	Crear con el uso de diccionarios una cesta de Compras,
que permita adicionar prendas de vestir como: camisetas, pantalones, short, camisas, pantalonetas para hombres,
en la compra deberá limitar que no exceda más de 10 productos.
Se debe ingresar la prenda el precio y la talla para cada uno.
Luego deberá calcular el valor a pagar.

Nota: (Pendiente el limetante de 10 productos)
'''

Cesta={}
centinela='si'
while centinela=='si':
    prenda=input("Introduzca prenda: ")
    talla=int(input("Introdusca la talla de " +prenda+ ':'))
    valor=int(input("Introdusca precio de " +prenda+ ':'))
    Cesta[prenda,talla]=valor
    print(Cesta)
    centinela=input( "si desea continuar /si, sino No :")
print(Cesta)

total=0
def subtotal(precio,cantidad):
    subtotals=precio*cantidad
    return subtotals
    
for null,precio in Cesta.items():
    cantidad=int(input("ingrese cantidad de prendas a pagar: "))
    total=total+subtotal(precio,cantidad)
print("El precio de los productos es:{total}",total)