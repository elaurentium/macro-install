# Macro Install

## Descrição
O **Macro Install** é um projeto desenvolvido para automatizar a instalação e configuração de macros do script de comando Powershell e scripts de comando Windows. Este script foi projetado para simplificar a configuração de um novo ambiente de trabalho, automatizando a instalação de ferramentas essenciais para trabalhadores Katrium.

Com o **Macro Install**, você pode rapidamente configurar seu ambiente com um conjunto pré-definido de pacotes, otimizando o tempo e evitando erros manuais durante a instalação.

## Funcionalidades
- Instalação automática de pacotes e ferramentas de trabalhadores Katrium.
- Configuração de permissões e ambientes personalizados.

## Intalação das depedencias
1. Clone o repositório:
   ```bash
   git clone https://github.com/elaurentium/macro-install.git

2. Crie um ambiente virtual:
    ```bash
    python3 -m venv venv ##Linux

    source venv/bin/activate ##Linux

    python -m venv venv ##Windows

    venv\Scripts\activate ##Windows

3. Instale as bibliotecas:
    ```bash
    pip install pathlib

    pip install tk

    pip install subprocess

    pip install python-dotenv



 **Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para mais detalhes.**

