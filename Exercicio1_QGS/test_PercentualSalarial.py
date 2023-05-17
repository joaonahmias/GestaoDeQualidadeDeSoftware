from PercentualSalarial import *
import unittest

class TestPercentualSalarial(unittest.TestCase):
    
    def testPercentualSalarial(self):
        lista1 = [("Trabalho 1", 2000),("Trabalho 2", 1220.25),("Trabalho 3", 716.12),("Trabalho 4", 300)]
        resultado_lista1 = [("Trabalho 1", 0.4721),("Trabalho 2", 0.2880),("Trabalho 3", 0.1690),("Trabalho 4",0.0708)]
        self.assertEqual(PercentualSalarial(lista1),resultado_lista1)
        lista2 = [('Trabalho 1', 3000.50), ('Trabalho 2', 5000.00), ('Trabalho 3',0), ('Trabalho 4', 200.50)]
        resultado_lista2 =[('Trabalho 1', 0.3659), ('Trabalho 2', 0.6097), ('Trabalho 3',0), ('Trabalho 4', 0.0244)]
        self.assertEqual(PercentualSalarial(lista2),resultado_lista2)
        lista3 = [('Trabalho 1', 0), ('Trabalho 2', 0), ('Trabalho 3',0), ('Trabalho 4', 0)]
        resultado_lista3 =[('Trabalho 1', 0), ('Trabalho 2', 0), ('Trabalho 3',0), ('Trabalho 4', 0)]
        self.assertEqual(PercentualSalarial(lista3),resultado_lista3)
    
    def test_PercentualRendaMedia(self):
        mes1 = (["trabalho 1", 2000],["trabalho 2", 3000],["trabalho 3", 1200])
        mes2 = (["trabalho 1", 1300],["trabalho 2", 1000],["trabalho 3", 200])
        mes3 = (["trabalho 1", 3140],["trabalho 2", 0],["trabalho 3", 1800])
        lista = [mes1,mes2,mes3]
        lista_esperada = [("trabalho 1", 0.4721),("trabalho 2", 0.2933),("trabalho 3", 0.2346)]
        self.assertEqual(percentual_renda_media(lista) ,lista_esperada)