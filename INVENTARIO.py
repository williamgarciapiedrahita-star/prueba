# definicion de la matriz con 5 articulos(codigo de articulo,nombre,stock actual,stock minimo requerido)

inventario=[["101","arroz(kg)",5,20],["102","frijoles(kg)",15,10],[ "103","azucar(kg)",8,8],[ "104","aceite(l)",2,12],[ "105","sal(kg)",3,10]]

# modulo o funcion para determinar la cantidad exacta a pedir
def calcular_cantidad_a_pedir(stock_actual,stock_minimo_requerido):
    if stock_actual<stock_minimo_requerido:
        return stock_minimo_requerido-stock_actual
    else:
        return 0

# procesamiento y salida

print("""|==========LISTA DE PEDIDOS==========|""")
print(f"{'articulo':20}|{'cantidad a pedir'}")
print("-" * 40)


for articulo in inventario:
    codigo=articulo[0]
    nombre=articulo[1]
    stock_actual=articulo[2]
    stock_minimo_requerido=articulo[3]
    
    cantidad_a_pedir=calcular_cantidad_a_pedir(stock_actual,stock_minimo_requerido)
    
    print(f"{nombre:20}|{cantidad_a_pedir}")

    