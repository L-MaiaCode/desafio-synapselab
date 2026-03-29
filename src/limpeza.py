import pandas as pd
from pathlib import Path

def limpar_dataframe():
    """
    Realiza a importação e limpeza inicial do conjunto de dados
    """

    # Carrega o arquivo csv

    # resolve() garante o caminho absoluto livre de erros
    # parent.parent sobe da pasta 'src' para a raiz do projeto
    diretorio_atual = Path(__file__).resolve().parent.parent

    # Junta o diretório atual com a pasta 'data' e o nome do arquivo
    caminho_arquivo = diretorio_atual / "data" / "Video_Games_Sales_Cleaned.csv"

    # Carregamento seguro dos dados
    try:
        df = pd.read_csv(caminho_arquivo)
        print('\033[92mArquivo CSV encontrado com sucesso!\033[00m')
    except FileNotFoundError:
        print(f'Arquivo não encontrado no caminho: {caminho_arquivo}')
        return None

    # Verificar se existem valores nulos e relatá-los
    nulos = df.isnull().sum()
    if nulos.any():
        print(f'Valores nulos encontrados: {nulos}')
    else:
        print('O conjunto de dados não possui valores nulos')

    # Verificar se existem linhas duplicadas e removê-las
    linhas_duplicadas = df.duplicated().sum()
    if linhas_duplicadas > 0:
        df.drop_duplicates(inplace=True)
        print(f'Foram removidas {linhas_duplicadas} linhas duplicadas.')
    else:
        print('Nenhuma linha duplicada encontrada.')

    # Retorna o dataframe limpo
    return df
