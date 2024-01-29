class Cliente:
    def __init__(self, nombre, email, edad, intereses=[]):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.intereses = intereses
        self.carrito = []

    def comprar(self, producto, tienda):
        # procesar la compra, imprimo un mensaje
        print(f"{self.nombre} ha comprado {producto} en {tienda}.")

    def __str__(self):
        return f"Cliente(nombre={self.nombre}, email={self.email}, edad={self.edad}, intereses={self.intereses})"

# Instancia de Cliente1
cliente1 = Cliente1("Matias", "Matias@gmail.com", 22, ["Deportes", "Tecnología"])

# Realizar una compra
cliente1.comprar("Celular", "claro")

# Imprimir la información del cliente
print(cliente1)
