<div align="center">
  <h1>💱 Conversor de Moedas e Criptomoedas</h1>
  <p>Um sistema web resiliente e de alta performance para conversão em tempo real.</p>

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" />
</div>

<br>

## 📋 Sobre o Projeto

Este projeto tem como objetivo construir um sistema web de conversão de moedas tradicionais (Fiat) e criptomoedas em tempo real. Desenvolvido com foco em resiliência, o sistema inclui fallback de APIs, gráficos históricos e consumo otimizado de dados através de cache[cite: 1].

## 🏗️ Arquitetura e Tecnologias

O projeto está dividido em dois microsserviços principais:

### ⚙️ Backend (API)
- **Linguagem/Framework:** Python com FastAPI
- **Responsabilidade:** Normalização de dados (Adapter Pattern), cálculos de conversão cruzada, roteamento de fallback e sistema de cache[cite: 1].
- **Integrações:** AwesomeAPI (Moedas Fiat) e CoinGecko API (Criptomoedas)[cite: 1].

### 💻 Frontend (Interface)
- **Framework:** React / Next.js com TypeScript[cite: 1]
- **Estilização:** Tailwind CSS[cite: 1]
- **Responsabilidade:** Interface do usuário responsiva, renderização de gráficos interativos (histórico de 7 a 90 dias) e formatação dinâmica de moedas[cite: 1].

## 🚀 Como executar o projeto localmente

### 1. Clonar o repositório
```bash
git clone [https://github.com/SEU_USUARIO/conversor-criptomoedas.git](https://github.com/SEU_USUARIO/conversor-criptomoedas.git)

```

### 2. Configurar o Backend
```Bash
cd backend
python -m venv venv
```

#### Ative o ambiente virtual (Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate)
```Bash
pip install -r requirements.txt
Crie um arquivo .env baseado no .env.example com suas credenciais.

Para rodar a API:

Bash
uvicorn main:app --reload
```

### 3. Configurar o Frontend
```Bash
cd frontend
npm install
npm run dev
```

# 👨‍💻 Autores
## Desenvolvido por estudantes de Análise e Desenvolvimento de Sistemas:

### [Tiago Farias](https://github.com/tiagohfarias) - Engenharia de Backend & Integrações

### Gabriel Borba - Engenharia de Frontend & UX/UI
