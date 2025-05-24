import streamlit as st

st.set_page_config(page_title="Simulador de Empréstimo", page_icon="💰")

st.title("💰 Simulador de Empréstimo")

st.subheader("Preencha os dados abaixo:")

# 👉 Novo campo: Nome da linha de crédito
nome_linha = st.text_input("Nome da linha de crédito (ex.: Empréstimo Pessoal)")

valor_total = st.number_input("Valor total do crédito (R$)", min_value=0.0, format="%.2f")

st.markdown("### Proposta 1")
p1_prazo = st.number_input("Prazo (meses) - Proposta 1", min_value=1)
p1_parcela = st.number_input("Valor da parcela (R$) - Proposta 1", min_value=0.0, format="%.2f")

st.markdown("### Proposta 2")
p2_prazo = st.number_input("Prazo (meses) - Proposta 2", min_value=1)
p2_parcela = st.number_input("Valor da parcela (R$) - Proposta 2", min_value=0.0, format="%.2f")

st.markdown("### Data da Primeira Parcela")
data_primeira_parcela = st.date_input("Data da primeira parcela")

if st.button("Gerar Simulação"):
    texto = f"""
    ❇️ {nome_linha} ❇️

    💲 **Valor total:** R$ {valor_total:,.2f}

    📄 **Proposta 1:**
    - Prazo: {p1_prazo} meses
    - Valor da parcela: R$ {p1_parcela:,.2f}

    📄 **Proposta 2:**
    - Prazo: {p2_prazo} meses
    - Valor da parcela: R$ {p2_parcela:,.2f}

    📆 **Primeira parcela em:** {data_primeira_parcela.strftime('%d/%m/%Y')}

    ❇️❇️❇️❇️❇️❇️
    """

    st.success("✅ Simulação Gerada!")
    st.markdown(texto)
    st.download_button("📥 Baixar Simulação como TXT", texto, file_name="simulacao.txt")