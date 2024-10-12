def construirListaDeAlunosAprovados(Alunos, lista_media):
    # A média é 7
    lista_dos_aprovados = []

    for aluno in Alunos:
        if lista_media[aluno.nome] >= 7:
           lista_dos_aprovados.append(aluno.nome) 

    return lista_dos_aprovados

