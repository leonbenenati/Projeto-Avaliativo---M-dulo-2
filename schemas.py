
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal


class DadosEntrada(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tipo: Literal["L", "M", "H"] = Field(
    ...,
    description="Tipo da máquina: L, M ou H"
)

    temperatura_ar_k: float = Field(
        ...,
        description="Temperatura do ar em Kelvin"
    )

    temperatura_processo_k: float = Field(
        ...,
        description="Temperatura do processo em Kelvin"
    )

    velocidade_rotacao_rpm: float = Field(
        ...,
        ge=0,
        description="Velocidade de rotação em RPM"
    )

    torque_nm: float = Field(
        ...,
        ge=0,
        description="Torque em Newton-metro"
    )

    desgaste_ferramenta_min: float = Field(
        ...,
        ge=0,
        description="Desgaste da ferramenta em minutos"
    )


class ResultadoPredicao(BaseModel):
    falha_maquina: int = Field(
        ...,
        ge=0,
        le=1,
        description="Predição: 0 para ausência de falha e 1 para falha"
    )

    probabilidade_falha: float = Field(
        ...,
        ge=0,
        le=1,
        description="Probabilidade estimada de falha"
    )
