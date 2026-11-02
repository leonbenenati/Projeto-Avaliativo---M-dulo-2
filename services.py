
import pandas as pd


def criar_features(dados: dict) -> pd.DataFrame:
    df = pd.DataFrame([dados])

    df["potencia"] = (
        df["velocidade_rotacao_rpm"] *
        df["torque_nm"]
    )

    df["delta_temperatura"] = (
        df["temperatura_processo_k"] -
        df["temperatura_ar_k"]
    )

    df["desgaste_torque"] = (
        df["desgaste_ferramenta_min"] *
        df["torque_nm"]
    )

    return df


def realizar_predicao(modelo, dados: dict) -> dict:
    entrada = criar_features(dados)

    predicao = int(modelo.predict(entrada)[0])

    probabilidade = float(
        modelo.predict_proba(entrada)[0, 1]
    )

    return {
        "falha_maquina": predicao,
        "probabilidade_falha": probabilidade
    }
