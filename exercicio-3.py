import os
# Enunciado: Você foi contratado para desenvolver um sistema de Venda de uma Empresa Y que vende toras de arvore para outras empresas que vendem madeira. Você ficou com a parte de desenvolver a interface com o cliente. 

# A Empresa Y opera as vendas da seguinte maneira: 
# Tora de Pinho (PIN), o valor do metro cúbico (m³) é de cento e cinquenta reais e quarenta centavos; 
# Tora de Peroba (PER), o valor do metro cúbico (m³) é de cento e setenta reais e vinte centavos; 
# Tora de Mogno (MOG), o valor do metro cúbico (m³) é de cento e noventa reais e noventa centavos; 
# Tora de Ipê (IPE), o valor do metro cúbico (m³) é de duzentos e dez reais e dez centavos;  
# Tora de Imbuia (IMB), o valor do metro cúbico (m³) é de duzentos e vinte reais e setenta centavos; 

# Se a quantidade (em m³) de toras for menor que 100 não há desconto na venda (0/100); 
# Se a quantidade (em m³) de toras for igual ou maior que 100 e menor que 500, o desconto será de 4% (4/100); 
# Se a quantidade (em m³) de toras for igual ou maior que 500 e menor que 1000, o desconto será de 9% (9/100); 
# Se a quantidade (em m³) de toras for igual ou maior que 1000 e menor ou igual que 2000, o desconto será de 16% (16/100); 
# Se a quantidade (em m³) de toras for maior que 2000, não é aceito pedidos com essa quantidade de toras; 




# Para o adicional de transporte rodoviário (1) é cobrado um valor extra de 1000 reais; 
# Para o adicional de transporte ferroviário (2) é cobrado um valor extra de 2000 reais; 
# Para o adicional de transporte hidroviário (3) é cobrado um valor extra de 2500 reais; 

# O valor final da conta é calculado da seguinte maneira: 
# total = ((tipoMadeira * qtdToras)*(1-desconto)) + transporte 

# Elabore um programa em Python que:  
# 1 - Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).  
# 2 - Por exemplo: print(“Bem-vindos a Madeireira do Lenhador Bruno Kostiuk”)  [EXIGÊNCIA DE CÓDIGO 1 de 7]; 
# 3 - Deve-se implementar a função escolha_tipo() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 2 de 7]; 
      # Pergunta o tipo de madeira desejado; 
      # Retorna o VALOR do tipo de madeira com base na escolha do usuário (use return); 
      # Repete a pergunta do item B.a se digitar uma opção diferente de: PIN/PER/MOG/IPE/IMB; 
# 4 - Deve-se implementar a função qtd_toras() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 3 de 7]; 
      # Pergunta a quantidade de toras; 
      # Retorna (use return) a quantidade de toras E o valor do desconto (os dois valores) seguindo a regra do enunciado; 
      # Repete a pergunta do item C.a se digitar um valor acima de 2000 ou valor não numérico (use try/except para não numérico) 
# 5 - Deve-se implementar a função transporte() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 4 de 7]; 
      # Pergunta pelo serviço adicional de transporte; 
      # Retorna (use return) o valor de apenas uma das opções de transporte; 
      # Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/3; 
# 6 - Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função, conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5 de 7]; 
# 7 - Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7]; 
# 8 - Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de 7]; 
# 9 - Deve-se apresentar na saída de console uma mensagem com o seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4]; 
# 10 - Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de tipo de madeira [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; 
# 11 - Deve-se apresentar na saída de console um pedido no qual o usuário digitou um valor que ultrapasse a quantidade máxima de toras aceitas (2000) [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4]; 
# 12 - Deve-se apresentar na saída de console um pedido com opção de tipo de madeira, quantidade de toras e transporte válidos [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4]; 

# mostra os tipos de madeira disponiveis
def mostrar_tipos_madeira():
  print('Entre com o tipo de madeira desejado:\n')
  print('PIN - Tora de Pinho')
  print('PER - Tora de Peroba')
  print('MOG - Tora de Mogno')
  print('IPE - Tora de Ipê')
  print('IMB - Tora de Imbuia\n')

def valor_da_madeira(tipo_madeira, metros_cubicos):
  if tipo_madeira == 'pin':
    return metros_cubicos * 150.40 - ((metros_cubicos * 150.40) * desconto(metros_cubicos))
  elif tipo_madeira == 'per':
    return metros_cubicos * 170.20 - ((metros_cubicos * 170.20) * desconto(metros_cubicos))
  elif tipo_madeira == 'mog':
    return metros_cubicos * 190.90 - ((metros_cubicos * 190.90) * desconto(metros_cubicos))
  elif tipo_madeira == 'ipe':
    return metros_cubicos * 210.10 - ((metros_cubicos * 210.10) * desconto(metros_cubicos))
  elif tipo_madeira == 'imb':
    return metros_cubicos * 220.70 - ((metros_cubicos * 220.70 ) * desconto(metros_cubicos))

# retorna o desconto com base nos metros pedidos
def desconto(metros_cubicos):
  if metros_cubicos < 100:
    return 0
  if 500 > metros_cubicos >= 100:
    return 4/100
  if 1000 > metros_cubicos >= 500:
    return 9/100
  if 2000 <= metros_cubicos >= 1000:
    return 16/100

# retorna o tipo de madeira pedido
def escolha_tipo():
  while True:
    tipo_madeira = input('>> ').lower()
    if tipo_madeira == 'pin' or tipo_madeira == 'per' or tipo_madeira == 'mog' or tipo_madeira == 'ipe' or tipo_madeira == 'imb':
      return tipo_madeira
    else:
      print('Escolha inválida, entre com o modelo novamente')
      continue

# retorna a quantidade de toras pedido
def qtd_toras():
  while True:
    try:
      qtd_madeira = int(input('\nEntre com a quantidade de toras (m³): '))
    except:
      print('Valor de entrada é inválido, por favor, entre com a quantidade novamente.\n')
      continue
    if 0 < qtd_madeira <= 2000:
      return qtd_madeira, desconto(qtd_madeira)
    else:
      print('Não aceitamos pedidos com essa quantidade de toras.')
      print('Por favor, faça um pedido abaixo de 2000m³ de toras.\n')
      continue

# retorna o valor referente ao tipo de transporte selecionado
def transporte():
  global tipo_transporte
  print('Escolha o tipo de Transporte:')
  print('1 - Transporte Rodoviário - R$ 1000.00')
  print('2 - Transporte Ferroviário - R$ 2000.00')
  print('3 - Transporte Hidroviário - R$ 2500.00')
  while True:
    try:
      tipo_transporte = int(input('>> '))
      if tipo_transporte == 1:
        return 1000
      elif tipo_transporte == 2:
        return 2000
      elif tipo_transporte == 3:
        return 2500
      else:
         print('O valor não é aceito, escolha entre 1, 2 e 3')
      continue
    except: 
      print('O valor não é aceito, escolha entre 1, 2 e 3')
      continue

# o nome da tora para mandar a mensagem para o cliente
def nome_da_tora_extenso(tipo_madeira):
  if tipo_madeira == 'pin':
    return 'Pinho'
  elif tipo_madeira == 'per':
    return 'Peroba'
  elif tipo_madeira == 'mog':
    return 'Mogno'
  elif tipo_madeira == 'ipe':
    return 'Ipê'
  elif tipo_madeira == 'imb':
    return 'Imbuia'

# função principal do código
def main():
  os.system('cls')
  print('Bem vindo a Madeireira do Lohran Fellipe Mendes de Souza\n')
  mostrar_tipos_madeira()
  tipo_madeira = escolha_tipo()
  qtd_e_desconto_do_pedido = qtd_toras()
  valor_do_transporte = transporte()
  print(f'\nPedido: {qtd_e_desconto_do_pedido[0]}m³ de toras de {nome_da_tora_extenso(tipo_madeira)}')
  print(f'Total R$ {(valor_da_madeira(tipo_madeira, qtd_e_desconto_do_pedido[0]) + valor_do_transporte):.2f}\n')

main()
