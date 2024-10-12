from Aprovacao.AlunosAprovados import construirListaDeAlunosAprovados
from CalcularMedia.CalcularMediaAluno import construirListaMediaDeAlunos
from ListaAlunos import Alunos


def AlunosAprovados():
    lista_media = construirListaMediaDeAlunos(Alunos)
    lista_aprovados = construirListaDeAlunosAprovados(Alunos, lista_media)

    return lista_aprovados