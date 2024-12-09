import os
# Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma Pizzaria que vende sabores de Pizzas Doces e Pizzas Salgadas. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto. 
# A Loja possui seguinte relação: 
# Tamanho P: Pizza Salgada (PS) custa 30 reais e a Pizza Doce (PD) custa 34 reais; 
# Tamanho M: Pizza Salgada (PS) custa 45 reais e a Pizza Doce (PD) custa 48 reais; 
# Tamanho G: Pizza Salgada (PS) custa 60 reais e a Pizza Doce (PD) custa 66 reais; 

# Elabore um programa em Python que:  

# 1 - Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).  
# 2 - Por exemplo: print(“Bem-vindos a Pizzaria do Bruno Kostiuk”)  
# 3 - Além do seu nome completo, deve-se implementar um print com um Menu para o cliente. [EXIGÊNCIA DE CÓDIGO 1 de 8]; 
# 4 - Deve-se implementar o input do sabor (PS/PD) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de PS e PD [EXIGÊNCIA DE CÓDIGO 2 de 8]; 
# 5 - Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8]; 
# 6 - Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8]; 
# 7 - Deve-se implementar um acumulador para somar os valores dos pedidos (valor total do pedido) [EXIGÊNCIA DE CÓDIGO 5 de 8]; 
# 8 - Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8]; 
# 9 - Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8]; 
# 10 - Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8]; 

# 11 - Deve-se apresentar na saída de console uma mensagem com o seu nome completo e o menu para o cliente conhecer as opções  [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4]; 
# 12 - Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];  
# 13 - Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4]; 
# 14 - Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];   
 

valor = 0
pizzas = {'pizza_salgada': {'P': 0, 'M': 0, 'G': 0}, 'pizza_doce': {'P': 0, 'M': 0, 'G': 0}}

# Informa que o input é inválido
def invalido(valor): 
  print(f'{valor} inválido. Tente novamente\n')

# Atualiza a quantidade de pizzas adicionadas
def atualiza_valores(valor_pizza, tipo_pizza, tamanho_pizza): 
  global pizzas
  global valor
  valor += valor_pizza
  pizzas[tipo_pizza][tamanho_pizza] += 1
  if tipo_pizza == 'pizza_salgada':
    print(f'Você pediu uma pizza salgada no tamanho {tamanho_pizza}: R${valor_pizza}\n')
  elif tipo_pizza == 'pizza_doce':
    print(f'Você pediu uma pizza doce no tamanho {tamanho_pizza}: R${valor_pizza}\n')
  
# Exibe o cardápio
def exibir_cardapio():  
  print(' Bem vindos a pizzaria do Lohran Fellipe Mendes de Souza '.center(80, '-'))
  print(' Cardápio '.center(80,'-'))
  print('-' * 80)
  print('|  Tamanho  |  Pizza Salgada(PS)  |  Pizza Doce(PD)  |'.center(80, '-'))
  print('|     P     |      R$ 30.00       |     R$ 34.00     |'.center(80, '-'))
  print('|     M     |      R$ 45.00       |     R$ 48.00     |'.center(80, '-'))
  print('|     G     |      R$ 60.00       |     R$ 66.00     |'.center(80, '-'))
  print('-' * 80 + '\n')
  
# Recebe os pedidos
def receber_entradas():  
  global valor
  global pizzas
  while True:
    sabor_desejado = input('\nEntre com o sabor desejado (PS/PD): ').strip().lower()
    if sabor_desejado == 'ps':
      while True:
        tamanho_desejado = input('Entre com o tamanho desejado (P/M/G): ').strip().lower()
        if tamanho_desejado == 'p':
          atualiza_valores(30,'pizza_salgada','P')
          break
        elif tamanho_desejado == 'm':
          atualiza_valores(45,'pizza_salgada','M')
          break
        elif tamanho_desejado == 'g':
          atualiza_valores(60,'pizza_salgada','G')
          break
        elif tamanho_desejado == 'sair' or tamanho_desejado == 'exit':
          return
        else:
          invalido('Tamanho')
          continue
    elif sabor_desejado == 'pd':
      while True:
        tamanho_desejado = input('Entre com o tamanho desejado (P/M/G): ').strip().lower()
        if tamanho_desejado == 'p':
          atualiza_valores(34,'pizza_doce','P')
          break
        elif tamanho_desejado == 'm':
          atualiza_valores(48,'pizza_doce','M')
          break
        elif tamanho_desejado == 'g':
          atualiza_valores(66,'pizza_doce','G')
          break
        elif tamanho_desejado == 'sair' or tamanho_desejado == 'exit':
          return
        else:
          invalido('Tamanho')
          continue
    elif sabor_desejado == 'sair' or sabor_desejado == 'exit':
      return  
    else:
      invalido('Sabor')
      continue 
    adicionar_mais()
    break
  
# Pergunta se quer adicionar mais pizzas
def adicionar_mais():  
  adicionar_pizza = input('Deseja mais alguma coisa? ').strip().lower()
  if adicionar_pizza == 'sim' or adicionar_pizza == 's':
    receber_entradas()
  elif adicionar_pizza == 'nao' or adicionar_pizza == 'não' or adicionar_pizza == 'n':
    valor_total()
  else:
    print('Responda com sim ou não')
    adicionar_mais()
    
# Exibe o valor total a ser pago
def valor_total():  
  global valor
  global pizzas 
  print(f'\nO valor total a ser pago: R${valor:.2f}\n')

# Limpa o terminal e executa o código    
def exercicio_2(): 
  os.system('cls')
  exibir_cardapio()
  receber_entradas()

exercicio_2()