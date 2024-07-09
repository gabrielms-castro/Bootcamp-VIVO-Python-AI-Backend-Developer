from fastapi import APIRouter

from workoutapi.atleta.controller import router as atleta
from workoutapi.categoria.controller import router as categoria
from workoutapi.centro_treinamento.controller import router as centro_treinamento

api_router = APIRouter()

# Criando rota para atletas
api_router.include_router(atleta, prefix="/atletas", tags=["atletas"])
api_router.include_router(categoria, prefix="/categorias", tags=["categorias"])
api_router.include_router(
    centro_treinamento, prefix="/centros_treinamento", tags=["centros_treinamento"]
)
