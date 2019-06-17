def cadastrar_aluno():
    aluno = input("Digite o nome do aluno: ")
    listaNota = []
    soma = 0
    for i in range (3):
        listaNota.append(float(input("Digite a nota {0}: ".format(i))))
        soma = soma + listaNota[i]
    media = soma / 3
    if media >= 5.75:
        print("Aluno {0} aprovado nota: {1:.2f}".format(aluno, media))
        status = 'Aprovado'
    elif media >= 3:
        print("Aluno {0} em recuperação nota: {1:.2f}".format(aluno, media))
        status = 'Recuperação'
    else:
        print("Aluno {0} reprovado :( nota: {1:.2f}".format(aluno, media))
        status = 'Reprovado'
    a = {'nome': aluno, 'media': media, 'Status': status}
    return a

turma = []

for i in range(2):
    turma.append(cadastrar_aluno())

for aluno in turma:
    print(aluno)

print(turma[0]['nome'])