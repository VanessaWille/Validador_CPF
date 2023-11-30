from Exercicio1 import ValidadorCPF

if __name__ == "__main__":
    cpf_input = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")
    validator = ValidadorCPF(cpf_input)

    if validator.validacao_cpf():
        print("CPF é válido")
    else:
        print("CPF inválido")