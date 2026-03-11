import streamlit as st
import time

# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="SGP | Núcleo GEN",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# ESTADOS
# ==========================================================
if "etapa" not in st.session_state:
    st.session_state.etapa = 1

if "autorizado" not in st.session_state:
    st.session_state.autorizado = False

TOKEN_CORRETO = "1234"  # troque aqui pelos 4 últimos dígitos

# ==========================================================
# CSS GLOBAL
# ==========================================================
st.markdown("""
<style>
    #MainMenu, footer, header {
        visibility: hidden;
    }

    .stApp {
        background:
            radial-gradient(circle at top right, rgba(56,189,248,0.12), transparent 25%),
            radial-gradient(circle at bottom left, rgba(37,99,235,0.10), transparent 25%),
            linear-gradient(180deg, #020617 0%, #0f172a 45%, #020617 100%);
        color: #e2e8f0;
    }

    .block-container {
        max-width: 760px;
        padding-top: 2.5rem;
        padding-bottom: 2rem;
    }

    .hero-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #e2e8f0;
        letter-spacing: 1.5px;
        margin-bottom: 0.3rem;
        text-shadow: 0 0 18px rgba(56, 189, 248, 0.15);
    }

    .hero-subtitle {
        text-align: center;
        font-size: 0.95rem;
        color: #38bdf8;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 1.4rem;
        font-family: monospace;
    }

    .glass-card {
        background: rgba(15, 23, 42, 0.78);
        border: 1px solid rgba(56, 189, 248, 0.30);
        border-radius: 20px;
        padding: 28px 24px;
        box-shadow:
            0 0 0 1px rgba(56,189,248,0.05),
            0 0 30px rgba(56,189,248,0.08),
            0 20px 60px rgba(0,0,0,0.35);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }

    .log-box {
        background: rgba(2, 6, 23, 0.65);
        border: 1px solid rgba(56, 189, 248, 0.22);
        border-radius: 14px;
        padding: 16px;
        color: #cbd5e1;
        font-size: 0.96rem;
        line-height: 1.6;
    }

    .small-label {
        color: #38bdf8;
        font-size: 0.78rem;
        letter-spacing: 1.4px;
        text-transform: uppercase;
        margin-bottom: 4px;
    }

    .big-value {
        color: #ffffff;
        font-size: 1.15rem;
        font-weight: 700;
        margin: 0;
    }

    .mini-panel {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 14px;
        padding: 16px;
    }

    .center-text {
        text-align: center;
    }

    .token-card {
        background: linear-gradient(180deg, rgba(15,23,42,0.95), rgba(2,6,23,0.95));
        border: 1px solid rgba(56,189,248,0.28);
        border-left: 5px solid #38bdf8;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 0 24px rgba(56,189,248,0.08);
    }

    .token-title {
        color: #94a3b8;
        font-size: 0.85rem;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }

    .token-main {
        color: #38bdf8;
        font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .token-sub {
        color: #64748b;
        font-size: 0.9rem;
    }

    .final-status {
        color: #38bdf8;
        font-family: monospace;
        font-size: 0.92rem;
        letter-spacing: 1px;
        text-align: center;
        margin-bottom: 20px;
    }

    .final-highlight {
        text-align: center;
        color: #7dd3fc;
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 20px;
    }

    .divider-line {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(56,189,248,0.45), transparent);
        margin: 22px 0;
    }

    .final-main {
        text-align: center;
        color: white;
        font-size: 2.2rem;
        font-weight: 800;
        line-height: 1.25;
        margin-bottom: 10px;
        text-shadow: 0 0 16px rgba(56,189,248,0.10);
    }

    .final-footer {
        text-align: center;
        color: #94a3b8;
        font-family: monospace;
        font-size: 0.78rem;
        margin-top: 28px;
    }

    .stTextInput > div > div > input {
        background-color: rgba(15,23,42,0.95) !important;
        color: white !important;
        border: 1px solid rgba(56,189,248,0.35) !important;
        border-radius: 12px !important;
        height: 52px !important;
        text-align: center !important;
        font-size: 1rem !important;
        letter-spacing: 5px !important;
    }

    .stTextInput label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
    }

    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 12px;
        border: none;
        font-weight: 800;
        font-size: 1rem;
        background: linear-gradient(90deg, #0ea5e9, #2563eb);
        color: white;
        box-shadow: 0 8px 24px rgba(37,99,235,0.35);
        transition: all 0.25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(37,99,235,0.45);
    }

    .message-bottom {
        text-align: center;
        color: #38bdf8;
        font-size: 0.98rem;
        margin-top: 18px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================================
# TÍTULO FIXO
# ==========================================================
st.markdown('<div class="hero-title">SISTEMA DE GESTÃO ESTRATÉGICA</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">NÚCLEO GEN | UNIDADE DE PROJETOS ESPECIAIS</div>', unsafe_allow_html=True)

# ==========================================================
# ETAPA 1 - INTRODUÇÃO
# ==========================================================
if st.session_state.etapa == 1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown("""
        <div class="log-box">
            🌐 <b>LOG DE ACESSO:</b> protocolo de transição identificado.<br>
            Aguardando confirmação de recebimento do cronograma para liberação da próxima etapa.
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="mini-panel">
                <div class="small-label">DATA DO PROJETO</div>
                <p class="big-value">21 MAR 2026</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="mini-panel">
                <div class="small-label">STATUS ATUAL</div>
                <p class="big-value">EM ANDAMENTO</p>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    if st.button("CONFIRMAR RECEBIMENTO DO CRONOGRAMA"):
        with st.spinner("Validando protocolo..."):
            time.sleep(1.5)
        st.session_state.etapa = 2
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================================
# ETAPA 2 - REVELAÇÃO DO TOKEN
# ==========================================================
elif st.session_state.etapa == 2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.success("AUTORIZAÇÃO DE SEGURANÇA CONCLUÍDA.")

    st.markdown("""
        <div class="token-card">
            <div class="token-title">CHAVE DE SEGURANÇA BIOMÉTRICA</div>
            <div class="token-main">4 ÚLTIMOS DÍGITOS DO SEU CELULAR</div>
            <div class="token-sub">(Obrigatório para liberação do cenário em 21/03)</div>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="message-bottom">O seu novo capítulo está em processamento.</div>', unsafe_allow_html=True)
    st.write("")

    if st.button("PROSSEGUIR PARA VALIDAÇÃO"):
        st.session_state.etapa = 3
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================================
# ETAPA 3 - LOGIN
# ==========================================================
elif st.session_state.etapa == 3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown("""
        <div class="center-text" style="color:#cbd5e1; font-size:1rem; margin-bottom:16px;">
            Insira o token de acesso para validar o protocolo final.
        </div>
    """, unsafe_allow_html=True)

    token = st.text_input(
        "TOKEN DE ACESSO",
        type="password",
        max_chars=4,
        placeholder="••••"
    )

    if st.button("VALIDAR PROTOCOLO FINAL"):
        if token == TOKEN_CORRETO:
            with st.spinner("Autenticando ambiente..."):
                time.sleep(1.2)
            st.session_state.autorizado = True
            st.session_state.etapa = 4
            st.rerun()
        else:
            st.error("Token inválido. Verifique e tente novamente.")

    st.write("")
    if st.button("VOLTAR"):
        st.session_state.etapa = 2
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================================
# ETAPA 4 - TELA FINAL
# ==========================================================
elif st.session_state.etapa == 4:
    st.balloons()

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown("""
        <div class="final-status">PROTOCOLO_FINALIZADO.EXE</div>
        <div class="final-highlight">IDENTIFICADO: VOCÊ ESTÁ LINDA.</div>
        <div class="divider-line"></div>
        <div class="final-main">PRÓXIMA ETAPA: CASA.</div>
        <div class="final-main" style="font-size:1.85rem;">ESTOU TE ESPERANDO.</div>
        <div class="final-footer">SISTEMA_ENCERRADO_21.03.2026</div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("REINICIAR PROTOCOLO"):
        st.session_state.etapa = 1
        st.session_state.autorizado = False
        st.rerun()
