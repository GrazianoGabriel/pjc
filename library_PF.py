import os

def ler_file(caminho):
    meu_arquivo = open(caminho)
    conteudo = meu_arquivo.read()
    meu_arquivo.close()
    return conteudo

def ler_linhas(caminho):
    arquivo = open(caminho)
    linhas = arquivo.readlines()
    arquivo.close
    return linhas

def escreve_file(caminho, texto):
    arquivo = open(caminho, 'w')
    arquivo.write(texto)
    arquivo.close

def cadastro_eleitor(caminho):
      
    """
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exist
    """

    #colunas = ["nome", "id", "data_nasc", "mae", "pai", "votou"]  
    
    nome = input("Digite o seu nome: ")
    id = input("Número do título ou CPF: ")
    data_nasc = (input("Data de nascimento: "))
    mae = input("Nome da mae: ")
    pai =  input("Nome do pai: ")
    votou = "0"

    c = input("Votou na ultima eleicao? s/n: ")
    if c == "s" or c == "S":
        votou = "1"

    meu_csv = open(caminho, 'a')
    meu_csv.write(";".join([nome,id,data_nasc,mae,pai,votou]) + "\n")
    meu_csv.close()
