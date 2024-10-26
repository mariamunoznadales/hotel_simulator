import random
from datetime import datetime
import matplotlib.pyplot as plt

class Habitacion:
    def __init__(self, numero, tipo, piso, vistas):
        self.numero = numero
        self.tipo = tipo  # "suite" o "estándar"
        self.piso = piso
        self.vistas = vistas  # "ciudad" o "mar"
        self.estado = 'disponible'
        self.fecha_reserva = None

    def reservar(self, fecha_reserva):
        if self.estado == 'disponible':
            self.estado = 'reservada'
            self.fecha_reserva = fecha_reserva
            return True
        return False

    def cancelar_reserva(self):
        if self.estado == 'reservada':
            self.estado = 'disponible'
            self.fecha_reserva = None
            return True
        return False

    def mostrar_info(self):
        info = (f"Habitación {self.numero} - Tipo: {self.tipo}, Piso: {self.piso}, "
                f"Vistas: {self.vistas}, Estado: {self.estado}")
        if self.fecha_reserva:
            info += f", Fecha de reserva: {self.fecha_reserva}"
        return info


class Hotel:
    def __init__(self):
        self.habitaciones = []
        self.generar_habitaciones()

    def generar_habitaciones(self):
        tipos = ['suite', 'estándar']
        vistas = ['ciudad', 'mar']
        for piso in range(1, 4):  # Tres pisos
            for num in range(1, 6):  # Cinco habitaciones por piso
                numero = piso * 100 + num
                tipo = random.choice(tipos)
                vista = random.choice(vistas)
                habitacion = Habitacion(numero, tipo, piso, vista)
                self.habitaciones.append(habitacion)

    def mostrar_disponibilidad(self):
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if habitacion.estado == 'disponible':
                print(habitacion.mostrar_info())

    def realizar_reserva(self, numero_habitacion, fecha_reserva):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                if habitacion.reservar(fecha_reserva):
                    print(f"Habitación {numero_habitacion} reservada con éxito.")
                    return
                else:
                    print(f"Habitación {numero_habitacion} ya está reservada.")
                    return
        print(f"Habitación {numero_habitacion} no encontrada.")

    def cancelar_reserva(self, numero_habitacion):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                if habitacion.cancelar_reserva():
                    print(f"Habitación {numero_habitacion} cancelada con éxito.")
                    return
                else:
                    print(f"Habitación {numero_habitacion} no está reservada.")
                    return
        print(f"Habitación {numero_habitacion} no encontrada.")

    def mostrar_info(self, numero_habitacion):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                print(habitacion.mostrar_info())
                return
        print(f"Habitación {numero_habitacion} no encontrada.")

    def generar_grafico_ocupacion(self):
        ocupacion = {
            'disponible': sum(1 for h in self.habitaciones if h.estado == 'disponible'),
            'reservada': sum(1 for h in self.habitaciones if h.estado == 'reservada')
        }
        labels = ocupacion.keys()
        sizes = ocupacion.values()
        colors = ['#66b3ff', '#ff6666']
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title("Ocupación del Hotel")
        plt.show()


def main():
    hotel = Hotel()

    while True:
        print("\n--- Sistema de Reservas del Hotel ---")
        print("1. Mostrar disponibilidad")
        print("2. Realizar reserva")
        print("3. Cancelar reserva")
        print("4. Mostrar información de una habitación")
        print("5. Mostrar gráfico de ocupación")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            hotel.mostrar_disponibilidad()
        elif opcion == '2':
            numero = int(input("Ingresa el número de la habitación a reservar: "))
            fecha_str = input("Ingresa la fecha de reserva (YYYY-MM-DD): ")
            try:
                fecha_reserva = datetime.strptime(fecha_str, "%Y-%m-%d")
                hotel.realizar_reserva(numero, fecha_reserva)
            except ValueError:
                print("Formato de fecha incorrecto. Usa YYYY-MM-DD.")
        elif opcion == '3':
            numero = int(input("Ingresa el número de la habitación a cancelar: "))
            hotel.cancelar_reserva(numero)
        elif opcion == '4':
            numero = int(input("Ingresa el número de la habitación para ver su información: "))
            hotel.mostrar_info(numero)
        elif opcion == '5':
            hotel.generar_grafico_ocupacion()
        elif opcion == '6':
            print("Gracias por usar el sistema de reservas.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
