from decimal import Decimal

# Menu do sistema do banco
menu = """  

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Inicalizando as varáveis e a constante
saldo = 0
limite = 500 # limite máximo por saque (3xdia)
extrato = " " # criar uma lista/array com as prints dos depositos e saques
numero_saques = 0
LIMITE_SAQUES = 3 # saques diarios
saque = 0

# Lista para armazenar todas as operações
operacoes = []

# Estrutura de repetição para realizar as operações conforme to do's do desafio
while True:
    
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = int(input("Qual valor deseja depositar? "))
        saldo += deposito
        print(f"Depósito realizado saldo de: R$ {saldo:.2f}")
        
        valor_deposito = (f"Depósito realizado de: R$ {deposito:.2f}")
        operacoes.append(valor_deposito)
        
        continue
    
    elif opcao == "s":
        print("Saque")
        saque = int(input("Quanto deseja sacar? "))
        if numero_saques < LIMITE_SAQUES:
            if saque > limite:
                print("Valor maior que limite máximo por saque!")
            elif saque < saldo:
                saldo -= saque
                numero_saques += 1
                print(f"Saque realizado saldo de: R$ {saque:.2f}")
                valor_saldo = (f"O saldo atual é: R$ {saldo:.2f}")
                
                valor_saque = (f"Saque realizado de: R$ {saque:.2f}")
                operacoes.append(valor_saque)
                
            else:
                print("Saldo insuficiente!")
        else:
            print("Você chegou ao limite diário de saques! ")
        continue
    
    elif opcao == "e":
        print("Extrato")

        extrato = f"""
==================== MENU ==================== 

Histórico:
{"\n".join(operacoes)}

{(valor_saldo)}

==============================================
"""
        
        print(extrato.strip())
    
    elif opcao == "q":
        print("Sair")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")