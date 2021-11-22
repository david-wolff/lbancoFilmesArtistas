#módulo de conexão, inserção e consultas no banco de dados local.

import mysql.connector
from mysql.connector import Error

#Função que cria o banco de dados caso o mesmo não exista. 
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

#Função que insere os filmes no banco de dados com as chaves 'nome' e 'codigoIMDB'(PK)
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

#Função que insere os artistas no banco de dados com as chaves 'nome' e 'codigoDRT'(PK)
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


#Função que insere os filmes e seus respectivos artistas no banco de dados com as chaves 'codigoDRT'(FK -> artistas(codigoDRT) e 'codigoIMDB'(FK -> filmes(codigoIMDB))
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
    sqlQuery = ("""SELECT * FROM participaDe;""")
    cursor.execute(sqlQuery)
    participaDe = list(cursor.fetchall())
    sqlQuery = ("""SELECT * FROM filmes;""")
    cursor.execute(sqlQuery)
    filmes = list(cursor.fetchall())
    sqlQuery = ("""SELECT * FROM artistas;""")
    cursor.execute(sqlQuery)
    artistas = list(cursor.fetchall())
    cursor.close()
    
  except Error as e:
    print("Erro de conexao - imprimeRelacaoArtistasFilmes()", e)
    
    #Seguinte query seleciona todos os nomes dos filmes e dos artistas dentro das tabelas 'filmes' e 'artistas' de acordo com as FK's dentro de participaDe.  
 
    cursor.close()
    connection.commit() 
  finally:
    if(connection.is_connected()):
      cursor.close()
      connection.close()
      print("Conexao encerrada - imprimeRelacaoArtistasFilmes()")
  lista5Artistas = []
  listaPart = []
  for linhaFilme in filmes:
    count = 0
    for linhaArtista in artistas:
      for linhapd in participaDe:
        if linhaFilme[0] == linhapd[0]:
          if linhaArtista[0] == linhapd[1]:
            if count in range(4):
              lista5Artistas.append(linhaArtista[1])
              lista5Artistas.append(linhaFilme[1]) 
    count += 1
  
  print("\n5 artistas de cada filme:\n")
  print(lista5Artistas)
  
  artistaConsulta = str(input("\nDigite o codigo DRT de um artista para verificar suas participações nos filmes listados:"))
  for c in artistas:
    if c[0] == artistaConsulta:
      nomeArtistaConsulta = c[1]
  print("\nFilmes em que o artista " + nomeArtistaConsulta + " participou: \n")
  
  for linhaArtista in artistas:
    if artistaConsulta == linhaArtista[0]:
      for linhapd in participaDe:  
        if linhapd[1] == artistaConsulta:
          for linhaFilme in filmes:
            if linhapd[0] == linhaFilme[0]:
              listaPart.append(linhaFilme[1])
  
  print(listaPart)
  return



