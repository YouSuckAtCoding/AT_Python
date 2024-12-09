from HashTable import HashTable

users = [
    [1, "Alice", 25, "alice@gmail.com"],
    [2, "Bob", 30, "bob@gmail.com"],
    [3, "Charlie", 22, "charlie@gmail.com"],
    [4, "Diana", 28, "diana@gmail.com"],
    [5, "Eve", 27, "eve@gmail.com"],
    [6, "Frank", 35, "frank@gmail.com"],
    [7, "Grace", 24, "grace@gmail.com"],
    [8, "Hannah", 29, "hannah@gmail.com"],
    [9, "Ian", 26, "ian@gmail.com"],
    [10, "Julia", 23, "julia@gmail.com"]
]

print(users)

table = HashTable(len(users))

for user in users:
    if table.buscar(user[1]) is None:
        table.inserir(user[1], user)
    else:
        print("Nome já cadastrado.")

print(table.buscar("Alice"))


