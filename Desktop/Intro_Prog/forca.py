import uteis.desenhoforca
import random

palavra=str
dica=str
arq='biblioteca.txt'
arq2='dicas.txt'
dicas=[]
dicas2=[]
dicas3=[]

menu=0
cont=0
nome=''
nome=input(str('Qual seu nome:'))
ganhou=0
perdeu=0
print(f'Olá {nome}, seja bem vindo!!!')
while True:
    # Menu do jogo
    print ('Jogo da forca'.center(30))
    print('(1) JOGAR'.center(30))
    print('(2) Inserir novas palavras'.center(30))
    print('(3) SAIR'.center(30))
    print(30*'=')
    op=int(input('Digite a opção desejada:'))
    print (f'{nome} voce jogou {cont} vezes')
    print (f'Vitórias {ganhou} e derrotas {perdeu} até o momento')
    if op == 1:
        cont+=1
        erros = 0
        # abre o aquivo biblioteca.txt para leitura dividindo as stings
        lines = open('biblioteca.txt').read().split()
        myline = random.choice(lines)

        lines2 = open('dicas.txt').read().split()
        for linha in lines:
            if linha == myline:
                teste = linha


                with open('dicas.txt') as f:
                    for l in f:  # percorrer linhas e enumera-las a partir de 1
                        if teste in l:  # ver se palavra esta na linha
                            dicas = l
                            dicas2 = dicas.split('=')
                            dicas3 = dicas2[1]
                            print('DICA: ',dicas3)
        #print(myline)

        temp = []
        for letra in myline:
            temp.append('_')
        while True:
            print('\n'*3)  # limpa a tela
            uteis.desenhoforca.forca(erros)  # imprime desenho da forca

            # imprime a adivinhacao
            print('\n\nAdivinhe: ', end ='')

            for let in temp:
                print(let, end=' ')
            print('\n'*2)
            print('DICA: ', dicas3)

            # Verifica se perdeu
            if erros == 6:
                perdeu+=1
                break  # sai do jogo (sai do while)

            # Verificar se o jogador ganhou
            ganhouJogo = True
            for let in temp:
                if let == '_' :
                    ganhouJogo = False
            if ganhouJogo:
                print('\nPARABÉNS VENCEDOR!!!')
                ganhou+=1

                break

                # captura a letra do usuario
            letraDig = input('Informe uma letra: ')
            letrast=[]
            letrast.append(letraDig) #Armazena as letras digitadas
            # verifica se acertou alguma letra
            errouLetra = True
            for i, let in enumerate(myline):
                if myline[i] == letraDig.upper():
                    temp[i] = myline[i]
                    errouLetra = False
            if errouLetra:
                erros = erros + 1

    if op == 2:
        palavra=(str(input('Entre com a nova palavra:')))
        dica=(str(input('Entre com a dica:')))
        a = open(arq, 'at')
        b = open(arq2, 'at')
        a.write(f'{palavra}\n')
        b.write(f'{palavra} = {dica}\n')
        a.close()
        b.close()


    if op == 3:
        print('Volte Sempre!!!')
        break

