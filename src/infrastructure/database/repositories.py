# Implementaci�n de repositorios
from domain.interfaces import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self):
        # Simula la base de datos en memoria
        self.database = []

    def save_user(self, name: str, email: str) -> dict:
        user_data = {"id": len(self.database) + 1, "name": name, "email": email}
        self.database.append(user_data)
        return user_data
