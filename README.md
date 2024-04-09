# Projeto de Login Flask

Este é um projeto de exemplo que demonstra a implementação de um sistema de login usando Flask.

## Funcionalidades
- Registro de novos usuários
- Autenticação de usuários existentes
- Proteção de rotas autenticadas
- Página de perfil do usuário

## Pré-requisitos
Certifique-se de ter Python instalado em seu sistema. Além disso, é recomendável o uso de um ambiente virtual para isolar as dependências do projeto.

## Instalação
1. Clone este repositório em seu ambiente de desenvolvimento:
    ```
    git clone https://github.com/nelson-s-jr/projeto_login_flask.git
    ```
2. Navegue até o diretório do projeto:
    ```
    cd nome-do-repositorio
    ```
3. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\activate   # Windows
    ```
4. Instale as dependências do projeto:
    ```
    pip install -r requirements.txt
    ```
5. Defina as variáveis de ambiente:
    ```
    $env:FLASK_APP='project'
    $env:FLASK_DEBUG=1 


## Uso
Para executar o aplicativo, use o seguinte comando:
```
flask run
