esp = "\n\n"
linha = "=" * 50

while True:
    print("Cp1 de Python")
    print("\t1 Validação delogin e senha")
    print("\t2 Cadastrando o usuário")
    print("\t3 Encontre um número primo")
    print("\t4 Protegendo a senha")
    print("\t5 Login com a senha protegida")
    print("\t6 Encerrar")

    opcao = input("Digite um número\n")
    
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
                        print("LOGIN")
                        login = input("Digite um Email:\n")
                        if "@" and ".com"in login:
                            print("Login valida")
                        else:
                            print("Login invalido")

                    case "2":
                        print(esp,linha)
                        print("USER-NAME")
                        user_name = input("Digite um nome de usuario:\n")
                        
                        
        case "6":
            break