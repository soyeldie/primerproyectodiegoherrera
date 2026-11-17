
import json

with open("data.json", "r", encoding="utf-8") as archivo:
  datos = json.load(archivo)

ventas = datos["ventas"]


# 1. Calcular el total facturado
def total_facturado(ventas):
    total = 0

    for venta in ventas:
        total += venta["cantidad"] * venta["precio_unitario"]

    return total


print("Total facturado:", total_facturado(ventas))


# 2. Calcular las ventas por categoría
def ventas_por_categoria(ventas):
    categorias = {}

    for venta in ventas:
        categoria = venta["categoria"]
        importe = venta["cantidad"] * venta["precio_unitario"]

        if categoria not in categorias:
            categorias[categoria] = 0

        categorias[categoria] += importe

    return categorias


print("Ventas por categoría:", ventas_por_categoria(ventas))


# 3. Identificar el producto más vendido
def producto_mas_vendido(ventas):
    productos = {}

    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]

        if producto not in productos:
            productos[producto] = 0

        productos[producto] += cantidad

    producto_ganador = max(productos, key=productos.get)

    return producto_ganador, productos[producto_ganador]


print("Producto más vendido:", producto_mas_vendido(ventas))
