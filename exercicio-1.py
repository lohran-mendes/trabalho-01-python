import os

def encerrar():
  print('o valor inserido não é válido.\n')
  print('Encerrando programa...\n')

def exercicio_1():
  os.system('cls')
  print('Esse sistema foi criado por Lohran Fellipe Mendes de Souza')
  
  # tratamento de entrada dos dados
  try: 
    valor_base = float(input('Informe aqui o valor base do plano: R$ ').strip())
  except:
    encerrar()
    return 
  try:
    idade = int(input('Digite a idade do cliente: ').strip())
  except:
    encerrar()  
    return 
  porcentagem = 0

  # lógica da porcentagem de desconto oferecido ao cliente
  if type(idade) == int:
    if  0 <= idade < 19:
      porcentagem = 100 / 100
    elif  19 <= idade < 29:
      porcentagem = 150 / 100
    elif  29 <= idade < 39:
      porcentagem = 225 / 100
    elif  39 <= idade < 49:
      porcentagem = 240 / 100
    elif  49 <= idade < 59:
      porcentagem = 350 / 100
    elif  59 <= idade:
      porcentagem = 600 / 100
    else:
      encerrar()
      return 

  valor_mensal_do_plano = valor_base * porcentagem
  print(f'O valor mensal do plano será de R${valor_mensal_do_plano:.2f}\n')

exercicio_1()