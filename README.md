# flask-cicd-docker

API simples em Flask, criada para as atividades formativas de DevOps (CI/CD com GitHub Actions + Docker).

## Rodando localmente (sem Docker)

```bash
pip install -r requirements-dev.txt
python app.py
```

Acesse http://localhost:5000 e http://localhost:5000/health.

## Rodando com Docker

```bash
docker build -t flask-cicd-docker .
docker run -d -p 5000:5000 --name flask-app flask-cicd-docker
```

Acesse http://localhost:5000/health e confira com `docker ps`.

## Testes

```bash
pytest -v
```

## CI/CD

- **CI** (`.github/workflows/ci.yml`): instala dependências e roda os testes a cada push/PR na `main`.
- **CD** (`.github/workflows/cd.yml`): builda a imagem Docker, sobe o container e testa o endpoint `/health`.
- **Publish to Docker Hub** (`.github/workflows/docker-publish.yml`, opcional): publica a imagem no Docker Hub a cada push na `main`, se os secrets `DOCKERHUB_USERNAME` e `DOCKERHUB_TOKEN` estiverem configurados.
