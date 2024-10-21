class Celular:
    def __init__(self, marca, modelo, camara): #Constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f'Estas haciendo una llamada desde un: {self.modelo}')
        
    def colgar(self):
        print(f'Colgaste una llamada desde un: {self.modelo}')
        
celular1 = Celular("Samsung", "S23", "50MP")
celular2 = Celular("Iphone", "15 pro max", "50MP")

celular1.llamar()