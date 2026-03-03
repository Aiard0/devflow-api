
# 🚀 DevFlow API

A DevFlow API é uma aplicação backend desenvolvida com FastAPI e totalmente containerizada com Docker.  
Este projeto foi criado como apresentação final do Bootcamp de DevOps da Atlantico Avanti, demonstrando na prática a implementação de um fluxo completo de Integração Contínua e Entrega Contínua (CI/CD), além de deploy em nuvem.

---

## 🔧 Tecnologias Utilizadas

- Python 3.12
- FastAPI
- Uvicorn
- Docker
- Git e GitHub
- GitHub Actions (CI/CD)
- AWS EC2 (Deploy em Nuvem)
- Ansible (Provisionamento de Servidor)

---

## 🎯 Objetivos do Projeto

Este projeto demonstra:

- Containerização de aplicações com Docker
- Automação de build e execução
- Versionamento e controle de código com Git
- Pipeline de Integração Contínua (CI)
- Deploy automatizado em servidor cloud (CD)
- Aplicação prática de conceitos DevOps

---

## 🏗️ Arquitetura

Usuário → AWS EC2 → Container Docker → Aplicação FastAPI  
GitHub → Pipeline CI/CD → Deploy Automatizado → Servidor na Nuvem

---

## ▶️ Executando Localmente

```bash
docker build -t devflow .
docker run -p 8000:8000 devflow
