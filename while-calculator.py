
while True:

    first_numberInput = input("Type a number: ")
    second_numberInput = input("Type another number: ")
    operatorSelect = input("(+ - / *) Select the account operator: ")

    validValue = None
    
    try:
        # Conversão dos inputs para números de ponto flutuante (com decimais).
        firstFloat = float(first_numberInput)
        secondFloat = float(second_numberInput)
        validValue = True
    
    except:
        validValue = None

    if validValue is None:
        print("One or each numbers typed are invalid.")
        continue

    allowedOperators = "+-/*"  # Operadores permitidos 

    # Se o operador não estiver na lista de operadores permitidos.
    if operatorSelect not in allowedOperators:
        print("You selected an invalid operator.")
        continue

    # Se o número de operadores digitados no input forem maiores que 1.
    if len(operatorSelect) > 1:
        print("You typed more than one operator. Select only one of them")
        continue
    
    if operatorSelect == "+":
        print(f"'{firstFloat}' + '{secondFloat}' result is {firstFloat + secondFloat}")

    elif operatorSelect == "-":
        print(f"'{firstFloat}' - '{secondFloat}' result is {firstFloat - secondFloat}")

    elif operatorSelect == "/":
        print(f"'{firstFloat}' / '{secondFloat}' result is {firstFloat / secondFloat}")

    elif operatorSelect == "*":
        print(f"'{firstFloat}' * '{secondFloat}' result is {firstFloat * secondFloat}")

    # Esse else só será atingido caso ocorra algo inesperado.
    else:
        print("You're not supposed to reach this")

    # Qualquer input que comece com "y" será considerado.
    # Lower para padronizar o input em letras minusculas.
    exitInput = input("Do you want to leave the program? Type [y]: ").lower().startswith("y")

    # Se o input da saída for verdadeiro, o ciclo do programa será quebrado.
    if exitInput is True:
        break 