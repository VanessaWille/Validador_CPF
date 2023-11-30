import re

class LimpezaCPF:
    """ Classe responsável por limpar o CPF, removendo caracteres não numéricos. """

    @staticmethod
    def limpeza(cpf: str) -> str:
        """
        Limpa o CPF removendo caracteres não numéricos.

        Args:
            cpf (str): O CPF a ser limpo.

        Returns:
            str: O CPF limpo, contendo apenas dígitos.
        """
        return re.sub(r"[^0-9]", "", cpf)

class ValidadorCPF:
    """ Classe responsável pela validação do CPF. """

    def __init__(self, cpf: str):
        """
        Inicializa o validador de CPF.

        Args:
            cpf (str): O CPF a ser validado.
        """
        self.cpf = LimpezaCPF.limpeza(cpf)

    @staticmethod
    def _calcular_digito(digitos: str, peso_inicial: int) -> int:
        """
        Calcula um dígito verificador baseado nos dígitos do CPF e um peso inicial.

        Args:
            digitos (str): Parte do CPF usada para calcular o dígito verificador.
            peso_inicial (int): Peso inicial usado no cálculo.

        Returns:
            int: O dígito verificador calculado.
        """
        digito_calculado = sum(int(digito) * peso for digito, peso in zip(digitos, range(peso_inicial, 1, -1)))
        return (digito_calculado * 10) % 11

    @staticmethod
    def _obter_digito_verificador(digitos_cpf: str, peso: int) -> int:
        """
        Obtém o dígito verificador correto para uma parte do CPF.

        Args:
            digitos_cpf (str): Parte do CPF usada para obter o dígito verificador.
            peso (int): Peso inicial usado para calcular o dígito verificador.

        Returns:
            int: O dígito verificador.
        """
        digito_verificador = ValidadorCPF._calcular_digito(digitos_cpf, peso)
        return digito_verificador if digito_verificador < 10 else 0

    @staticmethod
    def _validar_digitos(cpf: str) -> bool:
        """
        Valida os dígitos verificadores do CPF.

        Returns:
            bool: Verdadeiro se os dígitos verificadores são válidos, falso caso contrário.
        """
        if len(cpf) != 11 or cpf[0] * len(cpf) == cpf:
            return False

        cpf_sem_digitos_verificadores = cpf[:9]
        digito_verificador_1 = ValidadorCPF._obter_digito_verificador(cpf_sem_digitos_verificadores, 10)
        digito_verificador_2 = ValidadorCPF._obter_digito_verificador(cpf_sem_digitos_verificadores + str(digito_verificador_1), 11)

        return int(cpf[9]) == digito_verificador_1 and int(cpf[10]) == digito_verificador_2

    def validacao_cpf(self) -> bool:
        """
        Verifica se o CPF é válido.

        Returns:
            bool: Verdadeiro se o CPF é válido, falso caso contrário.
        """
        return ValidadorCPF._validar_digitos(self.cpf)
