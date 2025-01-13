import pandas as pd
import plotly.express as px

# Passo 1: Leitura dos dados
tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")

# Passo 2: Limpeza dos dados
# Deletar a coluna 'Unnamed: 8' que é inútil
tabela = tabela.drop("Unnamed: 8", axis=1)

# Passo 3: Tratamento de Dados
# Acertar informações que estão sendo reconhecidas de forma errada, como 'Salário Anual (R$)'
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")

# Corrigir os dados ausentes (deletando as linhas com NaN)
tabela = tabela.dropna()

# Passo 4: Análise inicial - Verificando o tipo dos dados
print(tabela.info())  # Para verificar os tipos de dados e valores ausentes
print(tabela.describe())  # Estatísticas descritivas para uma análise inicial

# Passo 5: Análise completa - Como cada característica do cliente impacta na nota

# Para uma melhor visualização, vamos configurar um título, eixos e outras melhorias de estilo no gráfico.
for coluna in tabela.columns:
    if coluna != "Nota (1-100)":  # Evitar que a própria nota seja plotada como coluna
        print(f"Gerando gráfico para {coluna}...")  # Feedback sobre o progresso
        grafico = px.histogram(
            tabela,
            x=coluna,
            y="Nota (1-100)",
            histfunc="avg",  # Mostrar a média das notas
            text_auto=True,  # Exibir valores no gráfico
            title=f"Impacto de {coluna} na Nota dos Clientes",
            labels={coluna: coluna, "Nota (1-100)": "Nota Média (1-100)"},  # Customizando rótulos
            color=coluna,  # Colorir os gráficos de acordo com a variável
            template="plotly_dark"  # Estilo do gráfico (você pode mudar para 'plotly', 'ggplot2', etc.)
        )

        # Melhorar a configuração de layout do gráfico
        grafico.update_layout(
            xaxis_title=coluna,
            yaxis_title="Nota Média (1-100)",
            bargap=0.2,  # Espaçamento entre as barras
            font=dict(size=12)  # Tamanho da fonte
        )

        # Exibir o gráfico
        grafico.show()

# Passo 6: Salvar gráficos (opcional)
# grafico.write_html("grafico_notas_interativo.html")  # Para salvar o gráfico como HTML interativo
