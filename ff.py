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
n = 479
senha_ord = ""
for c in senha:
    senha_ord += str(ord(c))
senha_hash = int(senha_ord) % n
senha = senha_hash
print(senha,senha_hash)