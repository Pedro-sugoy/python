esp = "\n\n"
linha = "=" * 50

while True:
    print("Cp1 de Python")
    print("\t1 Fazer um login e senha")
    print("\t2 Entrar como usuário")
    print("\t3 Encerrar")
    # print("\t4 Protegendo a senha")
    # print("\t5 Login com a senha protegida")
    # print("\t6 Encerrar")

    opcao = input("Digite uma das opções\n")
    
    match opcao:
        case "1":
            while True:
                print(esp,linha)
                print("Escolha um dos 3 métodos de de login")
                print("\a1 Emai")
                print("\a2 User-name")
                print("\a3 RG ou CPF")
                
                esc_usuario = input("Digite uma das opções:\n")

                match esc_usuario:
                    case "1":
                        print(esp,linha)
                        print("EMAIL")
                        login = input("Digite um Email:\n")
                        if "@" and ".com" or ".br" in login:
                            print("Email valida")
                        else:
                            print("Email invalido")
                        
                        print(esp,linha)

                        senha = input("Crie uma senha:\n ")
                        tamanho = len(senha) < 8  
                        minuscula = (
                            senha.islower()
                        )  
                        maiuscula = (
                            senha.isupper()
                        )  
                        soh_letras = (
                            senha.isalpha()
                        )  
                        soh_letras_e_num = (
                            senha.isalnum()
                        )  
                        eh_valida = (
                            tamanho
                            or minuscula  
                            or maiuscula  
                            or soh_letras  
                            or soh_letras_e_num  
                        )
                        if eh_valida:
                            print("Senha inválida")
                        else:
                            print("Senha válida")
                            break
                        print(esp,linha)

                    case "2":
                        print(esp,linha)
                        print("USER-NAME")
                        login = input("Digite um nome de usuario:\n").isalpha()
                        if "_" or "1" or "2" or "3" or "5" or "6" or "7" or "8" or "9" or "0" in login:
                            print("valido")
                        else:
                            print("invalido")

                        print(esp,linha)

                        senha = input("Crie uma senha:\n ")
                        tamanho = len(senha) < 8  
                        minuscula = (
                            senha.islower()
                        )  
                        maiuscula = (
                            senha.isupper()
                        )  
                        soh_letras = (
                            senha.isalpha()
                        )  
                        soh_letras_e_num = (
                            senha.isalnum()
                        )  
                        eh_valida = (
                            tamanho
                            or minuscula  
                            or maiuscula  
                            or soh_letras  
                            or soh_letras_e_num  
                        )
                        if eh_valida:
                            print("Senha inválida")
                        else:
                            print("Senha válida")
                            break
                        print(esp,linha)
                        
                    case "3":
                        print(esp,linha)
                        print("RG/CPF")
                        login = input("Digite o seu RG ou CPF (USE O FORMATO CPF: XXX.XXX.XXX-XX ou XXXXXXXXXXX/RG: XX.XXX.XXX-X ou XXXXXXXXX):\n")
                        tamanho = len(login) > 9
                        if login != tamanho:
                            print("RG ou CPF valido")
                        elif login == tamanho:
                            print("RG  ou CPF invalido")

                        print(esp,linha)

                        senha = input("Crie uma senha:\n ")
                        tamanho = len(senha) < 8  
                        minuscula = (
                            senha.islower()
                        )  
                        maiuscula = (
                            senha.isupper()
                        )  
                        soh_letras = (
                            senha.isalpha()
                        )  
                        soh_letras_e_num = (
                            senha.isalnum()
                        )  
                        eh_valida = (
                            tamanho
                            or minuscula  
                            or maiuscula  
                            or soh_letras  
                            or soh_letras_e_num  
                        )
                        if eh_valida:
                            print("Senha inválida")
                        else:
                            print("Senha válida")
                            break
                        print(esp,linha)
        case "2":
            print(esp,linha)
            print("ENTRAR COMO USUARIO")
            nome = input("Digite o seu nome:\n")
            print("Escolha uma das opções para entrar:")
            while True:
                print(esp,linha)
                print("Escolha um dos 3 métodos de de login")
                print("\a1 Emai")
                print("\a2 User-name")
                print("\a3 RG ou CPF")
                
                esc_usuario = input("Digite uma das opções:\n")

                match esc_usuario:
                    case "1":
                        print(esp,linha)
                        print("EMAIL")
                        login = input("Digite um Email:\n")
                        if "@" and ".com" or ".br" in login:
                            print("Email valida")
                        else:
                            print("Email invalido")
                        
                        print(esp,linha)

                        senha = input("Crie uma senha:\n ")
                        tamanho = len(senha) < 8  
                        minuscula = (
                            senha.islower()
                        )  
                        maiuscula = (
                            senha.isupper()
                        )  
                        soh_letras = (
                            senha.isalpha()
                        )  
                        soh_letras_e_num = (
                            senha.isalnum()
                        )  
                        eh_valida = (
                            tamanho
                            or minuscula  
                            or maiuscula  
                            or soh_letras  
                            or soh_letras_e_num  
                        )
                        if eh_valida:
                            print("Senha inválida")
                        else:
                            print("Senha válida")
                        print(esp,linha)

                    case "2":
                        print(esp,linha)
                        print("USER-NAME")
                        login = input("Digite um nome de usuario:\n").isalpha()
                        if "_" or "1" or "2" or "3" or "5" or "6" or "7" or "8" or "9" or "0" in login:
                            print("valido")
                        else:
                            print("invalido")

                        print(esp,linha)

                        senha = input("Crie uma senha:\n ")
                        tamanho = len(senha) < 8  
                        minuscula = (
                            senha.islower()
                        )  
                        maiuscula = (
                            senha.isupper()
                        )  
                        soh_letras = (
                            senha.isalpha()
                        )  
                        soh_letras_e_num = (
                            senha.isalnum()
                        )  
                        eh_valida = (
                            tamanho
                            or minuscula  
                            or maiuscula  
                            or soh_letras  
                            or soh_letras_e_num  
                        )
                        if eh_valida:
                            print("Senha inválida")
                        else:
                            print("Senha válida")
                        print(esp,linha)
                        
                    case "3":
                        print(esp,linha)
                        print("RG/CPF")
                        login = input("Digite o seu RG ou CPF (USE O FORMATO CPF: XXX.XXX.XXX-XX ou XXXXXXXXXXX/RG: XX.XXX.XXX-X ou XXXXXXXXX):\n")
                        tamanho = len(login) > 9
                        if login != tamanho:
                            print("RG ou CPF valido")
                        elif login == tamanho:
                            print("RG  ou CPF invalido")

                        print(esp,linha)

                        senha = input("Crie uma senha:\n ")
                        tamanho = len(senha) < 8  
                        minuscula = (
                            senha.islower()
                        )  
                        maiuscula = (
                            senha.isupper()
                        )  
                        soh_letras = (
                            senha.isalpha()
                        )  
                        soh_letras_e_num = (
                            senha.isalnum()
                        )  
                        eh_valida = (
                            tamanho
                            or minuscula  
                            or maiuscula  
                            or soh_letras  
                            or soh_letras_e_num  
                        )
                        if eh_valida:
                            print("Senha inválida")
                        else:
                            print("Senha válida")
                        print(esp,linha)
                
                print("Validando o login e usuario")
                validando_login = input("Digite o seu login:\n")
                if validando_login != login:
                    print("login incorreto!")
                else:
                    print("login correto")

                print("\n")

                validando_senha = input("Digite a sua senha:\n")
                if validando_senha != senha:
                    print("senha incorreta!")
                else:
                    print("senha correta")
                
                print(esp,linha)

                while True:
                    print(f"Bem vindo(a) {nome}!")
                    print("Digite uma das opção:")
                    print("\t1 Número primo")
                    print("\t2 Proteger a senha")

                    escolha = input("DIgite uma das opções:\n")

                    match escolha:
                        case "1":
                            print("NÚMERO PRIMO")
                            n = int(input("Digite um número inteiro e maior que zero:\n "))
                            eh_primo = True
                            for i in range(2, n // 2):
                                if n % i == 0:
                                    eh_primo = False  
                                    break
                            print(f"{n} {'' if eh_primo else 'não '}é primo")


        

                         
                        
                        
        case "3":
            pc = input("Deseje encerrar o programa?")
            match pc:
                case "s"|"sim"|"SIM"|"sIM"|"Sim"|"S":
                    break
                case _:
                    print("Continuando o programa")
                    print(linha, esp)
                    continue

