#Entrada
salario_atual = float(input('Digite seu salário atual: '))
#Processamento
aumento = salario_atual * 0.15
novo_salario = salario_atual + aumento
#saida
print(f'Salário original: R$ {salario_atual:.2f}\nValor do reajuste: R$ {aumento:.2f}\nNovo salário do funcionário já reajustado: R$ {novo_salario:.2f}')