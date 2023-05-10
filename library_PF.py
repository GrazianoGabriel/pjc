import os

import datetime

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
    #nome;mae;pai;data_nasc;titulo;zona;secao;municipio;uf;data_insc;votou 
    
    votou = "0"

    nome = input("Nome completo: ")
    mae = input("Nome da mae: ")
    pai =  input("Nome do pai: ")
    data_nasc = input("Data de nascimento: ")
    id = input("Número do título: ")
    zona = input('Zona: ')
    secao = input('Secao: ')
    municipio = input('Municipio de nascimento: ')
    uf = input('Estado: ')
    data_insc = input('Data de inscricao: ')

    c = input("Votou na ultima eleicao? s/n: ")
    if c == "s" or c == "S":
        votou = "1"

    meu_csv = open(caminho, 'a')
    meu_csv.write(";".join([nome,mae, pai, data_nasc, id, zona, secao, municipio, uf, data_insc, votou]) + "\n")
    meu_csv.close()

def calcula_idade(data_nasc):
    #data_nasc = "23/04/1993"
    day, month, year = map(int, data_nasc.split('/'))

    birth_date = datetime.date(year, month, day)

    current_date = datetime.datetime.now()

    if current_date.month - birth_date.month < 0:
        return current_date.year - birth_date.year -1
    elif current_date.month - birth_date.month > 0:
        return current_date.year - birth_date.year
    else:
        if current_date.day >= birth_date.day:
            return current_date.year - birth_date.year
        else:
            return current_date.year - birth_date.year -1
    
def verifica_voto(idade, votou):
    if idade >= 18 and idade <= 70 and votou == 1:
        return True
    elif idade >= 16 and idade < 18:
        return True
    elif idade > 70:
        return True
    else:
        return False

def valida_eleitor(caminho, nome, id, nome_mae):

    myFile = open(caminho, 'r', encoding='UTF-8')
    linhas = myFile.readlines()

    for i in linhas:
        line = i.split(';')

        if line[0] == nome and line[4]== id and line[1] == nome_mae:

            idade = calcula_idade(line[3])

            if verifica_voto(idade, int(line[10])):
                print('\nSituacao regular. Certidao emitida com sucesso.')
                myFile.close()
                return True
            else: 
                print('\nSituacao irregular. Regularize sua situacao antes de emitir a certidao.')
                myFile.close()
                return False
     
    print("\nEleitor nao cadastrado(a)")
    myFile.close()
    return False

def emite_certidao(caminho, nome, nome_mae, id):

    meu_csv = open(caminho, 'r', encoding='UTF-8')
    linhas = meu_csv.readlines()
    for i in linhas:
        line = i.split(';')

        if line[0] == nome and line[1]== nome_mae and line[4] == id:
            eleitor = line
    meu_csv.close()

    pagina = open('certidao.html')
    #nome;mae;pai;data_nasc;titulo;zona;secao;municipio;uf;data_insc;votou
    conteudo = pagina.read()
    atualizada = conteudo.replace('$NOME$', eleitor[0])
    atualizada = atualizada.replace('$TITULO$', eleitor[4])
    atualizada = atualizada.replace('$CIDADE$', eleitor[7])
    atualizada = atualizada.replace('$NASC$', eleitor[3])
    atualizada = atualizada.replace('$MAE$', eleitor[1])
    atualizada = atualizada.replace('$PAI$',eleitor[2])
    atualizada = atualizada.replace('$ZONA$', eleitor[5])
    atualizada = atualizada.replace('$SEC$', eleitor[6])
    atualizada = atualizada.replace('$UF$', eleitor[8])
    atualizada = atualizada.replace('$HORA$', datetime.datetime.now().strftime('%X'))
    atualizada = atualizada.replace('$DATA$', datetime.datetime.now().strftime('%x'))
    atualizada = atualizada.replace('$DATA_DOMILICIO$', eleitor[9])
    pagina.close()

    nova_pagina = open('certidao_atualizada.html', 'w')
    nova_pagina.write(atualizada)
    nova_pagina.close()