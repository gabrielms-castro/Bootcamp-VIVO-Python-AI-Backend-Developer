from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workoutapi.contrib.models import BaseModel


class CentroTreinamentoModel(BaseModel):
    __tablename__ = "centros_treinamento"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    atleta: Mapped["AtletaModel"] = relationship(back_populates="categoria")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
