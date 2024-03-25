import random
A={"unidades":0,"productos":[]}
B={"unidades":0,"productos":[]}
C={"unidades":0,"productos":[]}
D={"unidades":0,"productos":[]}

idUtilizada = []

opcion=100

while(opcion !=5):
    print("Tienda Comics")
    print("1.Registro de Producto")  
    print("2.Mostrar Inventario de Productos")
    print("3.Busqueda por Nombre")
    print("4.Buscar y Modificar")
    print("5.Finalizar")
    opcion=int(input("Digite una opcion: "))

    if opcion == 1:
        producto={}
        product_id=random.randint(1,100)
        while product_id in idUtilizada:
            product_id = random.randint(1,100)
        producto["id"] = product_id
        producto["nombre"]=input("Digite nombre del producto: ")
        producto["precio"]=float(input("Digite el precio del producto: "))
        producto["ubicacion"]=input("Digite la ubicacion del producto: ")
        flag=False
        while flag == False:
            producto["unidades"]=int(input("Digite las unidades compradas del producto: "))
            if producto["unidades"] > 50:
                print("Sobrepasas la cantidad de cualquier estanteria")
            else:
                if producto ["ubicacion"] == "A" or "a":
                    total=A["unidades"] +producto["unidades"]
                    if total <= 50:
                        A["unidades"]+=producto["unidades"]
                        flag=True
                    else:
                         print("Esta ubicacion no tiene espacio para esa cantidad de unidades")

                elif producto["ubicacion"] == "B" or "b":
                    total=B["unidades"] +producto["unidades"]
                    if total <= 50:
                        B["unidades"]+=producto["unidades"]
                        flag=True
                    else:
                         print("Esta ubicacion no tiene espacio para esa cantidad de unidades")
                elif producto["ubicacion"] == "C" or "c":
                    total=C["unidades"] +producto["unidades"]
                    if total <= 50:
                        C["unidades"]+=producto["unidades"]
                        flag=True
                    else:
                         print("Esta ubicacion no tiene espacio para esa cantidad de unidades")
                elif producto ["ubicacion"] == "D" or "d":
                    total=D["unidades"] +producto["unidades"]
                    if total <= 50:
                        D["unidades"]+=producto["unidades"]
                        flag=True
                    else:
                         print("Esta ubicacion no tiene espacio para esa cantidad de unidades")   
        
        producto["descripcion"]=input("Digite la descripcion del producto: ")
        producto["casa"]=input("Digite la casa del producto: ")
        producto["pais"]=input("Digite la pais del producto: ")
        producto["garantia"]=input("Digite si cuenta con garantia producto: ")
        if producto ["ubicacion"] == "A" or "a":
            A["productos"].append(producto)
        elif producto["ubicacion"] == "B" or "b":
            B["productos"].append(producto)
        elif producto["ubicacion"] == "C" or "c":
            C["productos"].append(producto)
        elif producto ["ubicacion"] == "D" or "d":
            D["productos"].append(producto)
    
    
    elif opcion == 2:
        print("Inventario Ubicacion A")
        print(A)
        print("Inventario Ubicacion B")
        print(B)
        print("Inventario Ubicacion C")
        print(C)
        print("Inventario Ubicacion D")
        print(D)

    elif opcion == 3:
        nombre_busqueda = input("Ingrese el nombre del producto que desea buscar: ")
        encontrado = False
    
        for lista in [A["productos"], B["productos"], C["productos"], D["productos"]]:
            for producto in lista:
                if producto["nombre"] == nombre_busqueda:
                    print("Producto encontrado:")
                    print("ID:", producto["id"])
                    print("Nombre:", producto["nombre"])
                    print("Precio:", producto["precio"])
                    print("Ubicación:", producto["ubicacion"])
                    print("Descripción:", producto["descripcion"])
                    print("Casa:", producto["casa"])
                    print("País:", producto["pais"])
                    print("Unidades:", producto["unidades"])
                    print("Garantía:", producto["garantia"])
                    encontrado = True
                    break  
            if encontrado:
                break  
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == 4:
        nombre_busqueda = input("Ingrese el nombre del producto que desea buscar: ")
        encontrado = False
    
        for lista in [A["productos"], B["productos"], C["productos"], D["productos"]]:
            for producto in lista:
                if producto["nombre"] == nombre_busqueda:
                    print("Producto encontrado:")
                    encontrado = True
                    nuevaCantidad=100
                    while nuevaCantidad > producto["unidades"]:
                        nuevaCantidad=int(input("Ingrese la nueva cantidad: "))
                        if nuevaCantidad > producto["unidades"]:
                            print("La nueva cantidad no puede ser mayor que la cantidad actual")
                    if producto["ubicacion"] == "A":
                        A["unidades"] += (nuevaCantidad - producto["unidades"])
                    elif producto["ubicacion"] == "B":
                        B["unidades"] += (nuevaCantidad - producto["unidades"])
                    elif producto["ubicacion"] == "C":
                        C["unidades"] += (nuevaCantidad - producto["unidades"])
                    elif producto["ubicacion"] == "D":
                        D["unidades"] += (nuevaCantidad - producto["unidades"])
                    producto["unidades"] = nuevaCantidad
                    print(producto)
            if encontrado:
                break  
        if not encontrado:
            print("Producto no encontrado.")