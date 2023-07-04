{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOJNUxWUH3SaR8Go3BWcifQ"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 44,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uapEkcLyx_xf",
        "outputId": "28d9ee56-f937-4026-8952-57c5b6fc8efe"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Menu\n",
            "\n",
            "[1] Depositar\n",
            "[2] Sacar\n",
            "[3] Extrato\n",
            "[0] Sair\n",
            "\n",
            "=> Digite valor da operação que deseja executar!\n",
            "1\n",
            "Valor do depósito: 5000\n",
            "Deposito efetuado no valor de: R$ 5000.00\n",
            "\n",
            "Menu\n",
            "\n",
            "[1] Depositar\n",
            "[2] Sacar\n",
            "[3] Extrato\n",
            "[0] Sair\n",
            "\n",
            "=> Digite valor da operação que deseja executar!\n",
            "1\n",
            "Valor do depósito: 3000\n",
            "Deposito efetuado no valor de: R$ 3000.00\n",
            "\n",
            "Menu\n",
            "\n",
            "[1] Depositar\n",
            "[2] Sacar\n",
            "[3] Extrato\n",
            "[0] Sair\n",
            "\n",
            "=> Digite valor da operação que deseja executar!\n",
            "1\n",
            "Valor do depósito: 150.50\n",
            "Deposito efetuado no valor de: R$ 150.50\n",
            "\n",
            "Menu\n",
            "\n",
            "[1] Depositar\n",
            "[2] Sacar\n",
            "[3] Extrato\n",
            "[0] Sair\n",
            "\n",
            "=> Digite valor da operação que deseja executar!\n",
            "3\n",
            "========= Extrato =========\n",
            "\n",
            "Depósito: R$ 5000.00\n",
            "Depósito: R$ 3000.00\n",
            "Depósito: R$ 150.50\n",
            "\n",
            "\n",
            "Saldo na conta: R$8150.50\n",
            "===========================\n",
            "\n",
            "Menu\n",
            "\n",
            "[1] Depositar\n",
            "[2] Sacar\n",
            "[3] Extrato\n",
            "[0] Sair\n",
            "\n",
            "=> Digite valor da operação que deseja executar!\n",
            "0\n",
            "Obrigado por utilizar os serviços do nosso banco, tenha um bom dia!\n"
          ]
        }
      ],
      "source": [
        "menu = '''\n",
        "Menu\n",
        "\n",
        "[1] Depositar\n",
        "[2] Sacar\n",
        "[3] Extrato\n",
        "[0] Sair\n",
        "\n",
        "=> Digite valor da operação que deseja executar!\n",
        "'''\n",
        "\n",
        "saldo = 0\n",
        "limite = 500\n",
        "extrato = ''\n",
        "saques_diario = 0\n",
        "LIMITE_SAQUES = 3\n",
        "\n",
        "while True:\n",
        "  opcao = input(menu)\n",
        "\n",
        "  if opcao == '1':\n",
        "    valor = float(input('Valor do depósito: '))\n",
        "\n",
        "    if valor > 0:\n",
        "      saldo += valor\n",
        "      extrato += f'Depósito de: R$ {valor:.2f}\\n'\n",
        "      print(f'Deposito efetuado no valor de: R$ {valor:.2f}')\n",
        "\n",
        "    else:\n",
        "      print('Opração falhou. O valor informado não é válido.')\n",
        "\n",
        "  elif opcao == '2':\n",
        "    valor = float(input('Valor do saque: '))\n",
        "\n",
        "    if valor > saldo:\n",
        "      print('Operação falhou! Saldo insuficiente.')\n",
        "\n",
        "    elif valor > limite:\n",
        "      print('Operação falhou! Valor do saque maior que o seu limite.')\n",
        "\n",
        "    elif saques_diario >= LIMITE_SAQUES:\n",
        "      print('Operação falhou! Limite de saques excedido.')\n",
        "\n",
        "    elif valor > 0:\n",
        "      saldo -= valor\n",
        "      saques_diario +=1\n",
        "      extrato += f'Saque de: R$ {valor:.2f}\\n'\n",
        "      print(f'Saque efetuado no valor de: R${valor:.2f}. Você ainda pode efetuar um total de {LIMITE_SAQUES - saques_diario} saques hoje.')\n",
        "\n",
        "    else:\n",
        "      print('Operação falhou! O valor informado não é válido.')\n",
        "\n",
        "  elif opcao == '3':\n",
        "    print('========= Extrato =========\\n')\n",
        "    print('Nenhuma movimentação encontrada.' if not extrato else extrato)\n",
        "    print(f'\\nSaldo na conta: R${saldo:.2f}')\n",
        "    print('===========================')\n",
        "\n",
        "  elif opcao == '0':\n",
        "    print('Obrigado por utilizar os serviços do nosso banco, tenha um bom dia!')\n",
        "    break\n",
        "\n",
        "  else:\n",
        "    print('Operação inválida, por favor selecione novamente a operação desejada')"
      ]
    }
  ]
}