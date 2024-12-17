# Contratos para repositorios y servicios
from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    def save_user(self, name: str, email: str) -> dict:
        """Guarda un usuario y devuelve sus datos."""
        pass

from typing import Dict

class CreateUserUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, name: str, email: str) -> Dict:
        """Ejecuta el caso de uso para crear un usuario."""
        pass
