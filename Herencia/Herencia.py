class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, universidad, promedio):
        super().__init__(nombre, edad, nacionalidad)
        self.universidad = universidad
        self.promedio = promedio

jesus = Empleado("Jesus", 21, "Mexicano", "Programador", 15000)
roberto = Estudiante("Roberto", 23, "Argentio", "UTXJ", 9.2)

print(jesus.trabajo)
print(roberto.promedio)