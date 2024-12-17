1. Capa de Presentación (API)
Responsabilidad:

Proporcionar una interfaz para interactuar con el sistema.
Exponer los endpoints HTTP (o cualquier otra interfaz de entrada).
Recibir datos de entrada (requests) y enviarlos a la capa de aplicación.
Manejar las respuestas y devolverlas al cliente (usuario, frontend, otra API).
Llama a:

La Capa de Aplicación (Casos de Uso).
Es llamada por:

Los clientes (frontend, herramientas como Postman, o consumidores de API).