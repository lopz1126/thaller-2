#funcion para crear la matriz
def crear_matriz_circunferencias(filas,columnas):
    return [['○' for _ in range(columnas)]for _ in range(filas)]

#fucion para imprimir la matriz
def print_matriz(matriz):
    print("  0 1 2 3 4 5 6 7")

    for i, filas in enumerate(matriz):
        print(i ,end=" ")
        for celda in filas:
            print(celda,end=" ")
        print()



#creacion de la matriz y muestra de que la matriz se creo
matriz= crear_matriz_circunferencias(8,8)
print_matriz(matriz)


#bucle de logica del software
while True:
    print(f"\nelija la opcion que desea \n 1. cambiar un circulo\n 2. reiniciar matriz \n 3. salir")

    #validacion de que ingreso la seleccion correctamente
    try:
        selecion_1=int(input())
    except ValueError:
        print("ingrese un valor valido")
        continue
       
    if selecion_1 == 1:
        #validacion de que ingreso la seleccion fila correctamente
        while True:
            try:    
                c_fila=int(input("posicion x = "))
                if c_fila >= 0 and c_fila < 9:
                    break
                else:
                    print("valor no valido")
            except ValueError:
                print("ingrese un numero")
        #validacion de que ingreso la seleccion columna correctamente
        while True:  
            try:
                c_columna=int(input("posicion y = "))
                if c_fila >= 0 and c_fila < 9:
                    break
                else:
                    print("valor no valido")   
            except ValueError:
                print("ingrese un numero")
        #cambio del circulo en la matriz
        matriz[c_fila][c_columna]="●"
        print(f"\n se cambio la cordenada ({c_fila} , {c_columna}) \n")
        print_matriz(matriz)
    #reinicio matriz
    elif selecion_1 ==2:
        matriz= crear_matriz_circunferencias(8,8)
        print_matriz(matriz)

    #salida del software
    elif selecion_1 == 3:
        print("has salido del programa")
        break

    else : 
        print("elige una opcion valida")
    
