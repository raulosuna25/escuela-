class CuentaBancaria:
    
    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 0.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
        elif self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo}")
        else:
            print("Fondos insuficientes.")

    def consultarSaldo(self):
        return self.saldo

    def mostrarInformacion(self):
        return f"Titular: {self.titular}, Saldo: ${self.saldo}"

# PRUEBAS DEL PROGRAMA


# Crear cuentas
cuenta1 = CuentaBancaria("raulo osuna", "001234567", 1000.0)
cuenta2 = CuentaBancaria("María osuna", "009876543", 2000.0)

# Operaciones cuenta1
cuenta1.depositar(500.0)
print(cuenta1.mostrarInformacion())

cuenta1.retirar(200.0)
print(f"Saldo actual: ${cuenta1.consultarSaldo()}")

cuenta1.retirar(2000.0)

print("---------------------------")

# Operaciones cuenta2
cuenta2.depositar(300.0)
cuenta2.retirar(1000.0)
print(cuenta2.mostrarInformacion())
print(f"Saldo actual cuenta2: ${cuenta2.consultarSaldo()}")