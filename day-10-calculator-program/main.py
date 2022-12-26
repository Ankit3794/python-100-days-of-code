from calculator import add, subtract, multiply, divide
import art

opeations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '\\' : divide 
}

def calculator():
    n1 = int(input("What's the first number?: "))
    
    should_continue = True
    
    # Print operations on console
    for op in opeations:
        print(op)

    operation = input('Pick an operation: ')

    while should_continue:
        n2 = int(input("What's the next number?: "))

        perform = opeations.get(operation)
        result = perform(n1, n2)
        output_message = f'{n1} {operation} {n2} = {result}'
        print(output_message)

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. Press CTRL+C to close program.\n") == 'y':
            n1 = result
        else:
            calculator()


print(art.logo)
calculator()