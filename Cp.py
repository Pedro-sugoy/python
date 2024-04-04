esp = "\n\n"
linha = "=" * 50
from datetime import date
time = date.today()

while True:
    print(esp,linha)
    print(f"Cp1 de Python\n{time}")
    print("bom dia!")
    print("\t1 -Fazer um login e senha")
    print("\t2 -Entrar como usuário")
    print("\t3 -Encerrar")


    opcao = input("Digite uma das opções:\n")
    
    match opcao:
        case "1"|"1 -Fazer um login e senha"|"Fazer um login e senha":#Questão 1 início
            while True:
                print(esp,linha)
                print("Escolha um dos 3 métodos de de login")
                print("\a1 -Email")
                print("\a2 -User-name")
                print("\a3 -RG ou CPF")
                print("\a4 -Voltar")
                
                esc_usuario = input("Digite uma das opções:\n")

                match esc_usuario:
                    case "1"|"1 -Email"|"Email":
                        print(esp,linha)
                        print("EMAIL")
                        login = input("Digite um Email (Use o formato: xxxxx@yyy.zzz/(.zz)):\n")
                        if "@" in login:
                             print("Email válido")
                        else:
                             print("Email inválido")
                             break
                        
                        print(esp,linha)

                        senha = input("Crie uma senha:\n ") # Questão 5 
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
                          
                        n = 479 #Questão 4 
                        senha_ord = ""
                        for c in senha:
                            senha_ord += str(ord(c))
                        senha_hash = int(senha_ord) % n
                        senha = senha_hash # Questão 4 fim / Questão 5 fim

                        print(esp,linha)

                    case "2"|"2 -User-name"|"User-name":
                        print(esp,linha)
                        print("USER-NAME")
                        login = input("Digite um nome de usuario(Por favor usar apenas o ''_'' como caractere especial):\n")
                        letra_num = (
                             login.isalnum()
                        ) 
                        if letra_num or "_" in login:
                            print("Nome de usuário válido")
                        else:
                            print("Nome de usuário inválido!")
                            break

                        print(esp,linha)

                        senha = input("Crie uma senha:\n ")
                        tamanho = len(senha) < 12
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
                             
                        n = 479
                        senha_ord = ""
                        for c in senha:
                            senha_ord += str(ord(c))
                        senha_hash = int(senha_ord) % n
                        senha = senha_hash

                        print(esp,linha)
                        
                    case "3"|"3 -RG ou CPF"|"-RG ou CPF":
                        print(esp,linha)
                        print("RG/CPF")
                        login = input("Digite o seu RG ou CPF (USE O FORMATO CPF: XXX.XXX.XXX-XX ou XXXXXXXXXXX/RG: XX.XXX.XXX-X ou XXXXXXXXX):\n")
                        tamanho = len(login) > 9
                        numeros = (
                             login.isnumeric()
                        )
                        certo = (
                             numeros
                             or tamanho
                        )
                        tam_errado = len(login) < 9
                        letra = (
                             login.isalpha()
                        )
                        erro = (
                             letra
                             or tam_errado
                        )
                        if erro:
                            print("RG ou CPF inválido!")
                            break
                        elif certo:
                             print("RG ou CPF válido")
                        

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
                          
                        n = 479
                        senha_ord = ""
                        for c in senha:
                            senha_ord += str(ord(c))
                        senha_hash = int(senha_ord) % n
                        senha = senha_hash #Questão 1 final

        case "2"|"2 -Entrar como usuário"|"Entrar como usuário":#Questão 2 início
            print(esp,linha)
            print("ENTRAR COMO USUARIO")
            nome = input("Digite o seu nome:\n")
            while True:
                print(esp,linha)
                print("Válide o usuario e a senha")
#######################################################################################################
                # print("Escolha um dos 3 métodos de de login")
                # print("\a1 -Email")
                # print("\a2 -User-name")
                # print("\a3 -RG ou CPF")
                # print("\a4 -Voltar")
                
                # esc_usuario = input("Digite uma das opções:\n")

                # match esc_usuario:
                #     case "1"|"1 -Email"|"Email":
                #         print(esp,linha)
                #         print("EMAIL")
                #         login = input("Digite um Email (Use o formato: xxxxx@yyy.zzz/(.zz)):\n")
                #         if "@" in login:
                #              print("Email válido")
                #         else:
                #              print("Email inválido")
                #              break
                        
                #         print(esp,linha)

                #         senha = input("Crie uma senha:\n ") # Questão 5 
                #         tamanho = len(senha) < 8  
                #         minuscula = (
                #                 senha.islower()
                #                 )  
                #         maiuscula = (
                #                 senha.isupper()
                #                 )  
                #         soh_letras = (
                #                 senha.isalpha()
                #                 )  
                #         soh_letras_e_num = (
                #                 senha.isalnum()
                #                 )  
                #         eh_valida = (
                #                 tamanho
                #                 or minuscula  
                #                 or maiuscula  
                #                 or soh_letras  
                #                 or soh_letras_e_num  
                #                 )
                #         if eh_valida:
                #                 print("Senha inválida")
                #         else:
                #                 print("Senha válida")   
                #                 break
                          
                #         n = 479 #Questão 4 
                #         senha_ord = ""
                #         for c in senha:
                #             senha_ord += str(ord(c))
                #         senha_hash = int(senha_ord) % n
                #         senha = senha_hash # Questão 4 fim / Questão 5 fim

                #         print(esp,linha)

                #     case "2"|"2 -User-name"|"User-name":
                #         print(esp,linha)
                #         print("USER-NAME")
                #         login = input("Digite um nome de usuario(Por favor usar apenas o ''_'' como caractere especial):\n")
                #         letra_num = (
                #              login.isalnum()
                #         ) 
                #         if letra_num or "_" in login:
                #             print("Nome de usuário válido")
                #         else:
                #             print("Nome de usuário inválido!")
                #             break

                #         print(esp,linha)

                #         senha = input("Crie uma senha:\n ")
                #         tamanho = len(senha) < 12
                #         minuscula = (
                #                 senha.islower()
                #                 )  
                #         maiuscula = (
                #                 senha.isupper()
                #                 )  
                #         soh_letras = (
                #                 senha.isalpha()
                #                 )  
                #         soh_letras_e_num = (
                #                 senha.isalnum()
                #                 )  
                #         eh_valida = (
                #                 tamanho
                #                 or minuscula  
                #                 or maiuscula  
                #                 or soh_letras  
                #                 or soh_letras_e_num  
                #                 )
                #         if eh_valida:
                #                 print("Senha inválida")
                #         else:
                #                 print("Senha válida")
                #                 break
                             
                #         n = 479
                #         senha_ord = ""
                #         for c in senha:
                #             senha_ord += str(ord(c))
                #         senha_hash = int(senha_ord) % n
                #         senha = senha_hash

                #         print(esp,linha)
                        
                #     case "3"|"3 -RG ou CPF"|"-RG ou CPF":
                #         print(esp,linha)
                #         print("RG/CPF")
                #         login = input("Digite o seu RG ou CPF (USE O FORMATO CPF: XXX.XXX.XXX-XX ou XXXXXXXXXXX/RG: XX.XXX.XXX-X ou XXXXXXXXX):\n")
                #         tamanho = len(login) > 9
                #         numeros = (
                #              login.isnumeric()
                #         )
                #         certo = (
                #              numeros
                #              or tamanho
                #         )
                #         tam_errado = len(login) < 9
                #         letra = (
                #              login.isalpha()
                #         )
                #         erro = (
                #              letra
                #              or tam_errado
                #         )
                #         if erro:
                #             print("RG ou CPF inválido!")
                #             break
                #         elif certo:
                #              print("RG ou CPF válido")
                        

                #         print(esp,linha)

                #         senha = input("Crie uma senha:\n ")
                #         tamanho = len(senha) < 8  
                #         minuscula = (
                #                 senha.islower()
                #                 )  
                #         maiuscula = (
                #                 senha.isupper()
                #                 )  
                #         soh_letras = (
                #                 senha.isalpha()
                #                 )  
                #         soh_letras_e_num = (
                #                 senha.isalnum()
                #                 )  
                #         eh_valida = (
                #                 tamanho
                #                 or minuscula  
                #                 or maiuscula  
                #                 or soh_letras  
                #                 or soh_letras_e_num  
                #                 )
                #         if eh_valida:
                #                 print("Senha inválida")
                #         else:
                #                 print("Senha válida")   
                #                 break
                          
                #         n = 479
                #         senha_ord = ""
                #         for c in senha:
                #             senha_ord += str(ord(c))
                #         senha_hash = int(senha_ord) % n
                #         senha = senha_hash #Questão 1 final
#######################################################################################################
                validando_login = input("Digite o seu login:\n")
                if validando_login != login:
                    print("login incorreto!")
                    break
                else:
                    print("login correto")

                print("\n")

                validando_senha = input("Digite a sua senha:\n")
                if validando_senha != senha:
                    print("senha incorreta!")
                    break
                else:
                    print("senha correta")
                
                print(esp,linha)#Questão 2 final

                while True:
                    print(f"Bem vindo(a) {nome}!")
                    print("Digite 1:\n")
                    print("\t1 Número primo")

                    escolha = input("DIgite uma das opções:\n")

                    match escolha:
                        case "1":
                            validando_login2 = input("Digite o seu login:\n")
                            if validando_login2 != login:
                                print("login incorreto!")
                                break
                            else:
                                print("login correto")

                            print("\n")

                            validando_senha2 = input("Digite a sua senha:\n")
                            if validando_senha2 != senha:
                                print("senha incorreta!")
                                break
                            else:
                                print("senha correta")
                                print(esp,linha)

                            print("NÚMERO PRIMO")
                            N = int(input("Digite um número, para achar o maio número primo até ele:\n"))  
                            maior_primo = 0
                            for num in range(2, N+1):
                                eh_primo = True
                                for i in range(2, int(num**0.5) + 1):
                                    if num % i == 0:
                                        eh_primo = False
                                        break
                                if eh_primo:
                                    maior_primo = num
                            print(maior_primo)
                            print(esp,linha)

                        
                                             
        case "3"|"3 -Encerrar"|"-Encerrar":
            pc = input("Deseje encerrar o programa?")
            match pc:
                case "s"|"sim"|"SIM"|"sIM"|"Sim"|"S":
                    break
                case _:
                    print("Continuando o programa")
                    print(linha, esp)
                    continue

