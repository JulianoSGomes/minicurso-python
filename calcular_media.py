def media_final(nota1,  nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

def aprovacao(nota):
    if nota >= 5.75:
        return "aprovado"
    else:
        return "reprovado"

if __name__ == "__main__":
    media = media_final(8, 7,  6)
    print("A média é: ", media)