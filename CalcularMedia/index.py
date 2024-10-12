from CalcularMedia.CalcularMediaTurma import calcularMediaTurma
from CalcularMedia.CalcularMediaAluno import construirListaMediaDeAlunos

def calcularMedia(Alunos):
    # print("# Preparando o calculo da media...\n")
    calcularMediaTurma(Alunos)
    construirListaMediaDeAlunos(Alunos)
