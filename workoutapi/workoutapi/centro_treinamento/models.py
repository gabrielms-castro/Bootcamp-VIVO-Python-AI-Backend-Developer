from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Datetime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from workoutapi.atleta.models import AtletaModel


class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')
    created_at: Mapped[datetime] = mapped_column(Datetime, nullable=False) 