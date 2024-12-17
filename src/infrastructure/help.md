4. Capa de Infraestructura
Responsabilidad:

Implementar detalles técnicos como:
Persistencia en bases de datos (repositorios).
Servicios externos (APIs de terceros, servicios de correo electrónico, etc.).
Tareas asíncronas (Celery, Redis).
Adaptar la lógica del sistema a tecnologías específicas.
Seguir las interfaces definidas en la Capa de Dominio.
Llama a:

Servicios externos, como bases de datos o APIs externas.
Es llamada por:

La Capa de Aplicación a través de las interfaces definidas en la Capa de Dominio.