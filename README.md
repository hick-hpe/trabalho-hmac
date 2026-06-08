# Trabalho – Autenticação de Mensagens com HMAC

## Descrição
Desenvolviemnto de uma estação meteorológica que coleta dados climáticos
(temperatura, umidade, pressão, entre outros) e os envia para um servidor central.
Para garantir a autenticidade e a integridade dos dados, a estação meteorológica usa
um HMAC (Hash-based Message Authentication Code) para assinar as mensagens
antes de enviá-las. O servidor, ao receber essas mensagens, deve validar a assinatura
para confirmar que os dados são legítimos e não foram alterados.

## Instalação

1. Clone o repositório
    ```bash
    git clone https://github.com/hick-hpe/trabalho-hmac.git
    cd trabalho-hmac
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Linux / Mac
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```
        # Windows
    pip install -r requirements.txt

    # Linux / Mac
    pip3 install -r requirements.txt
    ```

4. Rode o servidor:
    ```
    uvicorn main:app --reload
    ```


Abra o navegador em [http://localhost:8000/](http://localhost:8000/) para testar.

