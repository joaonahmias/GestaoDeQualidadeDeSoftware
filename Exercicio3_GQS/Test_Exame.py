import unittest
from Exame import Exames_alterados
from Exame import Quantidade_exames_medico
class Test_Exame(unittest.TestCase):
    def test_exames_alterados(self):
        lista = [(1, 1, '5/2/22', 100), (1, 2, '5/2/22', 90), (2, 1,'4/9/21', 250)]
        exame1 = 1
        valor_esperado = 120
        r_esperado = 50
        self.assertEqual(Exames_alterados(lista,exame1,valor_esperado),r_esperado)

    def test_quantidade_exames_medico(self):
        lista = [(1, 1, '5/2/22', 100), (1, 2, '5/2/22', 90), (2, 1,'4/9/21', 250)]
        medico = 1
        r_esperado = 2
        self.assertEqual(Quantidade_exames_medico(lista,medico),r_esperado)
        medico = 3
        r_esperado = 0
        self.assertEqual(Quantidade_exames_medico(lista,medico),r_esperado)

        


