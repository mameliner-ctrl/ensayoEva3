print ("¡BIENVENIDO AL SISTEMA DE GESTION DE ECO-BICIS-URBANAS")
capacidad_maxima = 25
bicis_disponibles = 25
viajes_activos = 0 
ejecutando = True 
#ciclo principal
white ejecutando:
print("\n===Menu principal===")
print("1 bicicletas disponibles")
print("2 arrendar bicicletas (salida)")
print("3 devolver bicicleta (entrada)")
print("4 historial de viajes activos")
print("5 salir")
try:
    opcion = int(input("seleccione una opcion (1-5): "))
    except ValueError:
        print("opcion no valida, por favor, ingrese un numero entre 1 y 5")
        continue

    #opcion 1 
    if opcion == 1:
        print(f"\n[info] cantidad actual de bicicletas disponibles: {bicis_disponibles}")
        #opcion 2 arrendar bicicletas
        elif opcion == 2:
            print(f"\n--- arrendar bicicletas (disponibles: {bicis_disponibles})---")
            if bicis_disponibles == 0:
                print("lo sentimos, no quedan bicicletas disponibles")
                else:
                    try:
                        cantidad_a_arrendar = int(input("¿cuantas bicicletas desea arrendar?"))
                        if cantidad_a_arrendar <= 0:
                            print("Error, la cantidad a arrendar debe ser mayor a 0 ")
                            elif cantidad_a_arrendar > bicis_disponibles:
                                print(f"no hay suficientes bicicletas, puede arrendar hasta: {bicis_disponibles} ")
                                else:
                                    bicis_disponibles -= cantidad_a_arrendar
                                    viajes_activos += cantidad_a_arrendar
                                    print(f"arriendo exitoso, ha retirado {cantidad_a_arrendar} bicis")
                                except ValueError:
                                    print("Error, debe ingresar un numero entero")
                         #opcion 3 devolver bicicletas
                         elif opcion == 3:
                            diferencia = capacidad_maxima-bicis_disponibles
                            print (f"\N---DEVOLVER BICICLETAS (ESPACIO LIBRE EN ESTACION:{diferencia})")
                            try:
                                candidad_a_devolver = int(inputt("¿cuantas bicicletas desea devolver?:"))
                                if candidad_a_devolver <= 0:
                                    print("error, la cantidad a devolver debe ser mayor a 0")
                                    elif bicis_disponibles + candidad_a_devolver > capacidad_maxima:
                                        print(f"error: no se puede devolver tantas bicicletas, supera capacidad maxima de 25 bicis")
                                        else:
                                            bicis_disponibles += candidad_a_devolver
                                    viajes_activos -= candidad_a_devolver
                                    print(f"devolucion exitosa ha registrado {candidad_a_devolver}bicicletas")
                                    except ValueError:
                                        print("error, debe ingresar un numero entero valido")
                                        #opcion 4: viajes activos
                                        elif opcion == 4:
                                        print("\n[historial]actualmente hay {viajes_activos}bicicleta(s)en uso por usuarios")

                                    #opcion 5 salir
                                    elif opcion == 5:
                                        print("gracias por utilizar nuestro sofware, hasta la proxima")
                                        ejecutando = False 
                                        else:
                                            print("opcion fuera de rango")

