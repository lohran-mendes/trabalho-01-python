import os

def exercicio_1():
  os.system('cls')
  valor_base = int(input('Informe aqui o valor base: '))
  idade = int(input('Qual a sua idade? '))
  porcentagem = 1
  print(f'Você tem {idade} anos')

  if type(idade) == int:
    if  0 <= idade < 19:
      porcentagem = 1
      print('primeira condição')
    if  19 <= idade < 29:
      porcentagem = 1.5
      print('segunda condição')
    elif  29 <= idade < 39:
      porcentagem = 2.25
      print('terceira condição')
    elif  39 <= idade < 49:
      porcentagem = 2.40
      print('quarta condição')
    elif  49 <= idade < 59:
      porcentagem = 3.50
      print('quinta condição')
    elif  59 <= idade:
      porcentagem = 6.00
      print('sexta condição')

  valor_mensal_do_plano = valor_base * porcentagem
  print(f'O valor mensal do plano será de {valor_mensal_do_plano} reais')

exercicio_1()