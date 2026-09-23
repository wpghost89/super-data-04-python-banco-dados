from mysql.connector import connect

def conectar():
    conexao = connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin",
        database="loja_db"
    )
    print("Conexão aberta com sucesso")
    return conexao

def consultar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, descricao FROM produtos")
    registros = cursor.fetchall()
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produtos:")
    for produto in registros:
        #print("Id:", produto[0], "\nNome:", produto[1], "\nDescrição:", produto[2], "\n\n")
        print(produto[0], "=>", produto[1], "=>", produto[2], "\n")

def cadastrar_produtos():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produtos (nome, descricao) VALUES (%s, %s)",
                   (nome, descricao)
                   )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto cadastrado com sucesso")
    # O que é sql injection = é uma falha de segurança em sistemas web que permite a invasores inserirem códigos maliciosos em campos de entrada de dados para manipular consultas feitas a um banco de dados.

def apagar_produto():
    id_produto = int(input("Digite o id do produto para apagar: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto apagado com sucesso!")

def editar_produto():
    id_produto = int(input("Digite o id do produto para editar: "))
    novo_nome = input("Digite o nome do produto: ")
    nova_descricao = input("Digite a descrição: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE produtos SET nome = %s, descricao = %s WHERE id = %s ",
        (novo_nome, nova_descricao, id_produto)
         )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto alterado com sucesso!") 

# Criar uma tabela de clientes com duas colunas id e nome
# Inserir dois registros na tabela de clientes
# Criar a função cadastrar_cliente no main.py
#   Implementar a lógica de pedir o nome do cliente e cadastrar 
#   o cliente com python e mysql
#   Adicionar no menu principal para usuário poder chamar o cadastro do cliente
# Criar a função apagar_cliente no main.py e implementar
# Criar a função editar_cliente no main.py e implementar
# Criar a função consultar_clientes no main.py e implementar
# Alterar a tabela de clientes adicionando a coluna de cnpj
# Modificar a função de cadastrar_cliente para solicitar o cnpj do 
#   cliente e cadastrar com o cnpj
# Modificar todas as demais funções de editar e consultar

# Alterar a tabela de clientes adicionando a coluna de endereço, telefone, email, limite_credito
# Modificar as funções de cadastro, editar e consultar

def consultar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cnpj, endereco, telefone, email, limite_credito FROM clientes")
    registros = cursor.fetchall()
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Clientes:")
    for cliente in registros:
        #print("Id:", cliente[0], "\nNome:", cliente[1], "\nDescrição:", cliente[2], "\n\n")
        print(cliente[0], "=>", cliente[1], "=>", cliente[2], "=>", cliente[3], "=>", cliente[4], "=>", cliente[5], "=>", cliente[6], "\n")

def cadastrar_cliente():
    nome = input("Digite o nome do Cliente: ")
    cnpj = input("Digite o CNPJ: ")
    endereco = input("Digite o endereço: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    limite_credito = input("Digite o limite de crédito: ");
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, cnpj, endereco, telefone, email, limite_credito) VALUES (%s, %s, %s, %s, %s, %s)",
        (nome, cnpj, endereco, telefone, email, limite_credito)
        )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Cliente cadastrado com sucesso")

def apagar_cliente():
    id_cliente = int(input("Digite o id do cliente para apagar: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Cliente apagado com sucesso!")

def editar_cliente():
    id_cliente = int(input("Digite o id do cliente para editar: "))
    novo_nome = input("Digite o nome do cliente: ")
    novo_cnpj = input("Digite o cnpj: ")
    novo_endereco = input("Digite o endereço: ")
    novo_telefone = input("Digite o telefone: ")
    novo_email = input("Digite o email: ")
    novo_limite_credito = input("Digite o limite de crédito: ");

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE clientes SET nome = %s, cnpj = %s, endereco = %s, telefone = %s, email = %s, limite_credito = %s WHERE id = %s ",
        (novo_nome, novo_cnpj, novo_endereco, novo_telefone, novo_email, novo_limite_credito, id_cliente)
         )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Cliente alterado com sucesso!") 


def limpar_terminal():
    import os
    os.system("cls")

if __name__ == "__main__":
    #conectar()
    menu = """MENU:
1    - Consultar produtos
2    - Cadastrar produto
3    - Apagar produto
4    - Editar produto
5    - Consultar clientes
6    - Cadastrar cliente
7    - Apagar cliente
8    - Editar cliente
99   - Sair

Digite o menu desejado:"""
    menu_escolhido = int(input(menu))

    while menu_escolhido != 99:
        limpar_terminal()
        if menu_escolhido == 1:
            consultar_produtos()
        elif menu_escolhido == 2:
            cadastrar_produtos()
        elif menu_escolhido == 3:
            apagar_produto()
        elif menu_escolhido == 4:
            editar_produto()
        elif menu_escolhido == 5:
            consultar_clientes()
        elif menu_escolhido == 6:
            cadastrar_cliente()
        elif menu_escolhido == 7:
            apagar_cliente()
        elif menu_escolhido == 8:
            editar_cliente()
        else:
            print("Opção inválida!")

        menu_escolhido = int(input(menu))

