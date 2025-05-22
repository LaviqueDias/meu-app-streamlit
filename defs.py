import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def read_csv(arquivo):
    df = pd.read_csv(arquivo, encoding='latin-1', decimal=',', thousands='.')

    st.subheader("Prévia dos dados:")
    st.dataframe(df.head())

    df = df[df['qtd_uh_financiadas'] > 0]
    df['media_financiamento'] = df['vlr_financiamento'] / df['qtd_uh_financiadas']

    return df


def grafico1(df):
    st.subheader("📍 Comparativo da Média de Financiamentos: SP vs PB (2020-2024)")
    df_sp_pb = df[(df['txt_uf'].isin(['SP', 'PB'])) & (df['num_ano_financiamento'].between(2020, 2024))]
    df_sp_pb['media_financiamento'] = df_sp_pb['vlr_financiamento'] / df_sp_pb['qtd_uh_financiadas']
    media_sp_pb = df_sp_pb.groupby(['num_ano_financiamento', 'txt_uf'])['media_financiamento'].mean().unstack()
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    media_sp_pb.plot(ax=ax2, marker='o')
    ax2.set_title("Comparativo da Média de Financiamentos (SP vs PB) - 2020 a 2024")
    ax2.set_xlabel("Ano")
    ax2.set_ylabel("Média por Unidade (R$)")
    ax2.grid(True)
    ax2.legend(title='Estado')
    st.pyplot(fig2)


def grafico2(df):
    st.subheader("🇧🇷 Média Nacional de Financiamentos (2009-2024)")
    media_nacional = df.groupby('num_ano_financiamento')['media_financiamento'].mean()
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    
    ax2.plot(media_nacional.index, media_nacional.values, marker='o', color='blue')
    ax2.set_title("Média Nacional de Financiamento por Unidade (2009 a 2024)")
    ax2.set_xlabel("Ano")
    ax2.set_ylabel("Média por Unidade (R$)")
    ax2.set_xticks(range(2009, 2025))
    ax2.grid(True)
    st.pyplot(fig2)


def grafico3(df):
    st.subheader("🏙️ Top 10 Cidades com Menor Quantidade de Imóveis Financiados (2024)")
    df_2024 = df[df['num_ano_financiamento'] == 2024].copy()
    df_2024['cidade_estado'] = df_2024['txt_municipio'] + ' - ' + df_2024['txt_uf']
    cidades_financiamentos = df_2024.groupby('cidade_estado')['qtd_uh_financiadas'].sum()
    top_10_cidades = cidades_financiamentos.sort_values().head(10)

    fig3, ax3 = plt.subplots(figsize=(12, 6))

    ax3.bar(top_10_cidades.index, top_10_cidades.values, color='orange')
    ax3.set_title('Top 10 Cidades com Menor Quantidade de Imóveis Financiados em 2024')
    ax3.set_xlabel('Cidade - Estado')
    ax3.set_ylabel('Quantidade de Imóveis Financiados')
    ax3.set_xticklabels(top_10_cidades.index, rotation=45, ha='right')

    st.pyplot(fig3)


def grafico4(df):
    st.subheader("💰 Valor Total de Financiamento por Estado (2024)")
    df_ano = df[df['num_ano_financiamento'] == 2024]

    if df_ano.empty:
        st.warning(f"Não há dados disponíveis para o ano {2024}.")
    else:
        financiamento_por_estado = df_ano.groupby('txt_uf')['vlr_financiamento'].sum().sort_values(ascending=False)
        fig4, ax4 = plt.subplots(figsize=(12, 6))
        financiamento_por_estado.plot(kind='bar', ax=ax4, color='skyblue', edgecolor='black')

        ax4.set_title(f'Valor Total de Financiamento por Estado em {2024}', fontsize=14)
        ax4.set_xlabel('Estado')
        ax4.set_ylabel('Valor Total de Financiamento (R$)')
        ax4.set_xticklabels(financiamento_por_estado.index, rotation=45, ha='right')
        ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'.replace(',', 'X').replace('.', ',').replace('X', '.')))

        plt.tight_layout()
        st.pyplot(fig4) 


def grafico5(df):
    st.subheader("📈 Quantidade Total de Unidades Habitacionais Financiadas por Ano")
    financiamento_uh_ano = df.groupby('num_ano_financiamento')['qtd_uh_financiadas'].sum()
    fig5, ax = plt.subplots(figsize=(10, 5))

    ax.plot(financiamento_uh_ano.index, financiamento_uh_ano.values, marker='o', color='purple')
    ax.set_title("Quantidade de Unidades Habitacionais Financiadas por Ano")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Quantidade de Unidades")
    ax.grid(True)

    st.pyplot(fig5)


def grafico6(df):
    st.subheader("🏠 Valor Médio de Subsídio Concedido por Unidade ao Longo dos Anos")
    df = df[df['qtd_uh_financiadas'] > 0].copy()
    df['subsidio_medio'] = df['vlr_subsidio'] / df['qtd_uh_financiadas']
    subsidio_por_ano = df.groupby('num_ano_financiamento')['subsidio_medio'].mean()
    
    fig6, ax = plt.subplots(figsize=(10, 5))
    ax.plot(subsidio_por_ano.index, subsidio_por_ano.values, marker='o', color='red')
    ax.set_title("Valor Médio de Subsídio por Unidade Habitacional por Ano")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Subsídio Médio (R$)")
    ax.grid(True)

    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'.replace(',', 'X').replace('.', ',').replace('X', '.')))

    st.pyplot(fig6)


if __name__ == "__main__":
    print("defs.py foi executado diretamente")