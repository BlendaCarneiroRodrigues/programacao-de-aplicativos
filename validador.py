ano = int(input("digite o ano: "))

if (ano % 4 == 0 and ano % 100 == 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bisxesto!")
else:
    print(f"O ano {ano} é um ano comum.")    