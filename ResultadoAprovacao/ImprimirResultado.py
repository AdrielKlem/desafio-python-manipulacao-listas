from Aprovacao.AlunosAprovados import AlunosAprovados

def ImprimirResultado():
    lista = AlunosAprovados() # Método para criar a lista dos aprovados

    for aluno in lista:
        print("---------------")
        print(f"Parabéns {aluno}!!!\nEstá Aprovado(a)")
        print("---------------\n")
