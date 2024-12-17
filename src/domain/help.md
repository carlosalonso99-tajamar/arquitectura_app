3. Capa de Dominio
Responsabilidad:

Contener las reglas de negocio centrales y la lógica que define cómo funciona el sistema.
Definir las entidades del dominio (por ejemplo, User).
Proveer interfaces (contratos) para repositorios y servicios.
Garantizar que las reglas de negocio sean consistentes.
Llama a:

Ninguna capa concreta, ya que es autónoma y no debe conocer otras capas.
Es llamada por:

La Capa de Aplicación para realizar validaciones o manipular entidades.
La Capa de Infraestructura para implementar las interfaces definidas.