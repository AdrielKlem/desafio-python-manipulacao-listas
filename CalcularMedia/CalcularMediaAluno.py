def construirListaMediaDeAlunos(Alunos):
    # print("=>   Calculando a media do Aluno...\n\n")

    lista_aluno_e_media = {}
 
    for aluno in Alunos:

        nome = aluno.nome
        nota_primeiro_semestre = aluno.notas["1 Semestre"]
        nota_segundo_semestre = aluno.notas["2 Semestre"]


        media = calcularMedia(nota_primeiro_semestre, nota_segundo_semestre)
        lista_aluno_e_media[nome] = media


        # print(f"Aluno {nome}")
        # print(f"----------")
        # print(f"Nota Primeiro Semestre: {nota_primeiro_semestre}")
        # print(f"Nota Segundo Semestre: {nota_segundo_semestre}")
        # print(f"E sua media e: {media}")
        # print(f"----------")
        # print("\n")

    return lista_aluno_e_media

def calcularMedia(nota_primeiro_semestre, nota_segundo_semestre):
    notas = 0

    notas += nota_primeiro_semestre + nota_segundo_semestre
    media = notas/2


    return media