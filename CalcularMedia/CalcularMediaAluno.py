def calcularMediaAluno(Alunos):
    print("=>   Calculando a media do Aluno...\n\n")

 
    for aluno in Alunos:
        notas = 0
        media = 0

        nome = aluno.nome
        nota_primeiro_semestre = aluno.notas["1 Semestre"]
        nota_segundo_semestre = aluno.notas["2 Semestre"]

        notas += nota_primeiro_semestre + nota_segundo_semestre
        media = notas/len(aluno.notas)

        print(f"Aluno {nome}")
        print(f"----------")
        print(f"Nota Primeiro Semestre: {nota_primeiro_semestre}")
        print(f"Nota Segundo Semestre: {nota_segundo_semestre}")
        print(f"E sua media e: {media}")
        print(f"----------")
        print("\n")

        
    print("\n")