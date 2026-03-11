import streamlit as st
import time

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="SGP | Núcleo GEN",
    page_icon="💎",
    layout="centered"
)

# CSS
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top right, #1e293b, #0f172a, #020617);
    color: white;
}

h1 {
    color: #38bdf8;
    text-align: center;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background: linear-gradient(90deg, #0ea5e9, #2563eb);
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# TÍTULO
st.markdown("<h1>SISTEMA DE GESTÃO ESTRATÉGICA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>NÚCLEO GEN | UNIDADE DE PROJETOS ESPECIAIS</p>", unsafe_allow_html=True)

st.divider()

# LOG
st.info("🌐 LOG DE ACESSO: protocolo de transição identificado. Aguardando confirmação de recebimento do cronograma.")

# PAINEL
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **DATA DO PROJETO**  
    21 MAR 2026
    """)

with col2:
    st.markdown("""
    **STATUS ATUAL**  
    EM ANDAMENTO
    """)

st.write("")
st.write("")

# BOTÃO
if st.button("CONFIRMAR RECEBIMENTO DO CRONOGRAMA"):

    with st.spinner("Validando protocolo..."):
        time.sleep(2)

    st.success("AUTORIZAÇÃO DE SEGURANÇA CONCLUÍDA.")

    st.markdown("""
    ### CHAVE DE SEGURANÇA BIOMÉTRICA

    **4 ÚLTIMOS DÍGITOS DO SEU CELULAR**

    (Obrigatório para liberação do cenário em 21/03)
    """)

    st.balloons()

    st.markdown(
        "<p style='text-align:center;color:#38bdf8;'>O seu novo capítulo está em processamento.</p>",
        unsafe_allow_html=True
    )
