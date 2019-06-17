import calcular_media 

def inserir():
    ident = int(input("Digite o identificador do aluno: ")) #número de identificação do aluno ex: Matrícula
    nome  = input("Digite o  nome do aluno: ")              #Lê o nome do  aluno     
    nota1 = float(input("Digite a 1° nota do  aluno: "))    #Lê as notas do  aluno
    nota2 = float(input("Digite a 2° nota do  aluno: "))
    nota3 = float(input("Digite a 3° nota do  aluno: "))
    media = calcular_media.media_final(nota1, nota2, nota3) #Cálcula a média utilizando a função  que está no arquivo calcular_media (note o import) 
    aprovado = calcular_media.aprovacao(media)              #Verifica se  o aluno  está aprovado ou não através da função  que está no arquivo calcular_media
    aluno = {"id": ident, "nome": nome, "nota1": nota1, "nota2": nota2, "nota3": nota3, "media": media, "aprovado": aprovado} #dicionário  que contém informações do aluno
    return aluno

turma = []    #inicializa lista da turma
qtd_alunos = 2 # quantidade de alunos que estão na turma

for i in range(qtd_alunos):   
    turma.append(inserir())   #insere o aluno na  turma através da função  inserir

for aluno in turma:     #Lista os alunos da  turma, suas notas, média e status de aprovado ou não
    print("\n{} - As notas do(a) aluno(a) {} são: {} {} {} com média {} e está {}(a) ".format(aluno['id'],
                                                                                    aluno['nome'], 
                                                                                    aluno['nota1'], 
                                                                                    aluno['nota2'], 
                                                                                    aluno['nota3'], 
                                                                                    aluno['media'],
                                                                                    aluno['aprovado']))

