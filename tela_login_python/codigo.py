
import cadastros as ca
 

def codifica(senha):
    cod=[]
    for i in range (len(senha)):
        opera=0
        opera= ord(senha[i])
        opera=chr(opera+3)
        cod.append(opera)
       
    cod.reverse()
    position0=cod[0]
    cod[0]=cod[len(cod)-1]
    cod[len(cod)-1]=position0
    
    juncao = ''
    novaSenha= juncao.join(cod)
    
    return novaSenha

def validaCadastro(resposta):
    resposta=resposta.upper()
    if resposta=='S':
        entrar()
    if resposta=='N':
        criaCadastro()

def criaCadastro():
    print('Dados pessoais')
    print()
    nome=input('\nfirst name: ')
    idade=int(input('\nidade: '))
    senha=input('\nDigite sua Senha de 8 dígitos: ')
    print()
    nome.upper()
    senhaCodificada=codifica(senha)
    ca.insereCadastro(nome,idade,senha,senhaCodificada)
    
    print()
    entrar()

def entrar():
    print('\nLOGIN')
    print()
    login=True
    while login:
        name=input('NOME:')
        senha=input('SENHA:')
        print()
        login=ca.entrar(name,senha)

        if login[0] == False:
            jogo(login[1])
            print()
            break

        
def opcao():
    repetir = True
    while repetir :
        testa = input('jogar novamente [s] ou [n] ? ')
        testa=testa.upper()
        print()
        if testa =='S':
            repetir=False
            entrar()
        elif testa== 'N':
            testa2 = input('Deseja cadastrar outro jogador [s] ou [n] ? ')
            testa2=testa2.upper()
            print()
            if testa2=='S':
                repetir=False
                criaCadastro()
            else:
                repetir=False
                print()
                print ('obrigado por jogar.')
                    
    
def jogo(usuario=0):
    print ('\nBEM VINDO AO JOGO\n')
    opcoes=int(input('\n1. alterar cadastro\n2. excluir cadastro\n3. relatório de cadastro\n4. sair\n\n: '))
    
    if opcoes==1:
        update= input('\nDigite o nome do campo que será alterado:\n\n.NOME\n.IDADE\n.SENHA\n.SAIR\n\n: ')
        update=update.upper()
        if update=='NOME':
    
            name=input('Digite o novo nome: ')
            campo='nome'
            ca.update(campo,name,usuario)

        elif update=='IDADE':
            idade = int(input('Digite a nova idade: '))
            campo = 'idade'
            ca.update(campo,idade,usuario)

        elif update == 'SENHA':
            senha = input('Digite a nova senha de 8 digitos: ')
            campo = 'senha'
            ca.update(campo,senha,usuario)
        else:
            opcao()

    elif opcoes == 2:

        ca.deleteCadastro(usuario)
        opcao()

    elif opcoes==3:
        relatorio = ca.relatorio()
        print('\nRELATÓRIO')
        for i in range(len(relatorio)):
            print('nome:',relatorio[i][0],' idade:',relatorio[i][1])
        opcao()
    else:
        opcao()