
nome = input("Digite seu nome completo: ")
cpf = input("Digite seu CPF: ")
endereco = input("Digite seu endereço completo: ")
telefone = input("Digite seu número de telefone: ")


saldo_conta = 1000.00
saldo_cartao = 500.00


produto = input("Digite o nome do produto que deseja comprar: ")
preco = 50.00


if preco > saldo_conta + saldo_cartao:
    print("Você não possui saldo suficiente para a aquisição do produto.")
    opcao = input("Deseja retornar à seleção de produtos? (S/N) ")
    if opcao == "S":
      
        pass
    else:
       
        pass
else:
    
    print("Seu saldo atual no cartão é de R$%.2f." % saldo_cartao)
    forma_pagamento = input("Digite a forma de pagamento (cartão ou conta): ")
    if forma_pagamento == "cartão":
        saldo_cartao -= preco
        print("Compra realizada com sucesso! Seu saldo atual no cartão é de R$%.2f." % saldo_cartao)
    else:
        saldo_conta -= preco
        print("Compra realizada com sucesso! Seu saldo atual na conta é de R$%.2f." % saldo_conta)