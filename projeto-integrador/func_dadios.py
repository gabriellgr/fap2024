import sqlite3
#stand by
tabela = '''
creat table if not exists leitos

'''

def salvar_dados(dados):
        dados_para_inserir = 'INSERT INTO dados (nome) VALUES (?)'
        valores = (dados)

        try:
            conexao = sqlite3.connect('dados_leitos.db')
            cursor = conexao.cursor()
            cursor.execute(dados_para_inserir, valores)  # Passando a tupla de valores
            conexao.commit()
            
            print('\nInserção dos dados completa!')
            
        except sqlite3.DatabaseError as erro:
            print("Erro ao inserir dados:", erro)
            
        finally:
            if conexao:
                conexao.close()
