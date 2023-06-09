# Programa de Verificação de Integridade e Segurança

import hashlib


# Função para geração de Hash
def generate_hash(file):
    hash_gen = hashlib.sha256()

    with open(file, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_gen.update(byte_block)

    return hash_gen.hexdigest()


# Menu para escolha do usuário
print(" \n Programe uma verificação de segurança ")
print(" [1] Verificar arquivo existente")
print(" [2] Verificar hash gerado")
print(" [0] Para sair\n ")

opcao = int(input("Selecione a opção: \n"))

# Verificação de arquivo existente
if opcao == 1:
    arquivo = input("Entre com o nome do arquivo para verificação: \n")
    gerado_hash = generate_hash(arquivo)
    print(f"Hash gerado para o arquivo '{arquivo}': \n {gerado_hash}")

# Verificação de hash específica
elif opcao == 2:
    hash_anterior = input("Digite o Hash: \n")
    arquivo = input("Digite o nome do arquivo para verificação: \n")
    gerado_hash = generate_hash(arquivo)
    print(f"Hash gerado para o arquivo '{arquivo}': \n {gerado_hash}")

    if gerado_hash == hash_anterior:
        print(f"Hash corresponde ao do arquivo {arquivo}. \n")
    else:
        print("Hash não correspondente. \n")

# Finalizando o programa
else:
    print("Programa finalizado")
