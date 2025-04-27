from utils.csvmanager import CSVManager
from api.controller import ApiController
from api.service import NewsApiService
from requests.exceptions import RequestException
import time

def main():
    max_retries = 5
    tentativa = 0
    sucesso = False

    while tentativa < max_retries and not sucesso:
        try:
            print(f"Tentativa {tentativa + 1} de {max_retries}...")

            service = NewsApiService()
            controller = ApiController(service=service)
            noticias = controller.coletar_noticias()

            if noticias:
                csv_manager = CSVManager()
                csv_manager.salvar(noticias, "noticias_api.csv")
                sucesso = True
                print("Notícias coletadas e salvas com sucesso!")
            else:
                print("Nenhuma notícia retornada, tentando novamente...")
                tentativa += 1
                time.sleep(2)  # Espera 2 segundos antes de tentar de novo

        except RequestException as e:
            print(f"Erro durante a tentativa {tentativa + 1}: {e}")
            tentativa += 1
            time.sleep(2)  # Espera 2 segundos antes de tentar de novo

    if not sucesso:
        print(f"Falha ao coletar notícias após {max_retries} tentativas.")

if __name__ == "__main__":
    main()