def adicionar_tarefas(tarefas, nome_tarefa):
  # tarefa: nome da tarefa
  # completado: indica se essa tarefa já foi completada ou não
  
  tarefa = {"tarefa": nome_tarefa, "completada": False }
  
  tarefas.append(tarefa)
  print(f"\nTarefa {nome_tarefa} foi adicionada com sucesso!")  
  return

def ver_tarefas(tarefas):
  print("\nLista de tarefas")
  
  for indice, tarefa in enumerate(tarefas):
    status = "✓" if tarefa["completada"] else " "
    print(f"{indice} - [{status}] {tarefa["tarefa"]}")
  
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
  elif escolha == "6":
    break
  
print("\nPrograma finalizado")