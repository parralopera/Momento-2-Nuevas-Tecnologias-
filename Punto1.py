# Primer Punto

'''
1.	Diseñe una función que permita registrar la información de un grupo de 5 personas con los siguientes datos:
identificación, nombre, salario, comisión, bonificaciones.
2.	La función antes de insertar a la lista debe permitir validar que el salario sea superior de 900000 que las comisiones mayores de 0 al igual que las bonificaciones.
3.	Deberá diseñar una segunda función donde esta permita mostrar la información contenida en la lista.
4.	Deberá realizar una función que permita buscar un dato en la lista.

Nota: Faltan las validaciones y la comision es fija

'''

class Empleado:
    def __init__(self,id,nombre,salario,comision,bonificacion):
        self.Id = id
        self.Nombre = nombre
        self.Salario = salario
        self.Comision = comision
        self.Bonificacion = bonificacion
        self.datos=[]
        self.sal=0
        
    def insertar_empleado(self,dato):
        self.datos=[]
        self.datos.append(dato)
        return self.datos
    
    def horas_trab(self):
        return self.datos

    def mostrar_empleado(self):
        print(self.datos)

# ID      
    def set_id(self,id):
        self.Id=id
    def get_id(self):
        return self.Id

# Nombre       
    def set_nombre(self,nombre):
        self.Nombre=nombre
    def get_nombre(self):
        return self.Nombre

# Salario
    def set_salario(self,salario):
        self.Salario=salario
    def get_salario(self):
        return self.Salario

# Comision
    def set_comision(self,comicion):
        self.Comision=comicion
    def get_comision(self):
        return self.Comision
    
# Bonificaciones
    def set_bonificacion(self,bonificacion):
        self.Bonificacion=bonificacion
    def get_bonificacion(self):
        return self.Bonificacion

# Instanciar Metodos

obj_emp=Empleado(0,'',0,0,0)
print(obj_emp.Id)

set_id=int(input("Ingrese su ID: "))
obj_emp.insertar_empleado(set_id)

set_nombre=(input("Ingrese su nombre: "))
obj_emp.insertar_empleado(set_nombre)

set_salario=(input("Ingrese su salario: "))
if (set_salario>="1000"):
        print("Salario Aprobado")
else:
        print("Salario No Aprobado")
obj_emp.insertar_empleado(set_salario)

obj_emp.horas_trab()
horas=int(input("Horas Extra: "))
extra = 4000 * horas
comision = extra - 5000
#salario_total = set_salario + extra

obj_emp.mostrar_empleado()
print("Su matrucula... \n")
print("ID... ", set_id)
print("Nombre... ", set_nombre)
print("Salario... ", set_salario)
print("Comision... ", comision)
print("Horas Extra Realizadas ", horas)
print("Bonificacion... ", extra)
print("Salario Total... ", set_salario, "Bonificacion", comision)

que_hacer=int(input("¿Que Quiere Hacer? 1:Mostar Lista 2:Continuar 3:Buscar"))
if (que_hacer=="1"):
        print("NO FUNCIONA AUN...")
elif (que_hacer=="2"):
        obj_emp.mostrar_empleado()
elif (que_hacer=="3"):
        print("NO FUNCIONA AUN...")