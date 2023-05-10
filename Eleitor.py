import os
import library_PF

opcao = 0

opcao = int(input('\nPara cadastrar um novo eleitor, digite 1. Para emitir Certidão de quitação eleitoral, digite 2: '))

while opcao != 1 and opcao != 2:
    print('\nOpcao invalida.')
    opcao = int(input('Para cadastrar um novo eleitor, digite 1. Para emitir Certidão de quitação eleitoral, digite 2: '))

if opcao == 1:
    library_PF.cadastro_eleitor('eleitores.csv')
else: 
    print('\nPara emissao da Certidão de quitação eleitoral, informe os dados abaixo: \n')

    nome = input("Nome completo: ")
    nome_mae = input("Nome da mae: ")
    id = input("Número do título: ")

    if library_PF.valida_eleitor('eleitores.csv', nome, id, nome_mae):
        library_PF.emite_certidao('eleitores.csv', nome, nome_mae, id)
