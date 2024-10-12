from Aprovacao.index import AlunosAprovados

def ImprimirResultado():
    lista = AlunosAprovados()

    for aluno in lista:
        print("---------------")
        print(f"Parabéns {aluno}!!!\nEstá Aprovado(a)")
        print("---------------\n")
