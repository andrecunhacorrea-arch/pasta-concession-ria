print("Bem-vindo à concessionária dos Uchihas")

pessoa = int(input("Você é um cliente ou vendedor? (1 = cliente | 2 = vendedor): "))

match pessoa:
    case 1:
        print("Você escolheu ser um cliente")
        cliente = {
            "nome": input("Informe seu nome: "),
            "email": input("Informe seu e-mail: "),
            "saldo": float(input("Informe o seu saldo atual (R$): "))
        }
        print("\n cliente cadrastado")
        

    case 2:
        print("Você escolheu ser um vendedor")
        vendedor = {
            "nome": input("Informe seu nome: "),
            "email": input("Informe seu e-mail: ")
        }
        print("vendedor cadrastado")

    case _:
        print("\n Só temos as opções 1 ou 2.")


print("====== Concessionária dos uchihas ======")

carros = {
    "porsche": {
        "skyline": 5000.0,
        "porsche 911 carrera": 749486.0,
        "porsche 911 t": 1046812.0,
        "porsche 911 targa 4 gts": 1431250.0,
        "porsche 911 4s coupe 2017": 580563.0,
        "porsche cayenne turbo gt": 1631250.
    },
    
    "nissan":{
        "Nissan Kicks Sense 1.6": 99044.0,
        "Nissan Kicks Active CVT 1.6": 90994.0,
        "Nissan Kicks Exclusive 1.6": 120079.0,
        "Nissan March 1.6 S": 40610,
        "Nissan March SL 1.6": 42527.0,
        "Nissan March SV 1.6": 43154.0,
        "Nissan Versa Exclusive 1.6 Aut.": 141726.0,
        "Nissan Versa SL 1.6 FlexStart 4p Aut.": 65293.0,
        "Nissan Sentra Advance 2.0 Aut.": 166.207,
        "Nissan Sentra Exclusive 2.0 Aut.": 182649.0,
        "Nissan Sentra Int. Premium 2.0 Aut.": 194009.0,
        "Nissan Sentra Exclusive 2.0 Aut.": 159387.0,
        "Nissan Sentra Exclu. Int. Premium 2.0 Aut.": 177025.0,
        "Nissan Frontier XE 4x4 2.3 Diesel": 232471.0
    },
    "chrevolet":{
        "Onix 1.0 Hatch": 67641.0,
        "Onix 1.0 Turbo Hatch": 79731.0,
        "Onix 1.0 Turbo LTZ": 81778.0,
        "Onix Plus Sedan 1.0": 72900.0,
        "Cruze LT 1.4 Turbo": 78063.0,
        "Cruze LTZ 1.4 Turbo": 81314.0,
        "S10 2.8 Diesel LS 4x4": 134525.0,
        "S10 2.5 Flex Advantage CD 4x2": 133305.0,
        "S10 2.8 Diesel LTZ 4x4 CD": 158740.0,
        "S10 Z71 Diesel 2.8 4x4":167802.0,
        "D-20 Diesel 1987": 52014.0
    }
}

def menu_cliente():
    print("opções de cliente")
    print("\n 1 - comprar carro")
    print(" 2 - alugar carro")
    print(" 3 - ver estoque")
    print(" 4 - sair")


def menu_vendedor():
    print("opções vendedor ")
    print("\n 1 -vender carro")
    print(" 2 - consultar tabela fipe")
    print(" 3 - sair")

def comprar_carro(cliente):
    while True:
        print("\n=== Comprar carro ===")
        print("modelos disponíveis: ")
        for marca in carros:
                print(f"- {marca}")
            
        marca_escolhida = input(("escollha a marca: ").lower())
            
        if marca_escolhida in carros:
                print("carros disponíceis: ")
                for modelos, preco in carros[marca_escolhida].items():
                
                 print(f"- {modelos} - R${preco}")

        if marca_escolhida not in carros:
            print("marca não encontrada, tente novamente")
            return
        
        preco_base = carros[marca_escolhida][modelos]
        preco_final = preco_base*1.25

        print(f"\n preço da tabela fipe: R${preco_base}")
        print(f"preço com a taxa da loja: R${preco_final}")

        confirmar = input(" deseja comprar o carro? (S/N): ").lower()

        if confirmar == "s":
            print(f"\n Parabéns, você comprou um {marca_escolhida} por R${preco_final}!\n")

        else:
            print("\n compra cancelada.\n")

#Inicio do menu
if pessoa == 1:
    menu_cliente()
    opc = int(input("escolha uma opção: "))
    
    match opc:
        case 1:
            comprar_carro(cliente)

        case 2:
            print("você escolheu alugar um carro")
        case 3:
            print("você escolheu ver estoque")
        

else:
    menu_vendedor()