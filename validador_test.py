"""
Módulo de testes para o validador de CPF.
"""

import unittest
from validador_cpf import LimpezaCPF, ValidadorCPF


class TestLimpezaCPF(unittest.TestCase):
    """
    Testes para a classe LimpezaCPF.
    """

    def test_limpeza(self):
        """
        DADO cpf COM caracteres não numéricos
        QUANDO o método limpeza é chamado
        ENTÃO o cpf é retornado sem os caracteres não numéricos
        """
        self.assertEqual(LimpezaCPF.limpeza("123.456.789-00"), "12345678900")
        self.assertEqual(LimpezaCPF.limpeza("000.111.222-33"), "00011122233")
        self.assertEqual(LimpezaCPF.limpeza("abc123def456"), "123456")


class TestValidadorCPF(unittest.TestCase):
    """
    Testes para a classe ValidadorCPF.
    """

    def test_calcular_digito(self):
        """
        DADO uma sequência de números e a posição do dígito
        QUANDO o método _calcular_digito é chamado
        ENTÃO o dígito é calculado corretamente
        """
        self.assertEqual(ValidadorCPF._calcular_digito("987654321", 10), 0)
        self.assertEqual(ValidadorCPF._calcular_digito("9876543210", 11), 10)
        self.assertEqual(ValidadorCPF._calcular_digito("787159503", 10), 2)
        self.assertEqual(ValidadorCPF._calcular_digito("7871595032", 11), 8)

    def test_obter_digito_verificador(self):
        """
        DADO uma sequência de números e a posição do dígito
        QUANDO o método _obter_digito_verificador é chamado
        ENTÃO o dígito verificador é obtido corretamente
        """
        self.assertEqual(
            ValidadorCPF._obter_digito_verificador("987654321", 10), 0)
        self.assertEqual(
            ValidadorCPF._obter_digito_verificador("9876543210", 11), 0)
        self.assertEqual(
            ValidadorCPF._obter_digito_verificador("787159503", 10), 2)
        self.assertEqual(
            ValidadorCPF._obter_digito_verificador("7871595032", 11), 8)

    def test_validar_digitos(self):
        """
        DADO uma sequência de números com dígitos verificadores
        QUANDO o método _validar_digitos é chamado
        ENTÃO os dígitos verificadores são validados corretamente
        """
        self.assertTrue(ValidadorCPF._validar_digitos("98765432100"))
        self.assertTrue(ValidadorCPF._validar_digitos("78715950328"))
        self.assertFalse(ValidadorCPF._validar_digitos("00000000000"))
        self.assertFalse(ValidadorCPF._validar_digitos("498703"))

    def test_validacao_cpf_valido(self):
        """
        DADO um CPF válido
        QUANDO o método validacao_cpf é chamado
        ENTÃO retorna True
        """
        self.assertTrue(ValidadorCPF("123.456.789-09").validacao_cpf())
        self.assertTrue(ValidadorCPF("98765432100").validacao_cpf())
        self.assertTrue(ValidadorCPF("235.998.567-10").validacao_cpf())

    def test_validacao_cpf_invalido(self):
        """
        DADO um CPF inválido
        QUANDO o método validacao_cpf é chamado
        ENTÃO retorna False
        """
        self.assertFalse(ValidadorCPF("11111111111").validacao_cpf())
        self.assertFalse(ValidadorCPF("123.456.789-00").validacao_cpf())
        self.assertFalse(ValidadorCPF("15698192022").validacao_cpf())
        self.assertFalse(ValidadorCPF("005.998.567-11").validacao_cpf())

    def test_validacao_cpf_formato_invalido(self):
        """
        DADO um CPF com formato inválido
        QUANDO o método validacao_cpf é chamado
        ENTÃO retorna False
        """
        self.assertFalse(ValidadorCPF("123.456.789").validacao_cpf())
        self.assertFalse(ValidadorCPF("abc123def456").validacao_cpf())
        self.assertFalse(ValidadorCPF("123").validacao_cpf())
        self.assertFalse(ValidadorCPF("").validacao_cpf())


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
