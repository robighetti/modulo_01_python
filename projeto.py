def adicionar_tarefas(tarefas, nome_tarefa):
  # tarefa: nome da tarefa
  # completado: indica se essa tarefa já foi completada ou não
  
  tarefa = {"tarefa": nome_tarefa, "completada": False }
  
  tarefas.append(tarefa)
  print(f"\nTarefa {nome_tarefa} foi adicionada com sucesso!")  
  return

# funcao de ver as tarefas cadastradas
def ver_tarefas(tarefas):
  print("\nLista de tarefas")
  
  for indice, tarefa in enumerate(tarefas, start=1):
    status = "✓" if tarefa["completada"] else " "
    print(f"{indice} [{status}] {tarefa["tarefa"]}")
  
  return

# funcao de atualizaçao
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
  #verifica se a opção digitada é válida
  indice_tarefa_ajustado = int(indice_tarefa) - 1 
  
  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
    tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa  
    print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
  else:
    print(f"Opção inválida, escolha uma nova opção válida")      
  return

def completar_tarefas(tarefas, indice_tarefa):
  indice_tarefa_completado = int(indice_tarefa) - 1
  tarefas[indice_tarefa_completado]["completada"] = True
  
  print(f"Tarefa {indice_tarefa} completada com sucesso!")
  return

tarefas = []
while True:
  print("\nMenu do Gerenciador de Lista de tarefas:")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar Tarefas")
  print("4. Completar Tarefas")
  print("5. Deletar tarefas completadas")
  print("6. Sair")
  
  escolha = input("\nDigite a sua escolha: ")
  
  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa: ")
    adicionar_tarefas(tarefas, nome_tarefa)
  elif escolha == "2":    
    ver_tarefas(tarefas)
  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o numero da tareafa que deseja atualizar: ")
    novo_nome = input("Digite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas=tarefas,indice_tarefa=indice_tarefa, novo_nome_tarefa=novo_nome)
  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o numero da tareafa que deseja atualizar: ")
    completar_tarefas(tarefas=tarefas, indice_tarefa=indice_tarefa)
  elif escolha == "6":
    break
  
print("\nPrograma finalizado")