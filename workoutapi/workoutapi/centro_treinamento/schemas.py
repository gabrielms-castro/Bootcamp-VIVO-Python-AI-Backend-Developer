from typing import Annotated

from pydantic import Field

from workoutapi.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT Joaquim Peixoto', max_length=20)] 
    proprietario: Annotated[str, Field(description='Nome do Proprietário do CT', example='Joaquim Peixoto', max_length=30)] 
    endereco: Annotated[str, Field(description='Endereço do CT', example='Av. Júlio Buono, 2028', max_length=60)] 