#Importei biblioteca PySimple para manter o código original
import FreeSimpleGUI as sg

#Configurando o tema
sg.theme("DarkBlue3")


menu = """

[d] Depositar 
[s] Sacar 
[e] Extrato
[q] Sair

==> """

valor = 0
saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#Função para substituir o input do menu
def mostrar_menu():
    layout = [
        [sg.Text("SISTEMA BANCÁRIO", font=("helvetica", 16))],
        [sg.Button("Depositar", key="d", size=(15,1))],
        [sg.Button("Sacar", key="s", size=(15,1))],
        [sg.Button("Extrato", key="e", size=(15,1))],
        [sg.Button("Sair", key="q", size=(15,1))]
    ]
    window = sg.Window("Banco Dio", layout , element_justification='c')
    event,_ = window.read()
    window.close() 
    return event


while True:

    opcao = mostrar_menu()

    if opcao == "d":
        valor_str = sg.popup_get_text("Informe o valor de depósito: ", title="Depósito")
        valor = float(valor_str) if valor_str else 0

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            sg.popup(f"Depósito de R$ {valor:.2f} realizado!")
        else:
            sg.popup_error(f"Operação falhou ! O valor informado é inválido.")
    
    elif opcao == "s":
        valor_str = sg.popup_get_text("Informe o valor do saque")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            sg.popup_error("Operação falhou! Você não tem saldo suficiente")
        elif excedeu_limite:
            sg.popup_error("Operação falhou! O valor do saque excedeu o limite")
        elif excedeu_saques:
            sg.popup_error("Operação falhou! O npumero de saques foi excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            sg.popup(f"Saque de R$ {valor:.2f} realizado!", title="Sucesso")
        else: 
            sg.popup_error("Operação falhou! O valor informado é inválido")
    elif opcao == "e":
        conteudo_extrato = "Não foram realizadas movimentações. " if not extrato else extrato
        sg.popup_scrolled(
            f"{conteudo_extrato}\n\nSaldo atual: R$ {saldo:.2f}", title="Extrato"
        )

    elif opcao in ("q", None):
        break

    else:
        sg.popup_warning("Operação inválida, por favor selecione uma opção válida e tente novamente. ")
