# Control de Carga de Pasajeros - Aerolínea "VuelosChile"
cabina = 0
bodega = 0
# Validar cantidad de equipajes
while True:

    try:

        cantidad = int(input("¿Cuántos equipajes se registrarán?: "))



        if cantidad <= 0:

            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

        else:

            break
    except ValueError:

        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
# Registro de equipajes

for i in range(cantidad):
    print(f"\n--- Registro de Equipaje {i + 1} ---")
    # Validar código de ticket
    while True:

        codigo = input("Ingrese código de ticket: ")

        if len(codigo) >= 5 and " " not in codigo:

            break

        else:

            print("Código inválido. Debe tener al menos 5 caracteres y no contener espacios.")

    # Validar peso del equipaje

    while True:

        try:

            peso = int(input("Ingrese peso del equipaje (kg): "))

            if peso <= 0:

                print("Error, Ingresa un número entero positivo para el peso.")

            else:

                break

        except ValueError:

            print("Error, Ingresa un número entero positivo para el peso.")



    # Clasificación automática

    if peso > 10:

        print("Clasificación: Equipaje de Bodega (Sobrecarga)")

        bodega += 1

    else:

        print("Clasificación: Equipaje de Cabina (Permitido)")

        cabina += 1



# Resumen final

print("\n====================================")

print(f"¡El avión transportará {cabina} equipajes en Cabina y {bodega} equipajes en Bodega!")

print("¡Manifiesto de carga listo!")

print("====================================")