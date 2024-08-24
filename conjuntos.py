def uniao(conjunto1, conjunto2):
    resultado = conjunto1.union(conjunto2)
    return 'União', resultado

def intersecao(conjunto1, conjunto2):
    resultado = conjunto1.intersection(conjunto2)
    return 'Interseção', resultado

def diferenca(conjunto1, conjunto2):
    resultado = conjunto1.difference(conjunto2)
    return 'Diferença', resultado

def produto_cartesiano(conjunto1, conjunto2):
    resultado = { (x, y) for x in conjunto1 for y in conjunto2 }
    return 'Produto cartesiano', resultado

operacoes_funcao = {
    'U': uniao,
    'I': intersecao,
    'D': diferenca,
    'C': produto_cartesiano
}

def resultado_conjuntos(conjuntos_file):
    with open(conjuntos_file, 'r') as file:
        linhas = file.readlines()

    resultados = []
    num_operacoes = int(linhas[0].strip())
    indice = 1

    for _ in range(num_operacoes):
        operacao = linhas[indice].strip()
        conjunto1 = set(linhas[indice + 1].strip().split(','))
        conjunto2 = set(linhas[indice + 2].strip().split(','))

        op_nome, resultado = operacoes_funcao.get(operacao, (None, None))(conjunto1, conjunto2)
        if op_nome:
            resultado_formatado = ', '.join(map(str, sorted(resultado)))
            conjunto1_formatado = ', '.join(map(str, sorted(linhas[indice + 1].strip().split(','))))
            conjunto2_formatado = ', '.join(map(str, sorted(linhas[indice + 2].strip().split(','))))

            resultado_linha = f"{op_nome}: conjunto 1 {{{conjunto1_formatado}}}, conjunto 2 {{{conjunto2_formatado}}}. Resultado: {{{resultado_formatado}}}"
            resultados.append(resultado_linha)

        indice += 3

    for resultado in resultados:
        print(resultado)

conjuntos_file = 'op0.txt'
resultado_conjuntos(conjuntos_file)
