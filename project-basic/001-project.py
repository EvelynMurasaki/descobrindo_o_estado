"""
Este Projeto é para um usuario informar apenas os numeros do seu CPF e com isso o codigo vai informar a qual estado
ele pertence
- 3 ultimos numeros (criar regra pra nao pegar string ou float apenas numero inteiro
- fazer if para a resposta
Dígito	Estado(s)
0	Rio Grande do Sul
1	Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins
2	Amazonas, Pará, Roraima, Amapá, Acre e Rondônia
3	Ceará, Maranhão e Piauí
4	Paraíba, Pernambuco, Alagoas e Rio Grande do Norte
5	Bahia e Sergipe
6	Minas Gerais
7	Rio de Janeiro e Espírito Santo
8	São Paulo
9	Paraná e Santa Catarina
xxx-xxx-xxx-xx
012-345-678-9
"""

print("""BEM VINDO AO JOGO DE ADIVINHAÇÂO DE ESTADO!\n
Vamos começar os jogos?!, abaixo passe algumas informações:""")

nome = input('Qual é o seu nome?:')
print('Olá', nome, ',' 'agora me informe o numero do seu CPF!')
cpf = str(input(' '))

try:
    cpf = int(cpf[8])
    if cpf == 0:
        print('Voce é do: Rio Grande do Sul')
    elif cpf == 1:
        print('Você é de um desses estados: Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul ou Tocantins')
    elif cpf == 2:
        print('Você é de um desses estados: Amazonas, Pará, Roraima, Amapá, Acre ou Rondônia')
    elif cpf == 3:
        print('Você é de um desses estados: Ceará, Maranhão ou Piauí')
    elif cpf == 4:
        print('Você é de um desses estados: Paraíba, Pernambuco, Alagoas ou Rio Grande do Norte')
    elif cpf == 5:
        print('Você é de um desses estados: Bahia ou Sergipe')
    elif cpf == 6:
        print('Você é de: Minas Gerais')
    elif cpf == 7:
        print('Você é de um desses estados: Rio de Janeiro ou Espírito Santo')
    elif cpf == 8:
        print('Você é de: São Paulo')
    elif cpf == 9:
        print('Você é de um desses estados: Paraná ou Santa Catarina')
    else:
        print('CPF não encontrado!')

except:
    print("Numero invalido")

