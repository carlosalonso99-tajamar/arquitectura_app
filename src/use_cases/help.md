2. Capa de Aplicación (Casos de Uso)
Responsabilidad:

Orquestar la lógica de negocio específica para una tarea o acción (por ejemplo, crear un usuario).
Garantizar que los flujos de trabajo cumplan con las reglas de negocio.
Actuar como intermediario entre la Capa de Presentación y la Capa de Dominio.
No debe contener detalles de implementación específicos de bases de datos o infraestructura.
Llama a:

La Capa de Dominio para ejecutar lógica de negocio o validaciones.
La Capa de Infraestructura (a través de interfaces) para interactuar con sistemas externos como bases de datos o servicios.
Es llamada por:

La Capa de Presentación (API o endpoints).
