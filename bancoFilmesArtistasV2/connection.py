import mysql.connector
from mysql.connector import Error

def criaBDmySql():
  try:
      connection = mysql.connector.connect(host='localhost',
                                           user='root',
                                           password='banzaiPipeleme_0')
      cursor = connection.cursor()
      cursor.execute("CREATE DATABASE IF NOT EXISTS filmes_artistas;")
      connection.commit()
      print("Base de dados 'filmes_artistas' existe no servidor local.\n")
  except Error as e:
      print("Erro de conexao - criaBDmySql()", e)
      return 0
  finally:
      if(connection.is_connected()):
          cursor.close()
          connection.close()
  return 1

def insereFilmes(nome, codigoIMDB):
  record = (codigoIMDB, nome)

  try:
    connection = mysql.connector.connect(host = 'localhost',
                                         user = 'root',
                                         password = 'banzaiPipeleme_0',
                                         database = 'filmes_artistas')
                          

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS filmes(codigoIMDB CHAR(32), nome VARCHAR(24), PRIMARY KEY (codigoIMDB));")

    sql = ("""INSERT INTO filmes (codigoIMDB, nome) VALUES (%s, %s);""")

    cursor.execute(sql, record)

    connection.commit()
    print(cursor.rowcount, "Registro Inserido - insereFilmes() ")
    
  except Error as e:
    print("Erro de conexao - insereFilmes()", e)
  
  finally:
    if(connection.is_connected):
      cursor.close()
      connection.close()
      print("Conexao Encerrada. insereFilmes()")  

  return  

def insereArtistas(nome, codigoDRT):
  
  record = (codigoDRT, nome)

  try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='banzaiPipeleme_0',
                                         database='filmes_artistas')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS artistas(codigoDRT VARCHAR(32), nome VARCHAR(24), PRIMARY KEY (codigoDRT))""")
    sql = ("""INSERT INTO artistas (codigoDRT, nome) VALUES (%s, %s);""")
    cursor.execute(sql, record)

    connection.commit()
    print(cursor.rowcount, "Registro Inserido - insereArtistas() ")

  except Error as e:
    print("Erro de conexao - insereArtistas()", e)

  finally:
    if(connection.is_connected()):
      cursor.close()
      connection.close()
      print("Conexao encerrada. - insereArtistas()")
  
  return

def criaRelacaoArtistasFilmes(codigoIMDB, codigoDRT):


  record = (codigoIMDB, codigoDRT)

  try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='banzaiPipeleme_0',
                                         database='filmes_artistas')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS participaDe(codigoIMDB CHAR(24), codigoDRT CHAR(32))""")

    sqlQuery = ("""INSERT INTO participaDe(codigoIMDB, codigoDRT) VALUES (%s, %s);""")
    cursor.execute(sqlQuery, record)

    connection.commit()
    print(cursor.rowcount, "Registro Inserido - criaRelacaoArtistasFilmes() ")

  except Error as e:
    print("Erro de conexao - criaRelacaoArtistasFilmes()", e)

  finally:
    if(connection.is_connected()):
      cursor.close()
      connection.close()
      print("Conexao encerrada - criaRelacaoArtistasFilmes()")
  
  return

def imprimeRelacaoFilmesArtistas():


  try:
    connection = mysql.connector.connect(host='localhost',
                                           user='root',
                                           password='banzaiPipeleme_0',
                                           database='filmes_artistas')
    cursor = connection.cursor()
  
    sqlQuery = ("""SELECT f.nome, a.nome FROM participaDe as p, filmes as f, artistas as a WHERE a.codigoDRT = p.codigoDRT AND f.codigoIMDB = p.codigoIMDB;""")
    cursor.execute(sqlQuery)
    rows = cursor.fetchall()

    print("\nLista com os nomes dos filmes e seus respectivos artistas: \n")
    for row in rows:
      final_result = [list(row)]
      print(row)
      print("\n")
    cursor.close()
    connection.commit()

  except Error as e:
    print("Erro de conexao - imprimeRelacaoArtistasFilmes()", e)

  finally:
    if(connection.is_connected()):
      cursor.close()
      connection.close()
      print("Conexao encerrada - imprimeRelacaoArtistasFilmes()")
  
  return



#criaBDmySql()
#insereFilmes() 
#insereFilmes()  
#insereFilmes()  
#insereFilmes()  
#nsereArtistas()
#insereArtistas()
#insereArtistas()
#insereArtistas()
#insereArtistas()
#insereArtistas()
#insereArtistas()
#insereArtistas()

#criaRelacaoArtistasFilmes()
#criaRelacaoArtistasFilmes()  
#criaRelacaoArtistasFilmes()
#criaRelacaoArtistasFilmes()

#imprimeRelacaoFilmesArtistas()

#FOREIGN KEY (codigoFilme) REFERENCES insereFilmes(codigoIMDB)