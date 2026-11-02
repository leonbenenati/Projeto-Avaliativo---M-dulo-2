# Predição de Falhas em Máquinas Industriais

## 1. Resumo do projeto

Este projeto utiliza Machine Learning para identificar a possibilidade de falhas em máquinas industriais a partir de variáveis operacionais, como temperatura, velocidade de rotação, torque e desgaste da ferramenta.

Foi desenvolvido um modelo de classificação utilizando LightGBM e uma API Web com FastAPI para disponibilizar as predições.

## 2. Origem dos dados e do modelo

O modelo foi desenvolvido a partir da base de dados de manutenção preditiva utilizada no projeto.

- **Base de dados:** manutencao_preditiva.csv
- **Modelo:** LightGBM
- **Artefato serializado:** modelo_falhas.joblib

A base de dados contém informações sobre as condições operacionais das máquinas e a ocorrência de falhas.

**Origem da base:** [Inserir o link da fonte original dos dados.]

## 3. Tecnologias utilizadas

- Python
- Pandas
- Scikit-learn
- LightGBM
- FastAPI
- Pydantic
- Uvicorn
- Joblib

As versões das bibliotecas estão especificadas no arquivo `requirements.txt`.

## 4. Estrutura do projeto

```text
.
├── main.py
├── routers.py
├── schemas.py
├── services.py
├── modelo_falhas.joblib
├── manutencao_preditiva.csv
├── requirements.txt
├── README.md
└── Projeto_Avaliativo_Módulo_2.ipynb
```

## 5. Desenvolvimento do modelo

O desenvolvimento foi realizado no Google Colab, incluindo as etapas de preparação dos dados, engenharia de atributos, divisão entre treino e teste, pré-processamento e treinamento do modelo.

Foi utilizada uma busca de hiperparâmetros com validação cruzada estratificada para selecionar uma configuração do LightGBM com foco no F1-Score.

O modelo final foi avaliado utilizando os dados de teste.

### Métricas do modelo final

| Métrica | Resultado |
|---|---:|
| Acurácia | 98,93% |
| Precisão | 90,70% |
| Recall | 76,47% |
| F1-Score | 82,80% |
| ROC-AUC | 97,52% |

O modelo foi serializado utilizando Joblib para permitir sua reutilização pela API.

## 6. Instalação e execução

### Pré-requisitos

Python e pip instalados.

### Instalar as dependências

```bash
pip install -r requirements.txt
```

### Executar a API

Na pasta do projeto, execute:

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

## 7. Endpoints

### GET /health

Verifica se o serviço está ativo e se o modelo foi carregado corretamente.

Exemplo de resposta:

```json
{
  "status": "ok",
  "modelo_carregado": true
}
```

### POST /predict

Recebe os dados operacionais de uma máquina e retorna a predição de falha e sua probabilidade estimada.

Exemplo de requisição:

```json
{
  "tipo": "M",
  "temperatura_ar_k": 300.0,
  "temperatura_processo_k": 310.0,
  "velocidade_rotacao_rpm": 1500.0,
  "torque_nm": 40.0,
  "desgaste_ferramenta_min": 100.0
}
```

Exemplo de resposta:

```json
{
  "falha_maquina": 0,
  "probabilidade_falha": 0.000556
}
```

Os valores da resposta são ilustrativos. A predição real depende dos dados enviados à API.

O campo `falha_maquina` indica a classificação do modelo: 0 para ausência de falha e 1 para falha.

A probabilidade representa a estimativa do modelo para a ocorrência de falha.

## 8. Validação e tratamento de erros

A API utiliza esquemas Pydantic para validar os dados de entrada e saída.

Valores inválidos, como categorias desconhecidas ou números fora dos limites permitidos, são rejeitados antes de serem enviados ao modelo.

Principais códigos HTTP:

- `200 OK`: requisição processada com sucesso.
- `422 Unprocessable Entity`: dados inválidos.
- `500 Internal Server Error`: erro interno ou modelo indisponível.

## 9. Evidências

- **Repositório GitHub:** [Inserir link do repositório.]
- **Vídeo de demonstração:** [Inserir link do Google Drive.]
