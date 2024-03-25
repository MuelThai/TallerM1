N = int(input("Ingrese la cantidad de frutas para el salpicón: "))

frutas = []

for i in range(N):
    print(f"\nFruta {i+1}:")
    fruta = {}
    fruta["id"] = i + 1
    fruta["nombre"] = input("Nombre de la fruta: ")
    fruta["precio_unitario"] = float(input("Precio unitario de la fruta: "))
    fruta["cantidad"] = int(input("Cantidad de esta fruta: "))
    frutas.append(fruta)

def mostrarPrecio():
    precioTotal = sum(fruta["precio_unitario"] * fruta["cantidad"] for fruta in frutas)
    print(f"El Costo Total del Salpifruta es : ${precioTotal} pesos colombianos")

def mostrarFrutas():
    frutasxPrecio= sorted(frutas, key=lambda x: x["precio_unitario"],reverse=True)
    print("Frutas de Mayor a Menor precio: ")
    for fruta in frutasxPrecio:
        print (f'Nombre: {fruta["nombre"]}-Precio Unitario: ${fruta["precio_unitario"]}')
def mostrarFruta():
    frutaBarata= min(frutas, key=lambda x: x["precio_unitario"] )
    print (f'\nNombre: {frutaBarata["nombre"]} es la fruta más barata con un -Precio Unitario: {frutaBarata["precio_unitario"]}')


opcion=0

while(opcion !=4):
    print("\nSalpiFrutas")
    print("1.Mostrar el precio del Salpicon: ")
    print("2.Mostrar frutas seleccionadas ($ desc): ")
    print("3.Mostrar cual es la fruta mas barata: ")
    print("4.No voy a comprar nada")
    opcion=int(input("Digite la opcion deseada: "))

    if opcion == 1:
        mostrarPrecio()
    elif opcion == 2:
        mostrarFrutas()
    elif opcion == 3:
        mostrarFruta()
    else:
        print("Ingrese una opcion correcta")


