import calcular_media 

def inserir():
    ident = int(input("Digite o identificador do aluno: "))
    nome  = input("Digite o  nome do aluno: ")
    nota1 = float(input("Digite a 1° nota do  aluno: "))
    nota2 = float(input("Digite a 2° nota do  aluno: "))
    nota3 = float(input("Digite a 3° nota do  aluno: "))
    media = calcular_media.media_final(nota1, nota2, nota3)
    aprovado = calcular_media.aprovacao(media)
    aluno = {"id": ident,
             "nome": nome, 
             "nota1": nota1, 
             "nota2": nota2, 
             "nota3": nota3, 
             "media": media,
             "aprovado": aprovado}
    return aluno

alunos = []

for i in range(3):
    alunos.append(inserir())

for aluno in alunos:
    print("\n{} - As notas do aluno {} são: {} {} {} com média {} e está {} ".format(aluno['id'],
                                                                                    aluno['nome'], 
                                                                                    aluno['nota1'], 
                                                                                    aluno['nota2'], 
                                                                                    aluno['nota3'], 
                                                                                    aluno['media'],
                                                                                    aluno['aprovado']))

