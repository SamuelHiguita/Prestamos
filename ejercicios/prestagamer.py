# app.py - Pantalla de bienvenida del Sistema de Préstamos

print("==================================================")
print("       SISTEMA DE CONTROL DE PRÉSTAMOS            ")
print("==================================================")

# Pantalla de bienvenida / Registro inicial
print("¡Hola! Vamos a registrar un nuevo movimiento.\n")

nombre_deudor = input("¿A quién le vas a hacer el préstamo?: ")
monto_prestamo = input("¿Cuánto dinero se le va a prestar?: ")

print("\n--------------------------------------------------")
print(f"📋 Resumen inicial:")
print(f"   - Deudor: {nombre_deudor}")
print(f"   - Monto: ${monto_prestamo}")
print("¡Bienvenido al sistema! Datos capturados con éxito.")
print("--------------------------------------------------")