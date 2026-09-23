import os
from mysql.connector import connect

def conectar():
    conexao = connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin",
        database="helpdesk"
    )
    #print("Conexão aberta com sucesso!")
    return conexao

def consultar_categorias():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cor_hex FROM categorias")
    registros = cursor.fetchall()

    cursor.close()
    conexao.close()
    print("Categorias:")
    for categoria in registros:
        print(categoria[0], "=>", categoria[1], "=>", categoria[2], "\n")

def cadastrar_categorias():
    nome = input("Digite o nome da categoria: ")
    cor_hex = input("Digite a cor: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO categorias (nome, cor_hex) VALUES (%s, %s)",
                   (nome, cor_hex)
                   )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Categoria cadastrada com sucesso")

def limpar_terminal():
    import os
    os.system("cls")






if __name__ == "__main__":
    menu = """MENU:
1    - Consultar categorias
2    - Cadastrar categoria
99   - Sair

Digite o menu desejado: """
    menu_escolhido = int(input(menu))

    while menu_escolhido != 99:
        limpar_terminal()
        if menu_escolhido == 1:
            consultar_categorias()
        elif menu_escolhido == 2:
            cadastrar_categorias()
        else:
            print("Opção inválida!")

        menu_escolhido = int(input(menu))