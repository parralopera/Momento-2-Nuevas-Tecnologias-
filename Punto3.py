# Tercer Punto

'''
1. Se quiere registrar la información de un vehículo,
como la placa la fecha de entrada, fecha salida, celda de parqueo,
luego se desea calcular el tiempo que duro un vehículo parqueado y generar el valor del boleto a pagar,
debe indicar si la celda se encuentra ocupada o no.
(desarrollar con el uso de funciones)

Nota: No Calcula por fecha, calcula por dias. Los dias se ingresen por teclado (PRECIO FIJO)

'''

class Vehiculo:
    def __init__(self,placa,fe_in,fe_out,espacio):
        self.Placa = placa
        self.Fe_in = fe_in
        self.Fe_out = fe_out
        self.Espacio = espacio
        self.datos=[0]
        
    def insertar_vehiculo(self,dato):
        self.datos=[]
        self.datos.append(dato)
        return self.datos
        
    def tiempo_park(self,):
        return self.datos
    
    def imprimir_boleto(self):
        print(self.datos)
    
# Atributos

# Placa       
    def set_placa(self,placa):
        self.Placa=placa
    def get_placa(self):
        return self.Placa

# Fe_in       
    def set_fe_in(self,fe_in):
        self.Fe_in=fe_in
    def get_fe_in(self):
        return self.Fe_in

# Fe_out
    def set_fe_out(self,fe_out):
        self.Fe_out=fe_out
    def get_fe_out(self):
        return self.Fe_out

# Espacio
    def set_espacio(self,valor):
        self.Espacio=valor
    def get_espacio(self):
        return self.Espacio

        
obj_carro=Vehiculo(0,0,0,0,)
print(obj_carro.Placa)

set_placa=int(input("Ingrese Placa: "))
obj_carro.insertar_vehiculo(set_placa)

set_fe_in=int(input("Ingrese Fecha Ingreso: "))
obj_carro.insertar_vehiculo(set_fe_in)

set_fe_out=int(input("Ingrese Fecha Salida: "))
obj_carro.insertar_vehiculo(set_fe_out)

set_espacio=int(input("Ingrese Espacio de lote: "))
obj_carro.insertar_vehiculo(set_espacio)

obj_carro.tiempo_park()
dias=int(input("Ingrese Numero de Dias Parqueado: "))
time = 4000 * dias

obj_carro.imprimir_boleto()
print("Su Boleto... REGRESA PRONTO\n")
print("Numero de Placa... ", set_placa)
print("Fecha Ingreso... ", set_fe_in)
print("Fecha Salida... ", set_fe_out)
print("Espacio Ocupado... ", set_espacio)
print("Dias en Uso", dias)
print("Cobro por dias", time)