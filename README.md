# 🛡️ Tech Challenge 5 — Simulador de Risco Pedagógico

📌 **Repositório oficial:**
https://github.com/tech-challenge-5-fiap/tech-challenge5

---

## 🎯 Sobre o desafio

Este projeto foi desenvolvido no contexto do **Datathon FIAP — Tech Challenge 5**, baseado no case da **Associação Passos Mágicos**, uma organização com mais de 30 anos de atuação na transformação da vida de crianças e jovens em vulnerabilidade social por meio da educação.

A iniciativa busca utilizar dados educacionais (2022–2024) para gerar insights e soluções que contribuam para:

* melhoria do desempenho acadêmico
* redução da defasagem escolar
* prevenção da evasão

---

## 🎯 Objetivo do projeto

Construir uma solução de **Data Analytics + Machine Learning** capaz de:

* analisar indicadores educacionais
* identificar padrões de comportamento
* prever o risco de defasagem ou evasão
* apoiar decisões preventivas na instituição

---

## ❓ Perguntas de negócio

O projeto busca responder questões como:

* Evolução da defasagem dos alunos (IAN)
* Tendência do desempenho acadêmico (IDA)
* Relação entre engajamento (IEG) e desempenho
* Coerência entre autoavaliação (IAA) e resultados
* Impacto de fatores psicossociais (IPS)
* Influência dos indicadores no ponto de virada (IPV)
* Combinação de variáveis que explicam desempenho (INDE)
* Previsão de risco com Machine Learning

---

## 🧠 Solução desenvolvida

O projeto contempla:

* análise exploratória de dados
* tratamento e limpeza das bases
* engenharia de features
* construção de modelo preditivo
* aplicação web interativa com Streamlit

---

## 🤖 Modelo preditivo

Foi desenvolvido um modelo de **Machine Learning (Random Forest)** para prever risco educacional.

### 🔹 Variáveis utilizadas

* Idade
* Fase
* IAA, IEG, IPS, IPP
* IDA, IPV, IAN

### 🔹 Estratégia

* Classificação: risco vs não risco
* Limiar otimizado: **0.36**
* Foco em **recall alto (detecção de alunos em risco)**

---

## 💻 Aplicação Streamlit

A aplicação permite simular o perfil de um aluno e obter a **probabilidade de risco em tempo real**.

### 🔹 Funcionalidades

* Entrada manual dos indicadores
* Previsão automática de risco
* Classificação visual (baixo risco / alerta)
* Interface amigável para uso educacional

### 🔗 Acesse o app:

https://tech-challenge5-nzyvrm4eesrur8xrgujj8x.streamlit.app

---

## 📂 Estrutura do projeto

```
├── app.py
├── Datathon.ipynb
├── modelo.ipynb
├── BASE DE DADOS PEDE 2024 - DATATHON.xlsx
├── requirements.txt
└── README.md
```

---

## ▶️ Como executar localmente

```bash
git clone https://github.com/tech-challenge-5-fiap/tech-challenge5.git
cd tech-challenge5

pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Entregáveis

Este projeto atende aos requisitos do desafio:

* ✔ Código no GitHub
* ✔ Notebook com modelo preditivo
* ✔ Aplicação em Streamlit (deploy realizado)
* ✔ Storytelling analítico
* ✔ Modelo de previsão de risco

---

## 🛠️ Tecnologias utilizadas

* Python
* Streamlit
* Pandas / NumPy
* Scikit-learn
* Jupyter Notebook

---

## 👥 Integrantes

Evandro, Jonas, Leonardo, Luiz Felipe e Robson

---

## 📌 Considerações finais

Este projeto demonstra como dados e Machine Learning podem ser utilizados para gerar impacto social real, auxiliando na identificação precoce de alunos em risco e apoiando decisões educacionais mais assertivas.
