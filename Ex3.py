def searchcontatoslinear(contatos, selected):
    for i in contatos.keys():
        if i == selected:
            return contatos[i]

contatos = {
    "Carlão": 123,
    "Josefino": 456,
    "Saravá": 789,
    "Xeroxkino": 147
}

print(searchcontatoslinear(contatos, "Josefino"))






