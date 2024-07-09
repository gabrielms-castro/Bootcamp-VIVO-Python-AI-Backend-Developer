from typing import Annotated

from pydantic import Field, UUID4

from workoutapi.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do Centro de Treinamento",
            example="CT Joaquim Peixoto",
            max_length=20,
        ),
    ]
    proprietario: Annotated[
        str,
        Field(
            description="Nome do Proprietário do CT",
            example="Joaquim Peixoto",
            max_length=30,
        ),
    ]
    endereco: Annotated[
        str,
        Field(
            description="Endereço do CT", example="Av. Júlio Buono, 2028", max_length=60
        ),
    ]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do Centro de Treinamento",
            example="CT Joaquim Peixoto",
            max_length=20,
        ),
    ]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do Centro de Treinamento")]
