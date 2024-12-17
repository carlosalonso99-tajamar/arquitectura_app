# Rutas relacionadas con usuarios
from fastapi import APIRouter, Depends, HTTPException, Body
from dependency_injector.wiring import Provide, inject
from domain.interfaces import CreateUserUseCaseInterface
from config.container import AppContainer

router = APIRouter()

@router.post("/")
@inject
def create_user(
    name: str = Body(),
    email: str = Body(),
    use_case: CreateUserUseCaseInterface = Depends(Provide[AppContainer.create_user_use_case])
):
    try:
        user = use_case.execute(name=name, email=email)
        return {"message": "User created successfully", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
