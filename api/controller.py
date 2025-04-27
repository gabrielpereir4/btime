from api.article import Article

class ApiController:
    """
    Controlador que orquestra a coleta e formatação dos dados da NewsAPI.
    """
    def __init__(self, service):
        self.service = service

    def coletar_noticias(self):
        artigos = self.service.fetch_top_headlines()
        noticias = []

        for artigo in artigos:
            titulo = artigo.get("title")
            hora = artigo.get("publishedAt")
            subtitulo = artigo.get("description")
            tema = artigo.get("source", {}).get("name")

            noticia = Article(
                titulo=titulo,
                hora=hora,
                subtitulo=subtitulo,
                tema=tema
            )
            noticias.append(noticia)

        return noticias