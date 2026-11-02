
from fastapi import APIRouter, HTTPException, Request

from schemas import DadosEntrada, ResultadoPredicao
from services import realizar_predicao

router = APIRouter()


@router.get("/health")
def health(request: Request):
    modelo = getattr(request.app.state, "modelo", None)

    return {
        "status": "ok",
        "modelo_carregado": modelo is not None
    }


@router.post(
    "/predict",
    response_model=ResultadoPredicao
)
def predict(dados: DadosEntrada, request: Request):
    modelo = getattr(request.app.state, "modelo", None)

    if modelo is None:
        raise HTTPException(
            status_code=500,
            detail="Modelo não carregado"
        )

    return realizar_predicao(
        modelo,
        dados.model_dump()
    )
