'''
How to use:
    When you run the code you will be asked to give in a text whose author you don't know. After that you will be asked to enter texts from people who could be the writer of the first you put in. Press enter twice when you're done and the algotithm will try to figure out which of the given texts has the same author as the first one put in.

    Disclaimer: Every text has to be adjusted in order to have no newline characters since that character is used to stop inputing a text and starting a new one.
    '''


# Possui ferramentas de manipulação de string
import re
import os

'''
Lê todos os textos adicionais para compara-los com a base
'''
def leTextos() :

    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    os.system("clear")
    while texto:
        textos.append(texto)
        i = i + 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        os.system("clear")

    return textos


def separaSentencas(texto) :
    sentencas = re.split(r'[.!?]+', texto)

    if sentencas[len(sentencas) - 1] == '':
        del sentencas[len(sentencas) - 1]

    return sentencas

def separaFrases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separaPalavras(frase):
    return frase.split()

def nPalavrasUnicas(lista_palavras):
    # dict() retorna algo similar a um mapa da STL (c++)
    freq = dict()
    unicas = 0

    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def nPalavrasDiferentes(lista_palavras):

    frequencia = dict()
    for palavra in lista_palavras:
        # lower() transforma as maiúsculas em minúsculas
        i = palavra.lower()
        if i in frequencia:
            frequencia[i] += 1
        else:
            frequencia[i] = 1

    return len(frequencia)

'''
Retorna o índice de similaridade entre 2 assinaturas
'''
def comparaAssinatura(as_a, as_b) :
    similaridade = 0

    for i in range(len(as_a)) :
        similaridade = similaridade + abs(as_a[i] - as_b[i])
    return similaridade / 6


'''
Essa função calcula as diferentes assinaturas do texto na ordem: 
    1 - Tamanho médio de palavra.
    2 - Relação Type-Token.
    3 - Razão Lapax Legomana.
    4 - Tamanho médio de sentença.
    5 - Complexidade de sentença.
    6 - Tamanho médio de frase.
'''
def calculaAssinatura(texto) :

    assinatura = []

    # Cria arrays para os diferentes tipo de dados presentes em um texto
    sentencas = separaSentencas(texto)
    frases = []
    for i in sentencas : 
        frases = frases + separaFrases(i)

    palavras = []
    for i in frases :
        palavras = palavras + separaPalavras(i)

    caracteres = 0
    for i in palavras : 
        caracteres = caracteres + len(i)

    tam_sentenca = 0

    for i in sentencas :
        tam_sentenca = tam_sentenca + len(i)

    tam_frase = 0

    for i in frases :
        tam_frase = tam_frase + len(i)

    #Calcula os valores e vai colocando-os em um array para retornar a assinatura completa
    assinatura.append(caracteres / len(palavras))
    assinatura.append(nPalavrasDiferentes(palavras) / len(palavras))
    assinatura.append(nPalavrasUnicas(palavras) / len(palavras))
    assinatura.append(tam_sentenca / len(sentencas))
    assinatura.append(len(frases) / len(sentencas))
    assinatura.append(tam_frase / len(frases))
    
    return assinatura

'''
Recebe uma lista de textos e um texto base e identifica qual dos textos da lista é mais semelhante à base
'''
def avaliaTextos(textos, ass_cp) :

    assinaturas = []
    for i in textos : 
        assinaturas.append(calculaAssinatura(i))

    indice = [0] * len(textos)

    for j in range(len(assinaturas)) : 
        for i in range(len(assinaturas[0])) : 
            indice[j] = indice[j] + abs(ass_cp[i] - assinaturas[j][i])

    copiado = 0

    for i in range(len(indice)) :
        indice[i] = indice[i] / len(assinaturas[0])
        if indice[i] <= indice[copiado] :
            copiado = i

    
    print("O autor do texto", copiado + 1, "provavelmente é o mesmo do texto base")
    return copiado + 1

def calculaTextoBase() : 
    texto = input("Digite o texto base: ")
    os.system("clear")
    return calculaAssinatura(texto)

def main() :

    ass_cp = calculaTextoBase()

    textos = leTextos()

    avaliaTextos(textos, ass_cp)


if __name__ == "__main__" : 
    main()