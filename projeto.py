import time
senhacadstrada = ['123456', '0000']

def senhaverificada(login, listassenha):
    if login in listassenha:
        print("Logado com sucesso!")
        return True  # Se a senha for encontrada, retorna True e encerra a função
    else:
        print("Senha incorreta. Tente novamente.")
        return False  # Se exceder o limite de tentativas, retorna False


def verifica_cpf(cpf):
    tentativas = 0
    while tentativas <= 5:
        cpf_str = str(cpf)  # Converte o CPF para uma string
        # Remove caracteres não numéricos
        cpf_str = ''.join(filter(str.isdigit, cpf_str))

        # Verifica se o CPF possui 11 dígitos
        if len(cpf_str) != 11:
            print("CPF deve conter 11 dígitos.")
        else:
            # Calcula o primeiro dígito verificador
            soma = sum(int(cpf_str[i]) * (10 - i) for i in range(9))
            resto = (soma * 10) % 11
            if resto == 10:
                resto = 0
            if resto != int(cpf_str[9]):
                print("CPF inválido.")
            else:
                # Calcula o segundo dígito verificador
                soma = sum(int(cpf_str[i]) * (11 - i) for i in range(10))
                resto = (soma * 10) % 11
                if resto == 10:
                    resto = 0
                if resto != int(cpf_str[10]):
                    print("CPF inválido.")
                else:
                    # CPF válido
                    return True
        tentativas += 1
        cpf = input("Digite o CPF novamente (somente números): ")

    # Após 5 tentativas sem sucesso, retorna False
    return False


def altera_exclui(lista, pos, acao):
    if not lista:  # Verifica se a lista está vazia
        print("A lista de oficinas está vazia. Por favor, cadastre uma oficina primeiro.")
        return  # Retorna imediatamente, sem fazer mais nada na função
    
    ind = pos * 5  # Calcula o índice baseado na posição da oficina
    if acao == 2:
        for _ in range(5):
            if ind < len(lista):
                lista.pop(ind)
       
        print(".....................................", end='', flush=True)
        time.sleep(2)
        print("", end='', flush=True)
        print("apagado")

    elif acao == 1:
        altera_oficina(lista, ind)
    else:
        print("Fazendo nada")


def submenu():
    print("1 - Altera\n2 - Exclui\n3 - Sair")
    opcao = int(input("Selecione: "))
    return opcao


def altera_oficina(lista,ind):
    mod = input(f"Razao social ({lista[ind]}): ")
    if len(mod) > 0:
        lista[ind] = mod
 
    mar = input(f"CNPJ ({lista[ind+1]}): ")
    if len(mar) > 0:
        lista[ind+1] = mar
 
   
    ver = input(f"Logadouro ({lista[ind+2]}): ")
    if len(ver) > 0:
        lista[ind+2] = ver
 
   
    ano = input(f"Numero ({lista[ind+3]}): ")
    if len(ano) > 0:
        lista[ind+3] = int(ano)
   
   
    pl = input(f"Cep ({lista[ind+4]}): ")
    if len(pl) > 0:
        lista[ind+4] = pl
 


oficinascadastradas=[]
def submenu_oficinas():
    print("1 - Altera Dados\n2 - Exclui Oficinas\n3 - Sair")
    opcao = int(input("Selecione: "))
    return opcao


def lista_oficinas(lista):
    i=0
    j=0
    while i < len(lista):
 
        print(f"{j}) {lista[1]} {lista[i + 4]}")
        i = i + 5
        j = j + 1
 


def menu():
    print("\nCadastro de oficinas\n")
    print("1 - Inclui Oficinas \n2 - Lista de oficinas cadastradas\n3 - Sair")
    opcao = int(input("Selecione: "))
    return opcao

def inclui_oficinas(oficinascads):
    oficinascadastradas.append(input("Razao social: "))
    oficinascadastradas.append(input("Cnpj: "))
    oficinascadastradas.append(input("Logadouro: "))
    oficinascadastradas.append(int(input("Numero: ")))
    oficinascadastradas.append(input("Cep: "))


executando = True

# Loop principal
while executando:
    print("############################################################################################################")
    print("##                                     Bem-vindo ao AutoCarePlus                                            ##")
    print("##                        O lugar onde o seu carro recebe o cuidado que merece!                              ##")
    print("############################################################################################################")

    print("\nPor favor, selecione uma opção:")
    print("1 - Agendar revisão")
    print("2 - Realizar AutoDiagnóstico")
    print("3 - Fale Conosco")
    print("4 - Cadastro de Oficinas Parceiras")
    print("5 - Sair")

    falharificada = 0
    anoverificado = 0
    ano = 0
    kmrodado = 0
    ano = 0
    opcao_agendamento = 0
    multiplicador = 0
    marca = 0
    horario = 0
    modelo = 0
    marcaverificada = 0
    verificadados = 0
    bateria = 0
    
    opcao_desejada = input("Digite a Opcao desejada: ")
    
    
    if opcao_desejada.isdigit():
        opcao_desejada2 = int(opcao_desejada)
    else:
        print("Por favor, digite apenas números.")
        continue

    if opcao_desejada2 == 1:
        CPF = int(input("Digite o CPF sem o traco: "))
        cpf_valido = verifica_cpf(CPF)
        
        if cpf_valido:
            print("CPF válido.")
            print("Qual Marca do veiculo")
            print("1 - Volkswagem\n2 - Chevrolet")
            print("3 - Ford\n4 - FIAT")

            while True:
                marca = input("Digite a marca: ")
                if marca.isdigit():
                    marcaverificada = int(marca)
                    break
                else:
                    print("Por favor, digite apenas números.")

            if marcaverificada in [1, 2, 3]:
                modelo = input("Digite o modelo: ")

                while True:
                    ano = input("Digite o ano: ")
                    if ano.isdigit():
                        anoverificado = int(ano)
                        break
                    else:
                        print("Por favor, digite apenas números.")

                    kmrodado = float(input("Digite a km: "))
                if kmrodado >=1000 and kmrodado <20000:
                    print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.1)
                elif kmrodado >=20000 and kmrodado <30000:
                    print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.19)
                elif kmrodado >=30000 and kmrodado <40000:
                    print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.22)
                elif kmrodado >=40000 and kmrodado <50000:
                    print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.02)
                elif kmrodado >=50000 and kmrodado <60000:
                    print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.01)
                elif kmrodado >=60000 and kmrodado <70000:
                    print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.2)
                elif kmrodado >=70000 and kmrodado <80000:
                    print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.2)
                elif kmrodado >=80000 and kmrodado <90000:
                    print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.2)
                elif kmrodado >=90000 and kmrodado <100000:
                    print("Valor da revisao para o veiculo",modelo,ano,"é",kmrodado*0.2)
                elif kmrodado >= 100000:
                    print("entrar em contato via telefone")

                print("Deseja agendar servico:")
                print("1 -sim  \n2- - nao")
                opcao_agendamento = int(input("Digite a opcao:"))
                if opcao_agendamento == 1:
                    data_marcada = str(input("digite a data desejada para atendimento: "))
                    print("Escolha um horário disponível para a data selecionada:")
                    print("1 - 8:00")
                    print("2 - 11:45")
                    print("3 - 9:00")
                    print("4 - 12:30")

                    horario = int(input("Selecione horario"))
                    while horario <1 or horario>4:
                        print("opcao invalidada")            
                        horario = int(input("Selecione horario")) 
                    print("Servico agendado para o CPF: ",CPF,"para veiculo",modelo,"\npara data: ",data_marcada,"e o horario selecionado")
                    time.sleep(3)
                else:
                    print("Volte sempre!")
                    time.sleep(3)
            else:
                print("Marca inválida ou limite de tentativas excedido.")
        else:        
            print("CPF inválido ou limite de tentativas excedido.")

            
        
              

    elif opcao_desejada2 == 2:
        placa = input("Digite A PLACA: ")

        print("Por favor, selecione a marca do veículo:")
        print("1 - Volkswagen")
        print("2 - Chevrolet")
        print("3 - Ford")
        print("4 - Fiat")


        while True:
            marca = input("Digite a marca: ")
            if marca.isdigit():
                marcaverificada = int(marca)
                break
            else:
                print("Por favor, digite apenas números.")

        if marcaverificada in [1, 2, 3]:
            modelo = input("Digite o modelo: ")

            while True:
                ano = input("Digite o ano: ")
                if ano.isdigit():
                    anoverificado = int(ano)
                    break
                else:
                    print("Por favor, digite apenas números.")

            print("################### Autodiagnóstico ##################################")
            print("##                Bem-vindo ao sistema de Autodiagnóstico!            ##")
            print("##            Por favor, selecione a origem da falha:                 ##")
            print("##                                                                    ##")
            print("##  1 - Bateria                                                       ##")
            print("##  2 - Mecânico                                                      ##")
            print("##  3 - Pane Elétrica                                                 ##")
            print("##  4 - Sair                                                          ##")
            print("#######################################################################")
            while True:
                falha = input("Selecione a origem da falha: ")
                if falha.isdigit():
                    falharificada = int(falha)
                    break
                else:
                    print("Por favor, digite apenas números.")

            if falharificada == 1:
                print("Por favor, selecione a cor indicada no indicador de nível de bateria:")
                print("1 - Verde")
                print("2 - Preto")
                print("3 - Branco")
                print("4 - Não sei")

                while True:
                    bateria = input("Selecione a cor: ")
                    if bateria.isdigit():
                        bateriaverificada = int(bateria)
                        break
                    else:
                        print("Por favor, digite apenas números.")

                if bateriaverificada == 1:
                    print("A bateria está carregada, mas recomendamos agendar uma revisão.")
                elif bateriaverificada == 2:
                    print("Será necessário a troca da bateria devido ter chego ao fim de sua vida útil")
                else:
                    print("Será necessário carga na bateria")

    elif opcao_desejada2 == 3:
        nome = input("Nome completo: ")
        email = input("Informe o email: ")
        telefone = input("Forneça o número de telefone para contato: ")
        dados_veiculo = input("Informe o RENAVAM do veículo: ")

        marca_veiculo = input("Informe a marca do veículo: ")
        modelo_veiculo = input("Informe o modelo do veículo: ")
        ano_veiculo = input("Informe o ano do veículo: ")
        placa_veiculo = input("Informe a placa do veículo: ")
        

        pergunta = input("Pergunta ou dúvidas: ")
        print("Mais tarde entraremos em contato.")
        print("Agradecemos pela sua paciência.")

    elif opcao_desejada2 == 5:
        print("Saindo...")
        break

    
    Senha=0
    
      
    
    if opcao_desejada2 == 4:
        Senha = input("Por favor, insira a senha do usuário do sistema.: ")
        logado = senhaverificada(Senha, senhacadstrada)

        if logado:
            print("Senha correta. Acesso permitido.")
            while True: 
                selecao = menu()  # Obtém a seleção do usuário

                if selecao == 1:
                    inclui_oficinas(oficinascadastradas)
                    print("Oficina cadastrada com sucesso")
                    print(oficinascadastradas)
                    print("salvando........")

                elif selecao == 2:
                    print("Lista de oficinas")
                    lista_oficinas(oficinascadastradas)
                    pos = int(input("Selecione a oficina: "))
                    acao = submenu_oficinas()
                    altera_exclui(oficinascadastradas, pos, acao)

                elif selecao == 3:  # Se o usuário selecionar 3, sai do loop
                    print("Saindo...")
                    break
        else:
            print("Senha incorreta. Acesso negado.")
            time.sleep(3)  # Atraso antes de sair do programa

        
                
   
        
                    

                    



                        
                    





    
        time.sleep(3)


                        
                    