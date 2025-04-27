# API KEY 2a5882af254f4787bc1ae0903b412f00
from dotenv import load_dotenv
import os
import requests

class NewsApiService:
    """
    Serviço responsável por fazer chamadas à NewsAPI.
    """
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.base_url = "https://newsapi.org/v2"
        if not self.api_key:
            raise ValueError("API_KEY não encontrada. Verifique se o arquivo .env está configurado corretamente.")


    def fetch_top_headlines(self, country='us', category='general', page_size=30):
        """
        Método para buscar notícias na NewsAPI, do tipo "top-headlines".
        :param country: Código do país (ex: 'us' para Estados Unidos).
        :param category: Categoria da notícia (ex: 'business', 'entertainment', etc.).
        :param page_size: Número de notícias a serem retornadas (padrão é 30).
        :return: Lista de artigos (notícias) retornados pela API, em JSON.
        """

        url = f"{self.base_url}/top-headlines"
        params = {
            'country': country,
            'category': category,
            'pageSize': page_size,
            'apiKey': self.api_key
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            #print('200 po')
            #print(response.json())
            return response.json().get('articles', [])
        else:
            #print("Erro:", response.status_code, response.text)
            return []