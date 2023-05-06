import os
import library_PF

caminho = os.path.join('ProjetoFinal','dados.csv')

#library_PF.cadastro_eleitor(caminho)

myFile = open(caminho, 'r')
linhas = myFile.readlines()

for i in linhas:
    line = i.split(';')

    if line[0] == 'Gabriel':
        print(line)
     
myFile.close()






