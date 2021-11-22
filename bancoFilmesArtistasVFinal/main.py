#interface usuário

import connection as db

def insereFilmesInterface():
    nome = str(input("\nNome do filme:\n"))
    codigoIMDB = str(input("\nCodigo IMDB de lançamento do filme:\n"))
    db.insereFilmes(nome, codigoIMDB)
    rUser = str(input("\nDeseja incluir mais algum registro? (S/n)'\n"))
    if rUser == 'S':
        return insereFilmesInterface()
    elif rUser == 'n':
        return


def insereArtistasInterface():
    nome = str(input("\nNome do artista:\n"))
    codigoDRT = str(input("\nCodigo do DRT do artista " + nome + ":\n"))
    db.insereArtistas(nome, codigoDRT)
    rUser = str(input("\nDeseja incluir mais algum registro? (S/n)'\n"))
    if rUser == 'S':
        return insereArtistasInterface()
    elif rUser == 'n':
        return

def insereParticipaDeInterface():
    print("\nInsira o codigo IMDB de lancamento do filme e o codigo DRT do artista que participa no mesmo:\n")
    codigoIMDB = str(input("\n\tIMDB:\n\t"))
    codigoDRT = str(input("\tDRT\n\t"))
    db.criaRelacaoArtistasFilmes(codigoIMDB, codigoDRT)
    rUser = str(input("\nDeseja incluir mais algum registro? (S/n)n\n"))
    if rUser == 'S':
        return insereParticipaDeInterface()
    elif rUser == 'n':
        return 

def main():

    db.criaBDmySql()

    rUser = str(input("Deseja incluir algum filme no banco? (S/n)"))
    if rUser == 'S':
       insereFilmesInterface()
    rUser = str(input("Deseja incluir algum artista no banco? (S/n)"))
    if rUser == 'S':
        insereArtistasInterface()
    rUser = str(input("\nDeseja incluir o registro de algum artista que participa de determinado filme? (S/n)"))
    if rUser == 'S':
        insereParticipaDeInterface()
    
    db.imprimeRelacaoFilmesArtistas()

    return

main()

