from HashTable import HashTable

names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Ian", "Julia", "Alice"]

table = HashTable(len(names))
count = 0
for name in names:
    if table.buscar(name) is None:
        table.inserir(name, count)
        count += 1
    else:
        print("Duplicado -> ", name)


print("Valor referente ao nome buscado:" ,table.buscar("Alice"))



