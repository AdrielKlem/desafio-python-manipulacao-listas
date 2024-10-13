from CalcularMedia.CalcularMediaAluno import construirListaMediaDeAlunos
from ConstrutorListaAlunos.ListaAlunos import Alunos


def AlunosAprovados():
    lista_aluno_e_media = construirListaMediaDeAlunos(Alunos) 
    lista_aprovados = construirListaDeAlunosAprovados(Alunos, lista_aluno_e_media)

    return lista_aprovados


def construirListaDeAlunosAprovados(Alunos, lista_aluno_e_media): # A média é 7
    lista_dos_aprovados = []

    for aluno in Alunos:
        if lista_aluno_e_media[aluno.nome] >= 7:
           lista_dos_aprovados.append(aluno.nome) 

    return lista_dos_aprovados

