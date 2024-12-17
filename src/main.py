import sys
import os

# Agregar la ruta del directorio `src` al PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.v1.routers.user_router import router as user_router
from fastapi import FastAPI
from config.container import AppContainer

app = FastAPI(debug=True)

# Inicializa y conecta el contenedor de dependencias
container = AppContainer()
container.wire(modules=["api.v1.routers.user_router"])
app.container = container

app.include_router(user_router, prefix="/users", tags=["Users"])

# for route in app.routes:
#     print(route.path, route.name)

