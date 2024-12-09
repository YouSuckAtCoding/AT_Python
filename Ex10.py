from SimpleStack import Stack

def navigate(choice, stack, aux):
    if choice == 'a':
        if stack.isFull():
            print("Ultima página")
            return
        stack.push(aux.pop())
        print(stack.peek())
        return
    else:
        if len(stack) == 1:
            print("Primeira página")
            return
        aux.push(stack.pop())
        print(stack.peek())
        return



stack = Stack(10)
aux = Stack(10)

for i in range(1, 11):
    stack.push(str.format("pag {}", i))

while not stack.isEmpty():
    choice = input("Avançar : a, Voltar : r, Sair : x \n")

    if choice == "x":
        break

    if choice != "a" and choice != "r":
        choice = input("Favor escolher uma opção valida. Avançar : a, Voltar : r")
    else:
        navigate(choice, stack, aux)
