class Item:
    def _init_(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def _str_(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

    def actualizar_cantidad(self, cantidad):
        if cantidad < 0 and abs(cantidad) > self.cantidad:
            raise ValueError("La cantidad a restar excede la cantidad disponible.")
        self.cantidad += cantidad

    class GestorInventario:
        def _init_(self, archivo):
            self.archivo = archivo
            self.inventario = self.inventario()
            self.inventario.cargar_desde_archivo(archivo)

        def agregar_item(self, id: object, nombre, cantidad, precio):
            item = Item(id, nombre, cantidad, precio)
            self.inventario.agregar_item(item)
            self.inventario.guardar_en_archivo(self.archivo)

        def eliminar_item(self, id):
            self.inventario.eliminar_item(id)
            self.inventario.guardar_en_archivo(self.archivo)

        def listar_items(self):
            self.inventario.listar_items()

        def buscar_item(self, id):
            item = self.inventario.buscar_item(id)
            if item:
                print(item)
            else:
                print("Item no encontrado.")

    # Crear o cargar el sistema de inventario
    gestor = GestorInventario()

    # Agregar ítems al inventario
    gestor.agregar_item('001', 'Laptop', 10, 999.99)
    gestor.agregar_item('002', 'Teclado', 15, 49.99)

    # Listar todos los ítems
    print("Listado de ítems:")
    gestor.listar_items()

    # Buscar un ítem específico
    print("Buscar ítem con ID 001:")
    gestor.buscar_item('001')

    # Eliminar un ítem
    gestor.eliminar_item('002')

    # Listar todos los ítems después de la eliminación
    print("Listado de ítems después de la eliminación:")
    gestor.listar_items()