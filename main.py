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
      print("Base de dados 'filmes_artistas' criada com sucesso.\n")
  except Error as e:
      print("Erro de conexao - criaBDmySql()", e)
      return 0
  finally:
      if(connection.is_connected()):
          cursor.close()
          connection.close()
          print("Base de dados 'filmes_artistas' existe no servidor local.\n")
  return 1

def insereFilmes():
  nome = str(input("\nNome do filme:\n"))
  codigoIMDB = str(input("\nCodigo IMDB de lançamento do filme:\n"))
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
    
  except Error as e:
    print("Erro de conexao - insereFilmes()", e)
  
  finally:
    if(connection.is_connected):
      cursor.close()
      connection.close()
      print("Conexao Encerrada. insereFilmes()")  

  return  

def insereArtistas():
  nome = str(input("\nNome do artista:\n"))
  codigoDRT = str(input("\nCodigo do DRT do artista " + nome + ":\n"))

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

  except Error as e:
    print("Erro de conexao - insereArtistas()", e)

  finally:
    if(connection.is_connected()):
      cursor.close()
      connection.close()
      print("Conexao encerrada. - insereArtistas()")
  
  return

def criaRelacaoArtistasFilmes():
  print("\nInsira o codigo IMDB de lancamento do filme e o codigo DRT do artista que participa no mesmo:\n")
  codigoIMDB = str(input("\n\tIMDB:\n\t"))
  codigoDRT = str(input("\tDRT\n\t"))

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

    for row in rows:
      final_result = [list(row)]
      print(row)

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

imprimeRelacaoFilmesArtistas()

#FOREIGN KEY (codigoFilme) REFERENCES insereFilmes(codigoIMDB)