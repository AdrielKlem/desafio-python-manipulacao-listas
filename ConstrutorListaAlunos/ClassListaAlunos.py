class Aluno:
    nome: str
    notas: dict  # Dicionário para armazenar as notas por semestre

    def __init__(self, nome, notaPrimeiroSemestre, notaSegundoSemestre):
        self.nome = nome
        self.notas = {
            "1 Semestre": notaPrimeiroSemestre,
            "2 Semestre": notaSegundoSemestre
        }