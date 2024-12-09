import os

# Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app para uma empresa X que vende Planos de Saúde. Uma das estratégias dessa empresa X é cobrar um valor diferente com base na idade do cliente, conforme a listagem abaixo: 

# Se a idade for maior ou igual que 0 e menor que 19, o valor será de 100% do valor base do plano (100 / 100); 
# Se a idade for maior ou igual que 19 e menor que 29, o valor será de 150% do valor base do plano (150 / 100); 
# Se a idade for maior ou igual que 29 e menor que 39, o valor será de 225% do valor base do plano (225 / 100); 
# Se a idade for maior ou igual que 39 e menor que 49, o valor será de 240% do valor base do plano (240 / 100); 
# Se a idade for maior ou igual que 49 e menor que 59, o valor será de 350% do valor base do plano (350 / 100); 
# Se a idade for maior ou igual que 59, o valor será de 600% do valor base do plano (600 / 100); 

# O valor mensal do plano é calculado da seguinte maneira: 
# valorMensal=valorBase∗porcentagem
# Exemplo: Se o valorBase informado for 100.00 e a idade for 45 anos (240% segundo a tabela acima) 
# valorMensal=100.00∗(240100)=R$ 240.00

# 1 - Elabore um programa em Python que: 
# 2 - Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).  
# 3 - Por exemplo: print(“Sistema desenvolvido por Bruno Kostiuk”) [EXIGÊNCIA DE CÓDIGO 1 de 6]; 
# 4 - Deve-se implementar o input do valorBase do plano e da idade do cliente [EXIGÊNCIA DE CÓDIGO 2 de 6]; 
# 5 - Deve-se implementar as regras de valores conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6]; 
# 6 - Deve-se implementar o valorMensal [EXIGÊNCIA DE CÓDIGO 4 de 6]; 
# 7 - Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];   
# 8 - Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6]; 
# 9 - Deve-se apresentar na saída de console uma mensagem com seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2]; 
# 10 - Deve-se apresentar na saída de console a utilização do sistema informando uma idade maior ou igual a 29 anos, apresentando na saída de console o valorMensal do plano [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2]; 

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