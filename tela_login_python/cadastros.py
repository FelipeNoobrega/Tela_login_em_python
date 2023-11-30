import pyodbc
import codigo as co

dadosConexao=(
    "Driver={SQL Server};"
    "Server=DESKTOP-NIPUJ95\SQLEXPRESS;"
    "Database=cadastros_bd;"
)

conexao=pyodbc.connect(dadosConexao)

print("conectado")
cursor=conexao.cursor()

#insere um novo cadastro no BD.
def insereCadastro(nome,idade,senha,senhaCodificada):
    insere=f"""INSERT INTO informacoesLogin (nome, idade, senha, senhaCod) 
    values ('{nome}', {idade}, '{senha}', '{senhaCodificada}')"""

    cursor.execute(insere)
    cursor.commit()
   
    print('Usuário cadastrado com sucesso!!!')

#faz uma pesuisa no BD.
def entrar(nome,senha):
    comando=f"""SELECT usuario, nome, senha FROM informacoesLogin 
    where senha ='{senha}' and nome ='{nome}'"""
    cursor.execute(comando)

    resultado=cursor.fetchone()
    
    
    try:
        if resultado[1] == nome and resultado[2] == senha: 
            return [False,resultado[0]]
    except:
        print('falha no login\nverifique o nome de usúario ou senha.')
        
        return True              

#faz update no campo específico com o novo valor direto no BD.
def update(campo,newValue,usuario):
    update = f"UPDATE informacoesLogin SET {campo} = '{newValue}' WHERE usuario = {usuario}"
    cursor.execute(update)
    conexao.commit()
    
    if campo == 'senha':
        newSenha = co.codifica(newValue)
        update2 = f"UPDATE informacoesLogin SET senhaCod = '{newSenha}' WHERE usuario = {usuario}"
        cursor.execute(update2)
        conexao.commit()
        

    print('\n',campo, 'alterado com sucesso!!!\n')
    co.opcao()
    

#deleta tupal inteiro do BD
def deleteCadastro(usuario):
    update = f"DELETE FROM informacoesLogin WHERE usuario = {usuario}"
    cursor.execute(update)
    print('\n Usuário deletado com sucesso\n\nObrigado por jogar\n')
    conexao.commit()
    

#relatorio do BD nome e idade
def relatorio():
    comando="""SELECT nome, idade FROM informacoesLogin """
    cursor.execute(comando)
    resultado=cursor.fetchall()
    
    return resultado



