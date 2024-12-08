import os
import copy
# Enunciado: Você e sua equipe de programadores foram contratados por uma pequena empresa para desenvolver um software de gerenciamento de Contatos Comerciais. Este software deve ter o seguinte menu e opções: 

# 1 - Cadastrar Contato 
# 2 - Consultar Contato 
    # Consultar Todos  
    # Consultar por Id 
    # Consultar por Atividade 
    # Retornar ao menu 
# 3 - Remover Contato 
# 4 - Encerrar Programa 

# Elabore um programa em Python que:  
# 1 - Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). Por exemplo: print(“Bem vindos a lista de contatos do Bruno Kostiuk”)  [EXIGÊNCIA DE CÓDIGO 1 de 8]; 
# 2 - Deve-se implementar uma lista com o nome de lista_contatos e a variável id_global com valor inicial igual ao número de seu RU [EXIGÊNCIA DE CÓDIGO 2 de 8]; 
# 3 - Deve-se implementar uma função chamada cadastrar_contato(id) que recebe apenas id como parâmetro e que: [EXIGÊNCIA DE CÓDIGO 3 de 8]; 
    # Pergunta nome, atividade, telefone do contato; 
    # Armazena o id (este é fornecido via parâmetro da função), nome, atividade, telefone dentro de um dicionário; 
    # Copiar o dicionário para dentro da lista_contatos (utilizar o copy); 
# 4 - Deve-se implementar uma função chamada consultar_contatos() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 4 de 8]; 
    # Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu): 
        # Se Consultar Todos, apresentar todos os contatos com todos os seus dados cadastrados; 
        # Se Consultar por Id, solicitar ao usuário que informe um id, e apresentar o contato específico (apenas 1) com todos os seus dados cadastrados; 
        # Se Consultar por Atividade, solicitar ao usuário que informe a atividade, e apresentar o(s) contato(s) que exercem aquela atividade com todos os seus dados cadastrados; 
        # Se Retornar ao menu, deve-se retornar ao menu principal (return); 
        # Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta D.a. 
        # Enquanto o usuário não escolher a opção 4, o menu consultar contatos deve se repetir. 
# 5 - Deve-se implementar uma função chamada remover_contato() em que: [EXIGÊNCIA DE CÓDIGO 5 de 8]; 
    # Deve-se pergunta pelo id do contato a ser removido; 
    # Remover o contato da lista_contatos; 
    # Se o id fornecido não for de um contato da lista, printar “Id inválido” e repetir a pergunta E.a. 
# 6 - Deve-se implementar uma estrutura de menu no código principal (main), ou seja, não pode estar dentro de função, em que: [EXIGÊNCIA DE CÓDIGO 6 de 8]; 
    # Deve-se pergunta qual opção deseja (1. Cadastrar Contato / 2. Consultar Contato / 3. Remover Contato / 4. Encerrar Programa): 
    # Se Cadastrar Contato, incrementar em um id_ global e em seguida, chamar a função cadastrar_contato (id_ global); 
    # Se Consultar Contato, chamar função consultar_contato (); 
    # Se Remover Contato, chamar função remover_ contato (); 
    # Se Encerrar Programa, sair do menu (e com isso acabar a execução do código); 
    # Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta F.a. 
    # Enquanto o usuário não escolher a opção 4, o menu deve se repetir. 
# 7 - Deve-se implementar uma lista de dicionários (uma lista contento dicionários dentro) [EXIGÊNCIA DE CÓDIGO 7 de 8]; 
# 8 - Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8]; 

# 9 - Deve-se apresentar na saída de console um cadastro do seu contato da seguinte forma: para nome informe seu nome completo (não usar apelidos ou abreviações), para atividade informar como estudante, e para telefone informe sua RU. [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6]; 
# 10 - Deve-se apresentar na saída de console um cadastro de mais 2 contatos com mesmo tipo de atividade (por exemplo: marceneiro, padeiro, pintor, pedreiro) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6]; 
# 11 - Deve-se apresentar na saída de console uma consulta de todos os contatos [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6]; 
# 12 - Deve-se apresentar na saída de console uma consulta por código (id) de um dos contados [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6]; 
# 13 - Deve-se apresentar na saída de console uma consulta por atividade em que 2 contatos exerçam a mesma atividade [EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6]; 
# 14 - Deve-se apresentar na saída de console uma remoção de um dos contatos e em seguida de uma consulta de todos os contatos, provando que o contato foi removido [EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6]; 
lista_contatos = [
  {'id_global':'5031145','nome': 'nome', 'atividade': 'atividade', 'telefone':'telefone'}, 
  {'id_global':'id','nome': 'nome', 'atividade': 'atividade', 'telefone':'telefone'}, 
  {'id_global':'id2','nome': 'nome2', 'atividade': 'atividade', 'telefone':'telefone2'}
  ]

def cadastrar_contato(id):
  global lista_contatos
  nome = input('Por favor, entre com o nome do Contato: ')
  atividade = input('Por favor, entre com a atividade do Contato: ')
  telefone = input('Por favor, entre com o telefone do Contato: ')
  contato = {'id_global':id,'nome': nome, 'atividade': atividade, 'telefone':telefone}

  print('\n')
  lista_contatos.append(copy.copy(contato))
  print(lista_contatos)
  
def consultar_contatos():
    print('1 - Consultar Todos os Contatos')
    print('2 - Consultar Contato por Id')
    print('3 - Consultar Contato(s) por Atividade')
    print('4 - Retornar ao menu')

    while True:
      try:
        opcao_escolhida =  int(input('>> '))
        if opcao_escolhida == 1:
          print('Todos os contatos:', lista_contatos)
          break
        elif opcao_escolhida == 2:
          id = input('Qual o id do contato a ser consultado?: ')
          for contato in lista_contatos:
            if contato['id_global'] == id:
              return print(contato)
          return print('Não há contatos com esse id')
        elif opcao_escolhida == 3:
          contatos_filtrados = []
          atividade = input('Qual a atividade para aplicar o filtro?: ')
          for contato in lista_contatos:
            if contato['atividade'] == atividade:
              contatos_filtrados.append(contato)
          if len(contatos_filtrados) == 0:
            return print('Não há contatos com essa atividade')
          else:
            print(f'Filtro de contatos pela atividade {atividade}: \n')
            for i in contatos_filtrados:
              print(i)
          return
        elif opcao_escolhida == 4:
          print('\nRetornando ao menu principal...\n')
          return mostrar_menu_principal()
        else:
          print('\nOpção inválida, escolha uma opção de 1 a 4')
          continue        
      except:
        print('\nOpção inválida, escolha uma opção de 1 a 4')
        continue

def mostrar_menu_principal():
  print('-' * 70)
  print(' MENU PRINCIPAL '.center(70, '-'))
  print('Escolha a opção desejada:')
  print('1 - Cadastrar Contato')
  print('2 - Consultar Contato(s)')
  print('3 - Remover Contato')
  print('4 - Sair')

  while True:
    try:
      opcao_escolhida =  int(input('>> '))
      if opcao_escolhida == 1:
        mostrar_menu_cadastrar_contato()
        break
      elif opcao_escolhida == 2:
        mostrar_menu_consultar_contato()
        break
      elif opcao_escolhida == 3:
        mostrar_menu_remover_contato()
        break
      elif opcao_escolhida == 4:
        print('\nEncerrando aplicação...\n')
        break
      else:
        print('\nOpção inválida, escolha uma opção de 1 a 4')
        continue        
    except:
      print('\nOpção inválida, escolha uma opção de 1 a 4')
      continue

def mostrar_menu_cadastrar_contato():
  print('\n' + '-' * 70)
  print(' MENU CADASTRAR CONTATO '.center(70, '-'))
  id = input('Id do Contato: ')
  cadastrar_contato(id)

def mostrar_menu_consultar_contato():
  print('\n' + '-' * 70)
  print(' MENU CONSULTAR CONTATOS '.center(70, '-'))
  consultar_contatos()

def mostrar_menu_remover_contato():
  print('-' * 70)
  print(' MENU REMOVER CONTATO '.center(70, '-'))
  print('Digite o ID do contato a ser removido:')
  
def main():
  os.system('cls')
  print(' Bem vindo a Lista de Contatos do Lohran Fellipe Mendes de Souza '.center(70, '-'))
  mostrar_menu_principal()

main()