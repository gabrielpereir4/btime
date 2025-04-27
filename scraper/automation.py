from scraper.tasks import Tasks

class Automation():
    """
    Classe que define o fluxo de execução da automação e fornece configurações conforme necessário.
    """
    def __init__(self):
        self.tasks = Tasks()

    def run(self):
        """
        Executa a automação
        """
        self.tasks.open_browser()
        self.tasks.iterar_noticias()
        self.tasks.close_browser()
        return self.tasks.get_noticias()