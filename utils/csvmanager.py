import pandas as pd

class CSVManager():
    """
    Classe genérica para gerenciar a criação e manipulação de arquivos CSV com os dados coletados
    Usada tanto pelo Scraper quanto pela API.
    """
    def __init__(self):
        pass

    def salvar(self, noticias, caminho_csv="noticias.csv"):
        """
        Salva a lista de notícias no caminho especificado.
        Aceita lista de objetos com método to_dict() ou dicionários.
        """
        dados = []

        for noticia in noticias:
            if hasattr(noticia, "to_dict"):
                dados.append(noticia.to_dict())
            else:
                dados.append(noticia)

        df = pd.DataFrame(dados)

        # Garante a ordem das colunas
        df = df.reindex()

        # Substitui None por string vazia para deixar o CSV limpo
        df.fillna("", inplace=True)

        df.to_csv(caminho_csv, index=False, encoding='utf-8-sig')
        print(f"Arquivo salvo com sucesso em: {caminho_csv}")