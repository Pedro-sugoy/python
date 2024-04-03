print("RG")
rg = input("Digite o seu RG:\n")
tamanho = len(rg) < 11  # Verifica se a senha tem menos de 11 caracteres
minuscula = (
rg.islower()
                                            )  # Verifica se a senha é composta apenas por letras minúsculas
maiuscula = (
                                    rg.isupper()
                                            )  # Verifica se a senha é composta apenas por letras maiúsculas
soh_letras = (
                                    rg.isalpha()
                                            )  # Verifica se a senha é composta apenas por letras
soh_letras_e_num = (
                                    rg.isalnum()
                                            )  # Verifica se a senha é composta apenas por letras e números
                                            # Verifica se a senha é válida e imprime o resultado
eh_valida = (
                                    tamanho
                                    or minuscula  # minúscula
                                    or maiuscula  # maiúscula
                                    or soh_letras  # alfabético
                                    or soh_letras_e_num  # alfa numérico
                                            )
if eh_valida:
                                    print("RG inválido")
elif not eh_valida:
                                    print("RG válido")
