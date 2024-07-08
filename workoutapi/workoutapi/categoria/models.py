from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Datetime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from workoutapi.atleta.models import AtletaModel


class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')
    created_at: Mapped[datetime] = mapped_column(Datetime, nullable=False) 