soma = 0
qtd = 0
somapos = 0
qtdneg = 0
somapar = 0
qtdpar = 0
qtdimpar = 0
print('Digite 5 números: ')
for i in range(0,5):
    num = int(input())
    soma += num
    qtd += 1
    if num > 0:
        somapos += num
    else:
        qtdneg += 1
    if num % 2 == 0:
        somapar += num
        qtdpar += 1
    else:
        qtdimpar += 1
if qtd == 0:
    print(f'a) A soma dos números digitados: {soma}')
    print(f'b) A quantidade de números digitados: {qtd}')
    print(f'd) A soma dos números positivos: {somapos}')
    print(f'e) A quantidade de números negativos: {qtdneg}')
else:
    print(f'a) A soma dos números digitados: {soma}')
    print(f'b) A quantidade de números digitados: {qtd}')
    print(f'c) A média dos números digitados: {soma/qtd}')
    print(f'd) A soma dos números positivos: {somapos}')
    print(f'e) A quantidade de números negativos: {qtdneg}')
    print(f'f) A média dos números pares: {somapar/qtdpar}')
    print(f'g) O percentual dos números ímpares entre todos os números digitados: {qtdimpar/qtd * 100}%')
