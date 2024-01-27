# NOME: ALEXANDREMAYCON PEREIRA DOS SANTOS DE SOUZA
# CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
# MATRICULA: 11100010563_20232_01

import os
import json

# Verica o sistema operacional utilizado e limpa a tela, o if seria para macbook e linux e o segundo para windows 
def cleanScreen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt': 
        os.system('cls')

# Função para mostrar o menu
def showMenu():
    print("-------------------""\n");
    print("¦   *BEM VINDO*   ¦""\n");
    print("-------------------""\n"),
    print("     ___|_|___       \n");
    print("    |_________|      \n");

    print("1- Estudantes \n2- Disciplinas \n3- Professores \n4- Turmas \n5- Matrículas \n6- Sair \n")
    option = input("Informe um número para a opcao desejada: ")
    return option
    

# Função para mostrar o menu de operações apenas uma vez
def actionMenu(titulo):
    print("BEM VINDO AO MENU DE " + titulo.upper() + "\n")
    print("1- Incluir "+ titulo +" \n2- Listar "+ titulo +" \n3- Atualizar "+ titulo +" \n4- Excluir "+ titulo +" \n5- Voltar ao menu principal \n ")
    action = input("Informe um número: ")
    return action


# Função para carregar os dados do arquivo JSON
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding='utf-8') as file:
            data = json.load(file)
    else:
        data = {"students": [], "disciplines": [], "teachers": [], "classes": [], "registrations": []}
    return data

# Função para salvar os dados no arquivo JSON
def save_data(data):
    with open("data.json", "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii = False)
        
# Função genérica para listar um array         
def listArray(titulo, arrayName, fields):
    cleanScreen()
    print("MOSTRAR " + titulo.upper() + "\n")
    if len(data[arrayName]) < 1:
        print(f"NÃO HÁ {titulo.upper()} CADASTRADOS (a)\n")
    else:
        for item in data[arrayName]:
            formatted_item = " - ".join([f"{field}: {item[field]}" for field in fields])
            print(formatted_item)
    print("\n")

# Função genérica adicionar um item no array  
def addNewItem(titulo, arrayName, fields):
    cleanScreen()
    print("INCLUIR " + titulo.upper() + "\n")
    arrayFields = {}
    
    # Lê o código do novo item
    try:
        cod = int(input(f"Informe o {fields[0]} do {titulo}: "))
    except ValueError:
        print("\nO codigo deve ser um número \n")
        return
    
    # Verifica se o código já existe
    for item in data[arrayName]:
        if item["codigo"] == cod:
            print(f"Já existe um {titulo} com o código {cod}. \n")
            return
    
    # Preenche os outros campos
    for i in range(1, len(fields)):
        value = input(f"Informe o {fields[i]} do {titulo}: ")
        arrayFields[fields[i]] = value

    # Adiciona o novo item aos dados
    arrayFields[fields[0]] = cod
    data[arrayName].append(arrayFields)
    print(f"{titulo} adicionado (a) com sucesso!\n")
    save_data(data)

# Função genérica para deletar um item de um array 
def deleteItem(titulo, arrayName):
    cleanScreen()
    print("EXCLUIR " + titulo.upper() + "\n")
    try:
        idItemDelete = int(input(f"Informe o código do (a) {titulo} a ser excluído: "))
    except ValueError:
            print("\nO codigo deve ser um número \n")
            return
    for newArrayOfitens in data[arrayName]:
        if newArrayOfitens["codigo"] == idItemDelete:
            data[arrayName].remove(newArrayOfitens)
            print(f"{titulo.capitalize()} excluído (a) com sucesso! \n")
            save_data(data)
            break
    else:
        print(f"{titulo.capitalize()} não encontrado (a)! \n")

# Função genérica para alterer um item no array
def updateItem(titulo, arrayName, fields):
    cleanScreen()
    print("ATUALIZAR " + titulo.upper() + "\n")
    
    try:
        idItemUpdate = int(input(f"Informe o código do (a) {titulo} a ser atualizado: "))
    except ValueError:
        print("\nO codigo deve ser um número \n")
        return
    
    for newItem in data[arrayName]:
        if newItem["codigo"] == idItemUpdate:
            # Lê o novo valor do código
            try:
                new_code = int(input(f"Informe o novo código: "))
            except ValueError:
                print("\nO código deve ser um número.\n")
                return
            
            # Verifica se o novo código já existe em outro item
            for existingItem in data[arrayName]:
                if existingItem != newItem and existingItem["codigo"] == new_code:
                    print(f"O código {new_code} já está sendo usado por outro {titulo}. \n")
                    return
            
            arrayFields = {}
            for i in range(len(fields)):
                field_name = fields[i]
                if field_name == "codigo":
                    arrayFields[field_name] = new_code
                else:
                    new_value = input(f"Informe o novo {field_name} (ou pressione Enter para manter o {field_name} atual): ")
                    if new_value:
                        arrayFields[field_name] = new_value
            
            newItem.update(arrayFields)
            
            # Salva os dados após atualizar o item
            print(f"{titulo} atualizado (a) com sucesso! \n")
            save_data(data)
            break
    else:
        print(f"{titulo} não encontrado (a)! \n")

data = load_data()

principalLoop = True

while principalLoop:
    option = showMenu()

    if option == '6':
        print("\nFinalizando operação...")
        save_data(data)  # Salva os dados no arquivo antes de sair
        principalLoop = False
        break

    cleanScreen()
    
    stay = True

    while stay:
        if option not in ['1', '2', '3', '4', '5']:
            cleanScreen()
            print("\nOpção inválida!\n")
            break

        match option:
            case '1':
                action = actionMenu("Estudante")

                match action:
                    case '1':
                        addNewItem("estudante", "students", ['codigo', 'nome', 'cpf'])

                    case '2':
                        listArray("estudantes", "students", ['codigo', 'nome', 'cpf'])

                    case '3':
                        updateItem("estudante", "students", ['codigo', 'nome', 'cpf'])

                    case '4':
                        deleteItem("estudante", "students")

                    case '5':
                        break

                    case _:
                        cleanScreen()
                        print("\nOpção Inválida!\n")
            case '2':
                action = actionMenu("Disciplina")

                match action:
                    case '1':
                        addNewItem("disciplina", "disciplines", ['codigo', 'nome'])

                    case '2':
                        listArray("disciplinas", "disciplines", ['codigo', 'nome'])

                    case '3':
                        updateItem("disciplina", "disciplines", ['codigo', 'nome'])

                    case '4':
                        deleteItem("disciplina", "disciplines")

                    case '5':
                        break

                    case _:
                        cleanScreen()
                        print("\nOpção Inválida!\n")
            case '3':
                action = actionMenu("Professor")

                match action:
                    case '1':
                        addNewItem("professor", "teachers", ['codigo', 'nome', 'cpf'])

                    case '2':
                        listArray("professores", "teachers", ['codigo', 'nome', 'cpf'])

                    case '3':
                        updateItem("professor", "teachers", ['codigo', 'nome', 'cpf'])

                    case '4':
                        deleteItem("professor", "teachers")

                    case '5':
                        break

                    case _:
                        cleanScreen()
                        print("\nOpção Inválida!\n")
            case '4':
                action = actionMenu("Turma")

                match action:
                    case '1':
                        addNewItem("turma", "classes", ['codigo', 'codigo_professor', 'codigo_diciplina'])

                    case '2':
                        listArray("turmas", "classes", ['codigo', 'codigo_professor', 'codigo_diciplina'])

                    case '3':
                        updateItem("turma", "classes", ['codigo', 'codigo_professor', 'codigo_diciplina'])

                    case '4':
                        deleteItem("turma", "classes")

                    case '5':
                        break

                    case _:
                        cleanScreen()
                        print("\nOpção Inválida!\n")
            case '5':
                action = actionMenu("Matricula")

                match action:
                    case '1':
                        addNewItem("matricula", "registrations", ['codigo', 'codigo_estudante', 'codigo_turma'])

                    case '2':
                        listArray("matriculas", "registrations", ['codigo', 'codigo_estudante', 'codigo_turma'])

                    case '3':
                        updateItem("matricula", "registrations", ['codigo', 'codigo_estudante', 'codigo_turma'])

                    case '4':
                        deleteItem("matricula", "registrations")

                    case '5':
                        break

                    case _:
                        cleanScreen()
                        print("\nOpção Inválida!\n")
