#trabalho para fazer uma conscessionária, onde as pessoa podem comprar e vender seus veiculos

carros = {
    "porsche":{
        "911 GT3 (991/992)" : 1708291.0,
        "911 GT3 (2018)": 1527910.0,
        "911 GT3 (2022)": 1661760.0,
        "911 GT3 RS": 2357438.0,
        "911 GT2 RS (2019)": 4028219,
        "911 GT2 RS (2018)": 3929970.0,
        "918 Spyder": 13556900.0,
        "Cayenne S 4.0 V8 (2024)": 855987.0,
        "Cayenne Turbo E-Hybrid 4.0": 1154688.0,
        "Cayenne S 3.0 V6 (Híbrido)": 623684.0
    },
    "nissan":{
        "March": 50000.0,
        "versa": 120000.0,
        "kicks Active": 114318.0,
        "kicks Exclusive": 153568.0,
        "sentra Advanced": 166207.0,
        "sentra Exlcuive":194099.0,
        "tiida":35000.0,
        "leaf":130000.0,
        "frontier S":244371.0,
        "frontier platinum":315267.0
    },
    "audi":{
        "A3 Sedan S-Line 2.0": 227383.0,
        "A3 2023 Performance Black 2.0": 222513.0,
        "A3 2025 Sedan Performance 2.0": 292967.0,
        "Q3 Prestige 2.0": 225084.0,
        "Q3 Performance 2.0": 2430116.0,
        "Q3 Performance Black 2.0": 257553.0,
        "Q3 Sportback Performance 2.0": 256470.0,
        "Q3 Sportback Performance Black 2.0": 26134.0,
        "A4 Prestige 2.0": 191064.0,
        "A4 S-Line 2.0 TFSI": 209391.0
    },
    "volkswagen": {
        "Polo 1.0 MPI Flex": 74848.0,  
        "Polo GTS 1.4 TSI Flex": 125556.0,  
        "Virtus TSI 1.0 Flex Manual": 92270.0,  
        "Virtus TSI 1.0 Flex Automático": 97168.0,  
        "Virtus Highline 200 TSI 1.0 Flex": 113858.0,  
        "T-Cross Sense 200 TSI 1.0 Flex Auto": 106144.0,  
        "T-Cross Comfortline 200 TSI 1.0 Flex Auto": 130693.0,  
        "T-Cross Highline 250 TSI 1.4 Flex Auto": 140651.0,  
        "Nivus Sense 200 TSI 1.0 Flex Auto": 106366.0,  
        "Nivus Highline 200 TSI 1.0 Flex Auto": 121682.0  
}
}

print("===== BEM VINDO A NOSSA CONCESSIONÁRIA DOS UCHIHAS =====")
pessoa = int(input("você é um vendedor ou um cliente da loja? (1 para cliente | 2 para vendedor): "))

match pessoa:
    case 1:
        print("===== CADRASTRO CLIENTE =====")
        cliente ={
            "nome": input("nome: "),
            "email": input("endereço eletrônico (Email): "),
            "saldo": float(input("saldo atual (R$): "))
        }
        print("\nCliente Cadrastrado com sucesso!")

    case 2:
        print("===== CADRASTRO VENDEDOR =====")
        vendedor ={
            "nome": input("nome: "),
            "email": input("endereço eletrônico (Email): "),
            "id": int(input("ID do vendedor: "))
        }
        print("\nVendedor cadrastrado com sucesso!")

while True:
    pessoa = int(input("escolha o menu: 1 para cliente | 2- para vendedor | 3 - sair do sistema: "))

    def menu_cliente():
        print("\n===== MENU DO CLIENTE =====")
        print("1- comprar carro")
        print("2 - alugar carro")
        print("3- ver preços dos carros")
        print("4- vender carro para a loja")
        print("5- sair")

    def menu_vendedor():
        print("\n===== MENU VENDEDOR =====")
        print(" 1- registrar carro novo no estoque")
        print(" 2- consultar tabela FIPE")
        print(" 3- ver estoque completo")
        print(" 4- voltar a tela incial")
        print(" 5- sair")

    if pessoa == 1:
        while True:
            menu_cliente()
            opc = int(input("escolha a opção: "))

            if opc == 1:
                print("você escolheu comprar um carro")

            elif opc == 2:
                print("você escolheu alugar um carro")

            elif opc == 3:
                print("ver preço dos carros")

            elif opc == 4:
                print("vender carro para a loja")
        
            elif opc == 5:
                print("saindo do sistema, obriagdo por confiar em nossa loja")
                break

            else:
                print("opção invalida, tente novamente")

    elif pessoa == 2:
        id_digitado = int(input("\n digite seu ID para entrar no menu de vendedor: "))
        if id_digitado == vendedor["id"]:
            print("ID confirmado! acessando menu de vendedor")

        else:
            print("id incorreto, tente novamente")    
        
        while True:
            menu_vendedor()
            opc = int(input("escolha uma opção: "))

            if opc == 1:
                print("registrar novo carro")

            elif opc == 2:
                print("consultar tabela FIPE")

            elif opc == 3:
                print("consultar estoque completo")

            elif opc == 4:
                print("voltando ao menu ")
                

            elif opc == 5:
                print("saindo do sistema...")
                break

            else:
                print("nenhuma opção válida, tente novamente")           