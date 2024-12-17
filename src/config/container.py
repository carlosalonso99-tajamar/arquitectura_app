# Contenedor para inyecci�n de dependencias
from dependency_injector import containers, providers
from infrastructure.database.repositories import UserRepository
from use_cases.create_user import CreateUserUseCase

class AppContainer(containers.DeclarativeContainer):
    user_repository = providers.Factory(UserRepository)
    create_user_use_case = providers.Factory(
        CreateUserUseCase,
        repository=user_repository
    )
