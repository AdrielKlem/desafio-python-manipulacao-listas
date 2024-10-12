def calcularMediaTurma(Alunos):
    print("=>   Calculando media da turma...")

    notas = 0
    quantidadeDeAlunos = len(Alunos)
 
    for aluno in Alunos:
        # nome = aluno.nome
        nota_primeiro_semestre = aluno.notas["1 Semestre"]
        nota_segundo_semestre = aluno.notas["2 Semestre"]

        # print(f"Aluno {nome}")
        # print(f"----------")
        # print(f"Nota Primeiro Semestre: {nota_primeiro_semestre}")
        # print(f"Nota Segundo Semestre: {nota_segundo_semestre}")
        # print(f"----------")
        
        notas += nota_primeiro_semestre + nota_segundo_semestre

    mediaTurma = notas/quantidadeDeAlunos
    
    print(f"A media da turma foi de: {mediaTurma}")
    print("\n")