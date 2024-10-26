# ENTREGA 1- SIMULADOR DE RESERVAS DE HOTEL.

Este proyecto simula un sistema de reservas para un hotel de 5 estrellas. Los usuarios pueden realizar reservas, cancelarlas y consultar la disponibilidad e información detallada sobre cada habitación.

## Descripción del código
Cuando ejecutas el código, el programa muestra un menú interactivo que te muestra el sistema de reservas de un hotel. Este menú inicial permite al usuario ver la disponibilidad de habitaciones, reservar y cancelar reservas y consultar el estado de las habitaciones.

El menú principal muestra opciones numeradas. La pantalla se verá algo así:

--- Sistema de Reservas del Hotel ---
1. Mostrar disponibilidad
2. Realizar reserva
3. Cancelar reserva
4. Mostrar información de una habitación
5. Mostrar gráfico de ocupación
6. Salir
Selecciona una opción: 

- Para mostrar la disponibilidad de las habitaciones, debes seleccionar la opción 1. Esto mostrará una lista de habitaciones que están disponibles para reservar, organizadas por pisos y tipos.

- Si quieres reservar una habitación, selecciona la opción 2. El programa te pedirá que ingreses el número de la habitación y la fecha de reserva en formato YYYY-MM-DD. Debes ingresar los datos en este formato para seguir.
Si la reserva se realiza correctamente, el sistema mostrará un mensaje de confirmación como: "Habitación 101 reservada con éxito." No se podrá volver a reservar y desaparecerá de la lista de disponibles.

- Para cancelar una reserva, selecciona la opción 3. El programa solicitará el número de la habitación que deseas cancelar. Ingresa el número, por ejemplo:
Si la cancelación es exitosa, verás el mensaje: "Habitación 101 cancelada con éxito." Volverá a aparecer como disponible.

- Si deseas consultar información detallada de una habitación, elige la opción 4. El programa te pedirá el número de la habitación, y tras ingresar este número, mostrará el estado actual de la habitación (disponible o reservada), el tipo de habitación, y las vistas que ofrece.

- Para ver un gráfico de ocupación del hotel, selecciona la opción 5. El programa abrirá un gráfico circular que representa la ocupación actual del hotel, mostrando el porcentaje de habitaciones ocupadas y las disponibles.

- Finalmente, si deseas salir del programa, selecciona la opción 6 para cerrar el sistema de reservas.
