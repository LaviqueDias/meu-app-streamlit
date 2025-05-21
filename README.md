
# 🏡 Dashboard de Financiamentos Habitacionais - Streamlit

Este projeto é uma aplicação interativa desenvolvida com [Streamlit](https://streamlit.io/) para visualização de dados de financiamentos habitacionais no Brasil. A aplicação permite explorar diversas análises gráficas a partir de um arquivo CSV com dados financeiros e habitacionais.

## 📁 Estrutura do Projeto

```
MEU_APP_STREAMLIT/
├── .venv/                  # Ambiente virtual (opcional)
├── defs/
│   └── read_csv.py         # Função de leitura e pré-processamento do CSV
├── app.py                  # Arquivo principal da aplicação Streamlit
├── dados.csv               # Arquivo CSV de exemplo com os dados
└── README.md               # Documentação do projeto
```

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd MEU_APP_STREAMLIT
   ```

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install streamlit pandas matplotlib
   ```

4. **Execute o aplicativo:**
   ```bash
   python -m streamlit run app.py
   ```

## 🧠 Funcionalidades

O app permite:

- Upload de um arquivo CSV com os dados de financiamento.
- Visualização inicial dos dados carregados.
- Cálculo da média de financiamento por unidade habitacional.
- Geração de diversos gráficos interativos:

### 📊 Gráficos Disponíveis

| Função     | Descrição |
|------------|-----------|
| `grafico1` | Comparativo da média de financiamentos entre SP e PB (2020-2024). |
| `grafico2` | Evolução da média nacional de financiamento por unidade (2009-2024). |
| `grafico3` | Top 10 cidades com menor quantidade de imóveis financiados em 2024. |
| `grafico4` | Valor total de financiamento por estado em 2024. |
| `grafico5` | Quantidade total de unidades habitacionais financiadas por ano. |
| `grafico6` | Valor médio de subsídio concedido por unidade habitacional ao longo dos anos. |

## 🧾 Requisitos do Arquivo CSV

O arquivo de entrada deve conter, no mínimo, as seguintes colunas:

- `txt_uf`: Sigla do estado.
- `txt_municipio`: Nome do município.
- `num_ano_financiamento`: Ano do financiamento.
- `vlr_financiamento`: Valor do financiamento.
- `qtd_uh_financiadas`: Quantidade de unidades habitacionais financiadas.
- `vlr_subsidio`: Valor do subsídio concedido.

> 💡 O CSV deve estar formatado com codificação **latin-1**, separador padrão e valores numéricos com **vírgula como separador decimal**.

## 📌 Observações

- O código está modularizado: as funções de carregamento de dados ficam no arquivo `defs/read_csv.py`.
- Os gráficos são gerados com `matplotlib` e exibidos via `Streamlit`.
- O app lida com possíveis divisões por zero e valores inconsistentes.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Desenvolvido com 💻 por Lavique Dias.
