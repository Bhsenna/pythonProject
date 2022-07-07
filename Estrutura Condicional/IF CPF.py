# 000.000.00X-00

cpf = input('Digite o seu CPF: ').replace('.', '').replace('-', '')
estado = cpf[8]
if estado == '0':
    print('Rio Grande do Sul')
elif estado == '1':
    print('Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins')
elif estado == '2':
    print('Amazonas, Pará, Roraima, Amapá, Acre e RondôniaRio Grande do Sul')
elif estado == '3':
    print('Ceará, Maranhão e Piauí')
elif estado == '4':
    print('Paraíba, Pernambuco, Alagoas e Rio Grande do Norte')
elif estado == '5':
    print('Bahia e Sergipe')
elif estado == '6':
    print('Minas Gerais')
elif estado == '7':
    print('Rio de Janeiro e Espírito Santo')
elif estado == '8':
    print('São Paulo')
elif estado == '9':
    print('Paraná e Santa Catarina')