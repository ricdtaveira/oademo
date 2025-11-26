## Para executar
## $ streamlit run app.py

import streamlit as st
import math
import time


# Funções de animação suave (simulação por atualização de tamanho)
def animate_size(start, end, steps=10, sleep_time=0.06):
    sizes = [start + (end - start) * i / steps for i in range(steps + 1)]
    for s in sizes:
        yield s
        time.sleep(sleep_time)


st.set_page_config(page_title="Geometria EF08MA19", page_icon="🔷", layout="centered")

# Inicialização de sessão
if "nivel" not in st.session_state:
    st.session_state.nivel = 1
if "concluido" not in st.session_state:
    st.session_state.concluido = False

st.title("🧮 Objeto de Aprendizagem: Medidas de Área e Volume")
st.caption("Habilidade BNCC EF08MA19 — 8º ano | Geometria para Estatística")


def mensagem_sucesso():
    st.success("Boa! Você acertou. Observe como ficou a figura e leia sua conclusão ao final.")


def mensagem_erro(explicacao):
    st.warning(f"Resposta incorreta, tente novamente! {explicacao}")


# -- Nível 1: Análise de Um Quadrado --
def nivel1():
    st.subheader("Nível 1: Área de um Quadrado ⬛")
    lado = 5  # metros
    area = lado ** 2
    st.markdown(f"**Observe:** O quadrado abaixo tem lados de **{lado} metros**.")

    # Simulação de animação de crescimento do quadrado
    area_html = ""
    for tam in animate_size(80, 160):
        area_html = f"""
        <div style='width:{tam}px;height:{tam}px;background:#0078C2;border-radius:10px;display:inline-block;transition:all 0.2s;'></div>
        """
        st.markdown(area_html, unsafe_allow_html=True)

    st.write("Qual é a área do quadrado? (em metros quadrados)")
    opcoes = {
        "A": 10,
        "B": 20,
        "C": 25,
        "D": 30
    }
    resposta = st.radio("Escolha a alternativa:", list(opcoes.keys()), key="nivel1_radio")

    if st.button("Responder", key="resp_nivel1"):
        if opcoes[resposta] == area:
            mensagem_sucesso()
            st.session_state.nivel = 2
            # Síntese automática
            st.info(
                f'Síntese: “Observa-se que um quadrado com lados de {lado} metros possui área de {area} m². O cálculo foi possível multiplicando o lado por ele mesmo.”')
        else:
            mensagem_erro("O cálculo correto é lado × lado = área.")


# -- Nível 2: Comparação Quadrado x Círculo --
def nivel2():
    st.subheader("Nível 2: Comparando Quadrado ⬛ e Círculo ⚪")
    lado_q = 6  # metros (quadrado)
    raio_c = 3  # metros (círculo)
    area_q = lado_q ** 2
    area_c = round(math.pi * raio_c ** 2, 2)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"⬛ Quadrado: lado = {lado_q} m")
        # Quadrado animado
        for tam in animate_size(90, 130):
            fig = f"<div style='width:{tam}px;height:{tam}px;background:#2596be;border-radius:10px;'></div>"
            st.markdown(fig, unsafe_allow_html=True)
        st.write(f"Área = {area_q} m²")
    with col2:
        st.markdown(f"⚪ Círculo: raio = {raio_c} m")
        # Círculo animado
        for tam in animate_size(80, 120):
            fig = f"<div style='width:{tam}px;height:{tam}px;background:#ffde59;border-radius:60px;'></div>"
            st.markdown(fig, unsafe_allow_html=True)
        st.write(f"Área ≈ {area_c} m²")

    st.write("Qual das duas figuras tem a **maior área**?")
    opcoes = {
        "A": "Quadrado",
        "B": "Círculo",
        "C": "Ambas têm a mesma área",
        "D": "Não é possível saber"
    }
    resposta = st.radio("Escolha a alternativa:", list(opcoes.keys()), key="nivel2_radio")

    if st.button("Responder", key="resp_nivel2"):
        if resposta == "A":
            mensagem_sucesso()
            st.session_state.nivel = 3
            st.info(
                f'Síntese: “Comparando as figuras, o quadrado possui área de {area_q} m² e o círculo cerca de {area_c} m². Observa-se que, neste caso, o quadrado tem maior área.”')
        else:
            mensagem_erro("Veja que o quadrado tem área maior que o círculo nesta situação.")


# -- Nível 3: Volume Cubo x Cilindro --
def nivel3():
    st.subheader("Nível 3: Comparando Volumes — Cubo 🧊 e Cilindro 🥤")
    # Dimensões
    lado_cubo = 4
    raio_cil = 2
    alt_cil = 6
    vol_cubo = lado_cubo ** 3
    vol_cil = round(math.pi * raio_cil ** 2 * alt_cil, 2)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"🧊 Cubo: lado = {lado_cubo} m")
        for tam in animate_size(60, 105):
            fig = f"<div style='width:{tam}px;height:{tam}px;background:#70db93;border-radius:14px;box-shadow:2px 2px 6px #cce7e7;'></div>"
            st.markdown(fig, unsafe_allow_html=True)
        st.write(f"Volume = {vol_cubo} m³")
    with col2:
        st.markdown(f"🥤 Cilindro: raio = {raio_cil} m, altura = {alt_cil} m")
        for tam in animate_size(65, 110):
            fig = f"<div style='width:{tam}px;height:{tam * 1.8}px;background:#F28679;border-radius:50px;box-shadow:2px 2px 8px #8e5656;'></div>"
            st.markdown(fig, unsafe_allow_html=True)
        st.write(f"Volume ≈ {vol_cil} m³")

    st.write("Qual dos sólidos tem **maior volume**?")
    opcoes = {
        "A": "Cubo",
        "B": "Cilindro",
        "C": "Ambos têm o mesmo volume",
        "D": "Não é possível saber"
    }
    resposta = st.radio("Escolha a alternativa:", list(opcoes.keys()), key="nivel3_radio")

    if st.button("Responder", key="resp_nivel3"):
        if resposta == "B":
            mensagem_sucesso()
            st.session_state.concluido = True
            st.info(
                f'Síntese: “Ao comparar os volumes, percebe-se que o cilindro ({vol_cil} m³) tem volume maior que o cubo ({vol_cubo} m³), pois o cálculo do volume dos sólidos depende de suas fórmulas específicas.”')
        else:
            mensagem_erro("Veja o cálculo: volume do cubo é menor que o do cilindro neste exemplo.")


# -- Apresentação por Nível --
if not st.session_state.concluido:
    if st.session_state.nivel == 1:
        nivel1()
    elif st.session_state.nivel == 2:
        nivel2()
    elif st.session_state.nivel == 3:
        nivel3()
else:
    st.header("Parabéns! 🌟 Você concluiu todos os níveis.")
    st.markdown("Se desejar, clique abaixo para reiniciar e praticar novamente.")
    if st.button("Reiniciar"):
        st.session_state.nivel = 1
        st.session_state.concluido = False
        st.experimental_rerun()

st.markdown("---")
st.markdown('<small>Desenvolvido para BNCC EF08MA19 | Geometria do 8º ano do Ensino Fundamental.</small>',
            unsafe_allow_html=True)
