
# 🚀 DevFlow API

A DevFlow API é uma aplicação backend desenvolvida com FastAPI e totalmente containerizada com Docker.  
Este projeto foi criado como apresentação final do Bootcamp de DevOps da Atlantico Avanti, demonstrando na prática a implementação de um fluxo completo de Integração Contínua e Entrega Contínua (CI/CD), além de deploy em nuvem.

---

## 🧩 O Problema

> *Uma startup de tecnologia chamada **DevFlow** possui uma pequena equipe de desenvolvedores que mantém uma API interna usada por outros times da empresa. O processo de deploy era feito manualmente: um desenvolvedor conectava via SSH no servidor, fazia o pull do código, reinstalava as dependências e reiniciava o processo na mão. Esse processo demorava cerca de 20 minutos, era propenso a erros humanos e dependia de uma única pessoa que "sabia como fazer". Em um dia crítico, um bug foi corrigido às 23h e ninguém conseguiu fazer o deploy porque essa pessoa estava indisponível. O sistema ficou fora do ar por horas.*
>
> *A solução foi reestruturar completamente o fluxo de entrega: containerizar a aplicação com Docker, automatizar o provisionamento do servidor com Ansible e criar um pipeline de CI/CD com GitHub Actions que, a cada push na branch principal, constrói a imagem, publica no Docker Hub e faz o deploy automático na EC2 via SSH — sem intervenção humana, em menos de 2 minutos.*

---

## 🔧 Tecnologias Utilizadas

- Python 3.12
- FastAPI
- Uvicorn
- Docker e Docker Hub
- Git e GitHub
- GitHub Actions (CI/CD)
- AWS EC2 — Ubuntu Server 24.04 LTS
- Ansible (Provisionamento de Servidor)

---

## 🎯 Objetivos do Projeto

Este projeto demonstra:

- Containerização de aplicações com Docker
- Build e publicação de imagens no Docker Hub via CI
- Versionamento e controle de código com Git
- Pipeline de Integração Contínua e Entrega Contínua (CI/CD)
- Provisionamento de servidor com Ansible
- Deploy automatizado em servidor cloud via SSH

---

## 🏗️ Arquitetura

```
Usuário → AWS EC2 → Container Docker → Aplicação FastAPI

GitHub (push main)
  └── CI: docker build → push Docker Hub
  └── CD: SSH na EC2 → docker pull → docker run
```

---

## 📁 Estrutura do Projeto

```
devflow-api/
├── app/
│   ├── main.py               # Entrypoint da aplicação FastAPI
│   └── routes/
│       └── example.py        # Rotas de exemplo
├── ansible/
│   ├── ansible.cfg
│   ├── inventories/
│   │   └── hosts.ini         # IP e credenciais da EC2
│   └── playbooks/
│       └── docker.yml        # Provisionamento: instala Docker na EC2
├── .github/
│   └── workflows/
│       ├── ci-cd.yml         # Build Docker Hub + Deploy na EC2 (push → main)
│       └── infra.yml         # Provisionamento Ansible (disparo manual)
├── Dockerfile
├── requirements-app.txt      # Dependências de runtime da API
├── requirements.txt          # Dependências de desenvolvimento local
└── .gitignore
```

---

## ▶️ Executando Localmente

```bash
docker build -t devflow-api .
docker run -p 8000:8000 devflow-api
```

Acesse em: http://localhost:8000

---

## ⚙️ CI/CD — GitHub Actions

### Workflow `ci-cd.yml` (automático — push na `main`)

1. **Build**: faz `docker build` e publica a imagem no Docker Hub
2. **Deploy**: conecta na EC2 via SSH, faz `docker pull` e reinicia o container

### Workflow `infra.yml` (manual — `workflow_dispatch`)

Roda o playbook Ansible `docker.yml` para provisionar o servidor:
- Atualiza pacotes do sistema
- Instala Docker Engine e Docker Compose plugin
- Habilita o serviço Docker
- Adiciona o usuário `ubuntu` ao grupo `docker`

---

## 🔐 Secrets necessários no GitHub

Configure em: **Settings → Secrets and variables → Actions**

| Secret | Descrição |
|---|---|
| `DOCKERHUB_USERNAME` | Usuário do Docker Hub |
| `DOCKERHUB_TOKEN` | Token de acesso gerado no Docker Hub |
| `EC2_SSH_KEY` | Conteúdo do `.pem` codificado em base64 (`base64 -w 0 ~/.ssh/DevTest.pem`) |

---

## 🌐 Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Verifica se a API está no ar |
| GET | `/health` | Health check |
| GET | `/ping` | Rota de exemplo |
