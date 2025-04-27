class Article:
    """
    Modelo de dados para uma notícia/artigo.
    """
    def __init__(self, titulo, hora, subtitulo, tema):
        self.titulo = titulo
        self.hora = hora
        self.subtitulo = subtitulo
        self.tema = tema

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "hora": self.hora,
            "subtitulo": self.subtitulo,
            "tema": self.tema
        }