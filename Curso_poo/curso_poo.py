# Creación de clases

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def saluda (self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'
    

if __name__ == "__main__":
    david=Persona("david",25)
    erica=Persona("erika",32)

    print(david.saluda(erica))