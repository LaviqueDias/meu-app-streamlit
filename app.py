import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import defs

st.set_page_config(page_title="Financiamentos Imobiliários", layout="centered")
st.title("📊 Financiamentos Imobiliários")

arquivo = st.file_uploader("Selecione o arquivo CSV com os dados de financiamento", type=["csv"])

if arquivo is not None:
    try:
        df = defs.read_csv(arquivo)
        
        defs.grafico1(df)

        defs.grafico2(df)

        defs.grafico3(df)
        
        defs.grafico4(df)

        defs.grafico5(df)

        defs.grafico6(df)

    except Exception as e:
        st.error(f"Ocorreu um erro ao processar o arquivo: {e}")
else:
    st.warning("Por favor, carregue um arquivo CSV para continuar.")
