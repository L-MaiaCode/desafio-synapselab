import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from limpeza import limpar_dataframe

# 1. Importação da base de dados

df = limpar_dataframe()

# Informações da base de dados
print(df.shape)

print(df.info())

print(df.head())

print(df.describe())  # resumo estatístico

# --- Aqui começa a análise de dados e criação dos gráficos ---

sns.set_theme(style="darkgrid")


def generos_mais_vendidos():
    vendas_por_genero = (
        df.groupby("genre")["total_sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.barplot(
        data=vendas_por_genero, x="genre", y="total_sales", palette="viridis", ax=ax
    )

    ax.set_title("Gêneros mais vendidos")
    ax.set_xlabel("Gênero")
    ax.set_ylabel("Total de vendas (milhões de cópias)")
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    return fig


def generos_mais_produzidos():
    producao_por_genero = (df["genre"].value_counts()).reset_index().head(12)

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.barplot(
        data=producao_por_genero, x="count", y="genre", palette="viridis", ax=ax
    )

    ax.set_title("Gêneros mais produzidos")
    ax.set_xlabel("Contagem de lançamentos")
    ax.set_ylabel("Gênero")

    plt.tight_layout()

    return fig


def anos_com_mais_vendas():
    vendas_por_ano = (
        df.groupby("release_year")["total_sales"].sum().reset_index()
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.lineplot(
        data=vendas_por_ano,
        x='release_year',
        y='total_sales',
        marker='o',
        color='purple'
    )

    ax.set_title('Evolução da venda de vídeo games (1980 - 2024)')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Total de vendas (milhões de cópias)')

    plt.tight_layout()

    return fig


def editoras_com_mais_vendas():
    vendas_por_editora = (
        df.groupby('publisher')['total_sales']
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    ).head(10)

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.barplot(
        data=vendas_por_editora,
        x='total_sales',
        y='publisher',
        palette='viridis',
        ax=ax
    )

    ax.set_title('Top 10 editoras com mais vendas')
    ax.set_xlabel('Total de vendas (milhões de cópias)')
    ax.set_ylabel('Editora')

    plt.tight_layout()

    return fig


def jogos_mais_vendidos():
    vendas_por_jogos = (
        df.groupby('title')['total_sales']
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    ).head(15)

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.barplot(
        data=vendas_por_jogos,
        x='total_sales',
        y='title',
        palette='viridis',
        ax=ax
    )

    ax.set_title('Top 15 jogos mais vendidos')
    ax.set_xlabel('Total de vendas (milhões de cópias)')
    ax.set_ylabel('Jogo')

    plt.tight_layout()

    return fig


def obter_lista_consoles():
    '''
    Retorna uma lista com os nomes de todos os consoles únicos (em ordem alfabética)
    '''

    consoles = df['console'].dropna().unique().tolist()
    consoles.sort()
    return consoles


def jogos_mais_vendidos_por_console(console_escolhido):
    '''
    Filtra o DF pelo console e retorna a fig com o top 10 jogos
    '''

    df_filtrado = df[df['console'] == console_escolhido]

    top_10 = (
        df_filtrado.sort_values(by='total_sales', ascending=False).head(10)
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.barplot(
        data=top_10,
        x='total_sales',
        y='title',
        palette='viridis',
        ax=ax
    )

    ax.set_title(f'Top 10 jogos mais vendidos - {console_escolhido}')
    ax.set_xlabel('Total de vendas (milhões de cópias)')
    ax.set_ylabel('Título')

    plt.tight_layout()

    return fig


def timeline_vendas_por_console(consoles_escolhidos):
    '''
    Filtra o DF pelo console e retorna a linha do tempo de vendas
    '''

    if not consoles_escolhidos:
        return None

    df_filtrado = df[df['console'].isin(consoles_escolhidos)]

    timeline = (
        df_filtrado.groupby(['release_year', 'console'])['total_sales']
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.lineplot(
        data=timeline,
        x='release_year',
        y='total_sales',
        hue='console',
        marker='o',
        ax=ax
    )

    ax.set_title('Comparação de vendas por console ao londo do tempo')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Total de vendas (milhões de cópias)')

    plt.tight_layout()

    return fig

# --------------------------- TESTES -----------------------------------

# # 3. Top 10 títulos mais vendidos

# titulos_mais_vendidos = (
#     df.groupby("title")["total_sales"].sum().sort_values(ascending=False).reset_index()
# ).head(10)

# # Plotando o gráfico
# plt.figure(figsize=(12, 6))

# sns.barplot(x="total_sales", y="title", data=titulos_mais_vendidos, palette='viridis')

# plt.title('Top 10 Títulos Mais Vendidos (mídia física)')
# plt.xlabel('Total de Vendas (milhões de cópias)')
# plt.ylabel('Título')

# plt.tight_layout()

# # 4. Top 10 plataformas com mais vendas

# vendas_por_plataforma = df.groupby('console')['total_sales'].sum().sort_values(ascending=False).reset_index().head(10)

# plt.figure(figsize=(12, 6))

# sns.barplot(
#     data=vendas_por_plataforma,
#     x='console',
#     y='total_sales',
#     palette='viridis'
# )

# plt.title('Top 10 Consoles com mais vendas')
# plt.xlabel('Console')
# plt.ylabel('Total de Vendas (milhões de cópias)')

# plt.tight_layout

# # Outras análises gráficas

# plt.show()
