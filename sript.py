import os

# Definición de la estructura
structure = {
    "src": {
        "main.py": "# Punto de entrada de la aplicación\n",
        "config": {
            "settings.py": "# Configuración general (variables de configuración)\n",
            "container.py": "# Contenedor para inyección de dependencias\n",
        },
        "api": {
            "v1": {
                "routers": {
                    "user_router.py": "# Rutas relacionadas con usuarios\n",
                    "task_router.py": "# Rutas relacionadas con tareas\n",
                },
                "dependencies.py": "# Gestión de dependencias para la API\n",
            }
        },
        "domain": {
            "entities.py": "# Entidades de dominio\n",
            "interfaces.py": "# Contratos para repositorios y servicios\n",
        },
        "use_cases": {
            "use_case_1.py": "# Caso de uso 1: Crear usuario\n",
            "use_case_2.py": "# Caso de uso 2: Actualizar usuario\n",
        },
        "infrastructure": {
            "database": {
                "models.py": "# Modelos ORM\n",
                "repositories.py": "# Implementación de repositorios\n",
                "database.py": "# Configuración de la base de datos\n",
            },
            "tasks": {
                "celery.py": "# Configuración global de Celery\n",
                "user_tasks.py": "# Tareas específicas de usuarios\n",
            },
            "services": {
                "email_service.py": "# Enviar correos electrónicos\n",
                "third_party_api.py": "# Interacción con APIs externas\n",
            },
        },
        "tests": {
            "unit": {},
            "integration": {},
        },
        "utils": {
            "exceptions.py": "# Manejo de errores personalizados\n",
        },
    }
}

# Función para crear directorios y archivos
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # Si es un directorio
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:  # Si es un archivo
            with open(path, "w") as file:
                file.write(content)

# Crear la estructura
base_path = "./"
create_structure(base_path, structure)

print("Estructura creada con éxito.")
