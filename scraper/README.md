# Web Scraper

Essa automação é desenvolvida para coleta automatizada de dados sobre notícias do site do G1.

Arquiteturalmente, a automação é monolítica, porém dividida em 2 classes, partindo do princípio de separação de responsabilidades:

- Tasks:
    - Agrupa e encapsula toda a lógica de automação, separando as tarefas em métodos distintos.
- Automation
    - Encapsula uma instância do Tasks e chama seus métodos na ordem de execução da automação, forencendo qualquer configuração conforme necessário
- Método Main
    - Método principal que instancia a classe Automation e chama ela para execução do fluxo da automação.

A biblioteca usada é o RPA Framework, framework em que conheci há não muito tempo, e que costumo usar bastante em minhas automações principalmente pelos seus métodos com esperas ímplicitas/dinâmicas. O RPA Framework implementa o Selenium para automações web.

OBS: Devido à variação na estrutura dos cards do portal G1, alguns campos podem estar ausentes ou inconsistentes (ex: subtítulo no lugar da hora). A automação, por agora, trata apenas cards sem dados, para evitar perda de informações.