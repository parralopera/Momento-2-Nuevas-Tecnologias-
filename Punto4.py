# Cuarto Punto

'''
Crear una clase que permita Matricula con la siguiente información
# Atrubutos
•	código matricula
•	nombre completo
•	Dirección
•	Teléfono
•	Curso
# Funciones
-	Deberá realizar el constructor de la clase.
-	El método de inscripción
-	El método de consulta
-	El método de eliminación de la matricula.

Nota: Los metodos de consulta, eliminacion no funcionan.

'''

class Matricula:
    def __init__(self,idmat,nombre,apellido,direccion,telefono,curso):
        self.Idmat = idmat
        self.Nombre = nombre
        self.Apellido = apellido
        self.Direccion = direccion
        self.Telefono = telefono
        self.Curso = curso
        self.inicio=[]
        self.datos=[0]
# Eliminar memoria
#    def __del__(self,idmat,nombre,apellido,direccion,telefono,curso):
#        print("Matricula Removida...")
# Iniciar Programa
#def iniciar_programa(self):
#    return self.insertar_matricula

    def insertar_matricula(self,dato):
        self.datos=[]
        self.datos.append(dato)
        return self.datos

    def mostrar_matricula(self):
        print(self.datos)
        
#def elimnar(self):
        
# idmat
    def set_idmat(self,idmat):
        self.Idmat=idmat
    def get_idmat(self):
        return self.Idmat

# Nombre       
    def set_nombre(self,nombre):
        self.Nombre=nombre
    def get_nombre(self):
        return self.Nombre

# Apellido
    def set_apellido(self,apellido):
        self.Apellido=apellido
    def get_apellido(self):
        return self.Apellido

# Direccion
    def set_direccion(self,dereccion):
        self.Direccion=dereccion
    def get_direccion(self):
        return self.Direccion
    
# Telefono
    def set_telefono(self,telefono):
        self.Telefono=telefono
    def get_telefono(self):
        return self.Telefono

# Curso
    def set_curso(self,curso):
        self.Curso=curso
    def get_curso(self):
        return self.Curso
    
# Instanciar Metodos

obj_mat=Matricula(0,'','','',0,'',)
print(obj_mat.Idmat)

set_idmat=int(input("Ingrese su ID de matricula: "))
obj_mat.insertar_matricula(set_idmat)

set_nombre=(input("Ingrese su nombre completo: "))
obj_mat.insertar_matricula(set_nombre)

set_apellido=(input("Ingrese su apellido: "))
obj_mat.insertar_matricula(set_apellido)

set_direccion=(input("Ingrese su direccion: "))
obj_mat.insertar_matricula(set_direccion)

set_telefono=(input("Ingrese su numero de telefono: "))
obj_mat.insertar_matricula(set_telefono)

set_curso=(input("Ingrese curso a matricular: "))
obj_mat.insertar_matricula(set_curso)

obj_mat.mostrar_matricula()
print("Su matrucula... \n")
print("ID de Matricula... ", set_idmat)
print("Nombre Aspirante... ", set_nombre)
print("Apellido Aspirante... ", set_apellido)
print("Direccion... ", set_direccion)
print("Telefono... ", set_telefono)
print("Curso a Matricular... ", set_curso)

que_hacer = (input("¿Que Quiere Hacer? 1:Eliminar,2:Continuar,3:Consultar"))
if (que_hacer=="1"):
        print("NO FUNCIONA AUN...")
elif (que_hacer=="2"):
        obj_mat.mostrar_matricula()
elif (que_hacer=="3"):
        print("NO FUNCIONA AUN...")

#obj_mat.eliminar_datos()