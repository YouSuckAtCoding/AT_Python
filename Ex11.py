from Queue import Queue
import random

def placeOrder(queue):

    num = random.randint(1,999)
    queue.insert(num)

    print("Seu número é: ", num)

queue = Queue(50)

while True:

    print("Bem vindo ao atendimento ao cliente")
    print()
    print("a para ser atendido")
    print("x para ir embora")
    print("c para consultar quem está sendo atendido")
    print("f para seguir atendimento")


    val = input()

    if val != "a" and val != "x" and val != "c" and val != "f":
        print("a para ser atendido")
        print("x para ir embora")
        print("c para consultar quem está sendo atendido")
        print("f para seguir atendimento")

        val = input()

    elif val == "x":
        break
    elif val == "c":
        if queue.isEmpty():
            print("Ninguém na fila")
        else:
            print("O próximo a ser atendido é: ", queue.peek())
    elif val == "f":
        if queue.isEmpty():
            print("Ninguém na fila")
        else:
            print("Sendo atendido: ", queue.peek())
            queue.remove()
    else:
        if queue.isFull():
            print("Fila cheia")
        else:
            placeOrder(queue)

