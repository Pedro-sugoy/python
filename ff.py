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

n = int(input("Digite um número inteiro e maior que zero:\n "))
eh_primo = True
for i in range(2, n // 2):
        if n % i == 0:
                eh_primo = False  
print(f"{n} {'' if eh_primo else 'não '}é primo")


print("Proteger a sua senha")
senha_ord = n
for c in senha:
        senha_ord += str(ord(c))
        int(senha_ord) % eh_primo
        
        # Pedro@sugoy1