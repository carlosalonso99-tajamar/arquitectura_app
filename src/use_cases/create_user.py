# Caso de uso 1: Crear usuario
from domain.interfaces import UserRepositoryInterface, CreateUserUseCaseInterface
from domain.entities import User

class CreateUserUseCase(CreateUserUseCaseInterface):
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, name: str, email: str) -> dict:
        # Validar y crear la entidad de usuario
        user = User(name=name, email=email)
        user.validate()

        # Guardar el usuario a través del repositorio
        saved_user = self.repository.save_user(name=user.name, email=user.email)
        return saved_user
