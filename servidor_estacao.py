# import json
# import os

# # Dados coletados pela estação meteorológica
# dados = {
#     "temperatura": 25,
#     "umidade": 70,
#     "pressao": 1013
# }

# # Chave secreta compartilhada entre estação e servidor
# chave = os.getenv('SECRET_KEY') #, 'key-not-found')
# print(f"chave: {chave}")

# # =================== TESTE DA PARTE DA ESTAÇÃO ===================
# mensagem = criar_mensagem_autenticada(dados, chave)

# print("=== MENSAGEM GERADA PELA ESTAÇÃO ===")
# print(json.dumps(mensagem, indent=4))

# print("\n=== HMAC GERADO ===")
# print(mensagem["hmac"])

# print("\n=== VALIDAR MENSAGEM ===")
# print(mensagem_eh_valida(mensagem, chave))

# print("\n=== FALSIFICAR E VALIDAR MENSAGEM ===")
# dados["temperatura"] = 20
# print(mensagem_eh_valida(mensagem, chave))


