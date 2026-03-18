import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Simulador de Risco PM",
    page_icon="🛡️",
    layout="centered"
)

# --- 2. MOTOR DE INTELIGÊNCIA (LIMPEZA E TREINO) ---
@st.cache_resource
def treinar_modelo_robusto():
    try:
        # Carregamento das bases originais
        df_2023 = pd.read_excel('BASE DE DADOS PEDE 2024 - DATATHON.xlsx', sheet_name='PEDE2023')
        df_2024 = pd.read_excel('BASE DE DADOS PEDE 2024 - DATATHON.xlsx', sheet_name='PEDE2024')
    except Exception as e:
        st.error(f"Erro ao carregar arquivos: {e}")
        return None

    def clean_numeric(v):
        if pd.isna(v): return np.nan
        try: return float(str(v).replace(',', '.'))
        except: return np.nan

    def tratar_idade(v):
        if pd.isna(v): return np.nan
        s = str(v).strip()
        if ' ' in s: s = s.split(' ')[0]
        if '-' in s: s = s.split('-')[-1]
        try: return float(s)
        except: return np.nan

    def tratar_fase(v):
        s = str(v).upper()
        if 'ALFA' in s: return 0
        n = "".join(filter(str.isdigit, s))
        return float(n) if n else 0.0

    # Processamento 2023 (Entradas/Features)
    df_23 = df_2023.copy()
    df_23['Idade_Limpa'] = df_23['Idade'].apply(tratar_idade)
    df_23['Fase_N'] = df_23['Fase'].apply(tratar_fase)
    
    indices = ['IAA', 'IEG', 'IPS', 'IPP', 'IDA', 'IPV', 'IAN']
    for col in indices + ['Defasagem']:
        df_23[col] = df_23[col].apply(clean_numeric)
    
    # Processamento 2024 (Status Futuro)
    df_24 = df_2024[['RA', 'Defasagem']].copy()
    df_24['Def_24'] = df_24['Defasagem'].apply(clean_numeric)
    
    # Cruzamento Left Join (Preserva os evadidos)
    df = pd.merge(df_23, df_24[['RA', 'Def_24']], on='RA', how='left')
    
    # Target (1 = Risco): O aluno defasou (Def_24 > 0) OU evadiu/sumiu (Def_24 é NaN)
    df['Target_Risco'] = ((df['Def_24'] > 0) | (df['Def_24'].isna())).astype(int)
    
    features = ['Idade_Limpa', 'IAA', 'IEG', 'IPS', 'IPP', 'IDA', 'IPV', 'IAN', 'Fase_N']
    df_train = df.dropna(subset=features)
    
    X = df_train[features]
    y = df_train['Target_Risco']
    
    # Modelo Otimizado (Tunado conforme Jupyter Notebook)
    model = RandomForestClassifier(
        n_estimators=400,             
        max_depth=10,                 
        min_samples_leaf=2,           
        class_weight='balanced_subsample', 
        random_state=42
    )
    model.fit(X, y)
    return model

# Iniciar modelo
with st.spinner("Sincronizando modelos preditivos..."):
    modelo_pm = treinar_modelo_robusto()

# --- 3. INTERFACE STREAMLIT ---
st.title("🛡️ Simulador de Risco Pedagógico")
st.markdown("### Prevenção de Defasagem e Evasão Escolar")

if modelo_pm:
    with st.form("form_avaliador"):
        st.subheader("📋 Ficha de Avaliação do Aluno")
        
        col1, col2 = st.columns(2)
        with col1:
            idade = st.number_input("Idade", 6, 25, 12)
            fase = st.slider("Fase (0=Alfa, 1-7=Fases, 8=Univ.)", 0, 8, 2)
            ian = st.slider("IAN (Adequação de Nível)", 0.0, 10.0, 7.0)
            ipp = st.slider("IPP (Ponto de Partida)", 0.0, 10.0, 7.0)
            ida = st.slider("IDA (Aprendizagem/Notas)", 0.0, 10.0, 7.0)

        with col2:
            ieg = st.slider("IEG (Engajamento)", 0.0, 10.0, 7.0)
            ipv = st.slider("IPV (Ponto de Virada)", 0.0, 10.0, 7.0)
            ips = st.slider("IPS (Psicossocial)", 0.0, 10.0, 7.0)
            iaa = st.slider("IAA (Autoavaliação)", 0.0, 10.0, 7.0)

        botao = st.form_submit_button("PROCESSAR ANÁLISE")

    # --- 4. LÓGICA DE PREDIÇÃO (LIMIAR OTIMIZADO) ---
    if botao:
        entrada = np.array([[idade, iaa, ieg, ips, ipp, ida, ipv, ian, fase]])
        
        probabilidade = modelo_pm.predict_proba(entrada)[0][1]
        risco_percentual = probabilidade * 100
        
        st.divider()
        
        # UTILIZANDO O LIMIAR MATEMÁTICO DESCOBERTO (0.36 = 36%)
        if probabilidade >= 0.36:
            st.error(f"## 🚨 ALERTA DE RISCO")
            st.warning(f"**Atenção:** O modelo preditivo detectou perfil compatível com defasagem ou evasão. Intervenção sugerida.")
        else:
            st.success("## ✅ BAIXO RISCO")
            st.write("O modelo prevê que o aluno se manterá estável e ativo na instituição.")

        st.progress(probabilidade)
        st.caption("Modelo preditivo blindado contra viés de sobrevivência. Limiar otimizado (Recall=75%) para maximizar a retenção de alunos.")
        
        st.metric("Probabilidade de Risco", f"{risco_percentual:.2f}%")

        
        st.info("""
        🔎 **Sobre o modelo:**
        Este simulador utiliza Random Forest, um modelo de Machine Learning que identifica padrões
        nos dados históricos para prever risco de evasão ou defasagem escolar.

        O modelo foi ajustado para priorizar a detecção de alunos em risco (recall alto).
        """)