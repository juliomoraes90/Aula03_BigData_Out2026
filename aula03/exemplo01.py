#Entrada
salario_atual = float(input('Digite seu salário atual: '))
#Processamento
percentual = float(input('Digite o digito para percentual: '))
percentual = percentual / 100
aumento = salario_atual * percentual
novo_salario = salario_atual + aumento
#saida
print(f'Salário original: R$ {salario_atual:.2f}\nValor do reajuste: R$ {aumento:.2f}\nNovo salário do funcionário já reajustado: R$ {novo_salario:.2f}')