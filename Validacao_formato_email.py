# Programa que valida o formato e-mail 


lista_provedor = ["hotmail", "gmail", "outlook", "yahoo", "protonmail"]

while True:
    email = input("Informe o seu email: ")
    if "@" in email and email[email.index("@")+1: email.index(".com")] in lista_provedor:
        usuario = email[0: email.index("@")]
        provedor = email[email.index("@") + 1: email.index(".com")]
        print(f"Usuário: {usuario}")
        print(f"Provedor: {provedor}")
        break

    else:
        print(f"O e-mail informado não exite : {email} .Tente novamente!!")
