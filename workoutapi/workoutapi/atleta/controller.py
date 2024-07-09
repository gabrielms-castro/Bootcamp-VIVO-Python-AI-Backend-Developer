from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, status

from workoutapi.atleta.schemas import AtletaIn, AtletaOut
from workoutapi.atleta.models import AtletaModel
from workoutapi.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    path="/",
    summary="Criar novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut
    )
async def post(
    db_session: DatabaseDependency,
    atleta_in: AtletaIn = Body(...)
    ):
    
    atleta_out = AtletaOut(id=uuid4(), created_at=datetime.now(datetime.UTC), **atleta_in.model_dump())
    atleta_model = AtletaModel(**atleta_out.model_dump())
    
    db_session.add(atleta_model)
    await db_session.commit()
    
    return atleta_out
    
 