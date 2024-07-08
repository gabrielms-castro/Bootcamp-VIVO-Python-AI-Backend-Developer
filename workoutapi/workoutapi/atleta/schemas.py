from typing import Annotated

from pydantic import Field, PositiveFloat
from workoutapi.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do Atleta", example="Pedro", max_length=50)
    ]
    cpf: Annotated[
        str, Field(description="CPF do Atleta", example="01234567890", max_length=11)
    ]
    idade: Annotated[int, Field(description="Idade do Atleta", example=30)]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", example=87.5)]
    altura: Annotated[
        PositiveFloat, Field(description="Altura do Atleta", example=1.82)
    ]
    sexo: Annotated[
        str, Field(description="Altura do Atleta", example="M", max_length=1)
    ]
