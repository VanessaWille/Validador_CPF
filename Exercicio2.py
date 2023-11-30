import unittest
from Exercicio1 import LimpezaCPF, ValidadorCPF

class TestLimpezaCPF(unittest.TestCase):
    """
    Testa se o método limpeza de LimpezaCPF remove corretamente os caracteres 
    não numéricos.
    """
    def test_limpeza(self):
        self.assertEqual(LimpezaCPF.limpeza("123.456.789-00"), "12345678900")
        self.assertEqual(LimpezaCPF.limpeza("000.111.222-33"), "00011122233")
        self.assertEqual(LimpezaCPF.limpeza("abc123def456"), "123456")

class TestValidadorCPF(unittest.TestCase):
    """
    Testa se o método _calcular_digito calcula corretamente o dígito verificador.
    """
    def test_calcular_digito(self):
        self.assertEqual(ValidadorCPF._calcular_digito("987654321", 10), 0)
        self.assertEqual(ValidadorCPF._calcular_digito("9876543210", 11), 10)
        self.assertEqual(ValidadorCPF._calcular_digito("787159503", 10), 2)
        self.assertEqual(ValidadorCPF._calcular_digito("7871595032", 11), 8)

    """ 
    Testa se o método _obter_digito_verificador obtém corretamente o dígito 
    verificador. 
    """
    def test_obter_digito_verificador(self):
        self.assertEqual(ValidadorCPF._obter_digito_verificador("987654321", 10), 0)
        self.assertEqual(ValidadorCPF._obter_digito_verificador("9876543210", 11), 0)
        self.assertEqual(ValidadorCPF._obter_digito_verificador("787159503", 10), 2)
        self.assertEqual(ValidadorCPF._obter_digito_verificador("7871595032", 11), 8)

    """
    Testa se o método _validar_digitos valida corretamente os dígitos 
    verificadores.
    """
    def test_validar_digitos(self):
        self.assertTrue(ValidadorCPF._validar_digitos("98765432100"))
        self.assertTrue(ValidadorCPF._validar_digitos("78715950328"))
        self.assertFalse(ValidadorCPF._validar_digitos("00000000000"))
        self.assertFalse(ValidadorCPF._validar_digitos("498703"))

    """
    Testa se CPFs válidos passam na validação do método validacao_cpf.
    """
    def test_validacao_cpf_valido(self):
        self.assertTrue(ValidadorCPF("123.456.789-09").validacao_cpf())
        self.assertTrue(ValidadorCPF("98765432100").validacao_cpf())
        self.assertTrue(ValidadorCPF("235.998.567-10").validacao_cpf())

    """
    Testa se se CPFs inválidos falham na validação do método validacao_cpf.
    """
    def test_validacao_cpf_invalido(self):
        self.assertFalse(ValidadorCPF("11111111111").validacao_cpf())
        self.assertFalse(ValidadorCPF("123.456.789-00").validacao_cpf())
        self.assertFalse(ValidadorCPF("15698192022").validacao_cpf())
        self.assertFalse(ValidadorCPF("005.998.567-11").validacao_cpf())

    """
    Testa se CPFs com formatos inválidos falham na validação do método 
    validacao_cpf.
    """
    def test_validacao_cpf_formato_invalido(self):
        self.assertFalse(ValidadorCPF("123.456.789").validacao_cpf())
        self.assertFalse(ValidadorCPF("abc123def456").validacao_cpf())
        self.assertFalse(ValidadorCPF("123").validacao_cpf())
        self.assertFalse(ValidadorCPF("").validacao_cpf())

if __name__ == '__main__':
    unittest.main() # pragma: no cover
