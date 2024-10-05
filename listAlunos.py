class Aluno:
    nome: str
    nota: float         

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

aluno1 = Aluno("Adriel", 12)

print(aluno1.nome)
print(aluno1.nota)

ListaAlunos = "Hello, World"
