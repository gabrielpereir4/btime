# API

Automação de chamada de API, especificamente do NewsAPI.

Arquiteturalmente a automação é dividida em 3 classes com diferentes responsabilidades:
- Service
    - Classe de serviço responsável exclusivamente pela lógica direta de chamada da API.
- Article
    - Classe de modelo para os artigos
- Controller
    - Classe intermediária entre o Service, o Article e o método Main. Engloba a lógica de chamar a classe Service quando solicitado, e de tratar sua saída para o método Main utilizando a classe Article.
- Método Main
    - Método responsável por executar o fluxo completo da automação.

OBS: Essa automação utiliza uma chave API_KEY para a NewsAPI armazenada num arquivo do tipo ```.env```. 
    Dessa forma, para utilizar a automação API, crie um arquivo ```.env``` dentro da pasta ```/api``` e crie o seguinte campo:
    ```
    API_KEY=SUA_CHAVE_AQUI
    ```
    E substitua ```SUA_CHAVE_AQUI``` pelo valor real da chave.
    Para obter uma chave, basta criar uma conta gratuita no site da NewsAPI.