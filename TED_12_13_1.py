'''Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, chame este dicionário de glossário.
Pense em cinco palavras relacionada à programação que você conheceu nesta disciplina. Use estas palavras como chaves em seu glossário e armazene seus significados como valores.
Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante. Por exemplo: você pode exibir a palavra seguida de dois-pontos e depois o seu significado, ou apresentar a palavra em uma linha e então exibir seu significado identado em uma segunda linha. Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada par palavra-significado em sua saída.
Sugestões de termos: Algoritmos, Python, Webscraping, Lógica de Programação, Google Colab, Visual Studio Code.
'''
glossario = {
    'Python' : 'Python é uma linguagem de programação de alto nível, do termo em inglês, high level language.',
    'Webscraping' : 'Webscraping é o nome dado ao processo de coleta de dados estruturados da web de maneira automatizada.',
    'Lógica_de_Programação' : 'Lógica de programação é a técnica de encadear pensamentos para atingir determinado objetivo.',
    'Google_Colab' : 'O Google Colab é a área de pesquisas científicas do Google.',
    'Visual Studio Code' : 'O Visual Studio Code (VS Code) é um editor de código de código aberto desenvolvido pela Microsoft.'
}

for i in glossario:
    deco = '-'*50
    print(f'{deco}\n\n{i}:\n{glossario[i]}\n')
