# página criada com o objetivo de realizar cadastros de novos clientes na aplicação.

def validarCPF(cpf):
    if len(cpf) == 11:
        val = int(cpf[9])
        cont = 2
        soma = 0
        for i in range(8, -1, -1):
            numero = int(cpf[i])
            soma = soma + (numero*cont)
            cont += 1
        res = soma % 11
        if res < 2:
            tent = 0
        else:
            tent = 11 - res
        if tent == val:
            val1 = int(cpf[10])
            cont1 = 2
            soma1 = 0
            for j in range(9, -1, -1):
                num1 = int(cpf[j])
                soma1 = soma1 + (num1*cont1)
                cont1 += 1
            res1 = soma1 % 11
            if res1 < 2:
                tent1 = 0
            else:
                tent1 = 11 - res1
            if tent1 == val1:
                d = cpf
            else:
                d = 0
        else: 
            d = 0
    else:
        d = 0

    return d