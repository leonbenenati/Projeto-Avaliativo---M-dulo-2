
from contextlib import asynccontextmanager
from pathlib import Path

import joblib
from fastapi import FastAPI

from routers import router


CAMINHO_MODELO = Path(__file__).parent / "modelo_falhas.joblib"


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.modelo = joblib.load(CAMINHO_MODELO)

    yield

    app.state.modelo = None


app = FastAPI(
    title="API de Predição de Falhas em Máquinas",
    description="API para identificar falhas em máquinas industriais usando LightGBM.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router)
