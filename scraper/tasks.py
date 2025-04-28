from RPA.Browser.Selenium import Selenium

class Tasks():
    """
    Classe para encapsulamento da lógica da automação
    """
    def __init__(self):
        self.browser = None
        self.noticias = []

    def get_noticias(self):
        """
        Método para retornar a lista de notícias coletadas
        """
        return self.noticias

    def open_browser(self):
        """ 
        Método para abrir o navegador Chrome, maximizando a janela e repassar a instância
        do navegador para a variável de instância self.browser
        """
        browser = Selenium()
        # A definção do user_agent é opcional, mas pode ajudar a evitar bloqueios de acesso
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        browser.open_chrome_browser(url="https://g1.globo.com/", user_agent=user_agent, headless=True)
        # browser.maximize_browser_window() # Não necessário em modo headless
        self.browser = browser

    def close_browser(self):
        """
        Método para fechar o navegador
        """
        if self.browser:
            self.browser.close_browser()
            self.browser = None

    def iterar_noticias(self):
        """
        Método para iterar as notícias da página inicial do G1, retornando o título e o link
        de cada uma delas.
        """
        j = 1
        while True:
            i = 1
            # O site do G1 contém vários contêineres de notícias, representados na variável master_xpath_root
            master_xpath_root = 'xpath://html/body/div[2]/main/div[4]/div[2]/div/div/div/div/div/div/div/div[2]/div[' + str(j) + ']'
            try:
                self.browser.wait_until_element_is_enabled(master_xpath_root, timeout=5)
            except AssertionError:
                # Se não encontrar o elemento, significa que não há mais notícias para iterar
                break
            
            xpath_root = master_xpath_root + '/div/div/div['

            while True:
                # Aqui as notícias são iteradas de acordo com o contêiner pai e numeração conforme
                # variável auxiliar i.
                xpath_atual = xpath_root + str(i) + "]"
                try:
                    self.browser.wait_until_element_is_enabled(xpath_atual, timeout=5)
                except AssertionError:
                    # Se não encontrar o elemento, significa que não há mais notícias para iterar
                    break

                noticia = {
                "titulo": self.procurar_item(xpath_atual, '/div/div/div/div[2]'),
                "hora": self.procurar_item(xpath_atual, '/div/div/div/div[4]'),
                "subtitulo": self.procurar_item(xpath_atual, '/div/div/div/div[5]'),
                "tema": self.procurar_item(xpath_atual, '/div/div/div/div[1]/span'),
                }

                self.noticias.append(noticia)

                i = i + 1

            j = j + 1

       #print("Total de notícias: ", len(self.noticias))
        #print("Notícias: ", self.noticias)


    def procurar_item(self, xpath_atual, xpath_alvo):
        """
        Método para procurar um item específico dentro de um elemento, retornando o texto
        encontrado ou None caso não encontre o elemento.
        """
        xpath_completo = xpath_atual + xpath_alvo
        try:
            self.browser.wait_until_element_is_visible(xpath_completo, timeout=1)
            retorno = self.browser.get_text(xpath_completo)
            #print("Texto encontrado: ", retorno)
            return retorno
        except AssertionError:
            #print(f"Elemento {xpath_alvo} não encontrado: ", e)
            return None