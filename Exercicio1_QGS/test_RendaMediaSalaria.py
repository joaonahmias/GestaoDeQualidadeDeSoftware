import unittest
from PercentualSalarial import *


class TestPercentualRendaMedia(unittest.TestCase):
    def test_PercentualRendaMedia(self):
        mes1 = (["trabalho 1", 2000],["trabalho 2", 3000],["trabalho 3", 1200])
        mes2 = (["trabalho 1", 1300],["trabalho 2", 1000],["trabalho 3", 200])
        mes3 = (["trabalho 1", 3140],["trabalho 2", 0],["trabalho 3", 1800])
        lista = [mes1,mes2,mes3]
        lista_esperada = (["trabalho 1", 0.4545],["trabalho 2", 0.1832],["trabalho 3", 0.3621])
        self.assertEqual(percentual_renda_media(lista) ,lista_esperada)
