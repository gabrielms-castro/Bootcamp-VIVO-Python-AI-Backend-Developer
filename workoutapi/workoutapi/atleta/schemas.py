from typing import Annotated, Optional

from pydantic import Field, PositiveFloat

from workoutapi.contrib.schemas import BaseSchema, OutMixIn
from workoutapi.categoria.schemas import CategoriaIn
from workoutapi.centro_treinamento.schemas import CentroTreinamentoAtleta


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

    categoria: Annotated[
        CategoriaIn, Field(description="Categoria do Atleta")
    ]
    
    centro_treinamento: Annotated[
        CentroTreinamentoAtleta, Field(description="Centro de Treinamento do Atleta")
    ]


class AtletaIn(Atleta):
    pass


class AtletaOut(AtletaIn, OutMixIn):
    pass
 
 
class AtletaUpdate(BaseSchema):
    nome: Annotated[
        Optional[str], Field(None, description="Nome do Atleta", example="Pedro", max_length=50)
    ]
    idade: Annotated[Optional[int], Field(None, description="Idade do Atleta", example=30)]
