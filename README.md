# Disease Prediction API (Flask)

API simples em **Python + Flask** para **predizer se um paciente possui predisposição a uma doença**, usando um modelo de Machine Learning treinado com o **Breast Cancer Dataset** do `scikit-learn`.

Este projeto é **educacional**, focado em aprender:

* Estrutura de uma API
* Organização de código
* Integração com Machine Learning
* Boas práticas iniciais para projetos backend

---

## Tecnologias usadas

* Python 3.10+
* Flask
* Scikit-learn
* VSCode
* Git / GitHub

---

## Estrutura do projeto

```
app/
 ├── routes/
 │    └── predict.py              # Rotas da API
 ├── services/
 │    └── prediction_service.py   # Lógica de predição
 ├── model/
 │    ├── dataset.py              # Carregamento do dataset
 │    └── __init__.py
 ├── config.py                    # Configurações da aplicação
 └── main.py                      # Ponto de entrada da API
```

---

## O que cada parte faz (resumo rápido)

* **main.py**
  Inicia o Flask e registra as rotas.

* **routes/**
  Define os endpoints da API (`/`, `/status`, `/predict`).

* **services/**
  Contém a lógica de negócio (onde o modelo é usado para prever).

* **model/**
  Responsável pelos dados e, futuramente, pelo treino do modelo.

* **config.py**
  Centraliza configurações da aplicação.

---

## Como rodar o projeto

1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/disease-prediction-api.git
cd disease-prediction-api
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Instale as dependências

```bash
pip install flask scikit-learn
```

4. Execute a aplicação

```bash
python -m app.main
```

A API ficará disponível em:

```
http://127.0.0.1:5000
```

---

## Endpoints disponíveis

### Verificar se a API está ativa

```
GET /
```

Resposta:

```json
{
  "message": "API de predição está ativa"
}
```

---

### Status da API

```
GET /status
```

Resposta:

```json
{
  "status": "ok"
}
```

---

### Fazer uma predição

```
POST /predict
```

#### Exemplo de JSON para o Postman

```json
{
  "features": [
    17.99, 10.38, 122.8, 1001.0, 0.1184,
    0.2776, 0.3001, 0.1471, 0.2419, 0.07871,
    1.095, 0.9053, 8.589, 153.4, 0.006399,
    0.04904, 0.05373, 0.01587, 0.03003, 0.006193,
    25.38, 17.33, 184.6, 2019.0, 0.1622,
    0.6656, 0.7119, 0.2654, 0.4601, 0.1189
  ]
}
```

Resposta:

```json
{
  "prediction": false
}
```

* `true` → predisposição detectada
* `false` → sem predisposição

---

## Observações importantes

* O modelo espera **30 features** exatamente
* Este projeto **não é médico**, é apenas educacional
* O foco é aprender **API + ML + organização de código**

---

## Próximos passos (futuro)

* Treinar e salvar o modelo (`train.py`)
* Persistir modelo em arquivo
* Adicionar testes automatizados
* Containerizar com Docker
* Deploy em servidor

---

Se quiser, no próximo passo posso:

* 🧠 **Redesenhar essa estrutura de forma ainda mais simples**
* 🧪 **Adicionar testes**
* 🤖 **Explicar melhor a parte de Machine Learning**
* 🚀 **Preparar para Docker / deploy**

É só dizer 👍
